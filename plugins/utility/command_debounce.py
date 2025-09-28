import json
import os
import time
import asyncio
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Constants
DEBOUNCE_THRESHOLD = 3  # Seconds to wait before processing the same command again
COMMAND_HISTORY_FILE = 'command_history.json'  # File to store command history

# Create a semaphore to limit concurrent access to the command history file
file_lock = asyncio.Lock()

# Create an in-memory cache to reduce file I/O operations
command_history_cache = {}
command_cache_last_update = 0
CACHE_TTL = 10  # Cache time-to-live in seconds

# Create a dictionary to track active commands per user
active_commands = {}

# Load or create command history JSON file with file locking
async def load_command_history():
    global command_history_cache, command_cache_last_update
    
    # Return cached data if it's still fresh
    current_time = time.time()
    if command_history_cache and current_time - command_cache_last_update < CACHE_TTL:
        return command_history_cache.copy()
    
    # Otherwise load from file with proper locking
    async with file_lock:
        try:
            with open(COMMAND_HISTORY_FILE, 'r') as file:
                command_history_cache = json.load(file)
                command_cache_last_update = current_time
                return command_history_cache.copy()
        except (FileNotFoundError, json.JSONDecodeError):
            command_history_cache = {}
            command_cache_last_update = current_time
            return {}

# Save command history to JSON file with file locking
async def save_command_history(command_history):
    global command_history_cache, command_cache_last_update
    
    # Update the cache
    command_history_cache = command_history.copy()
    command_cache_last_update = time.time()
    
    # Save to file with proper locking
    async with file_lock:
        with open(COMMAND_HISTORY_FILE, 'w') as file:
            json.dump(command_history, file, indent=4)

# Clean old entries from command history
async def clean_command_history():
    command_history = await load_command_history()
    current_time = time.time()
    
    # Remove entries older than 1 hour
    command_history = {user_id: {
        cmd: data for cmd, data in user_cmds.items() 
        if current_time - data['timestamp'] < 3600
    } for user_id, user_cmds in command_history.items()}
    
    # Remove empty user entries
    command_history = {user_id: user_cmds for user_id, user_cmds in command_history.items() if user_cmds}
    
    await save_command_history(command_history)

# Check if a command is being executed too quickly (debounce)
async def is_duplicate_command(user_id, command, message_id=None):
    from plugins.utility.db import gateways_collection
    
    # First check if the command is a gateway command and if it's active in the database
    if command.startswith('/'):
        command_without_prefix = command[1:]
    else:
        command_without_prefix = command
    
    # Check gateway status in database first
    gateway = await gateways_collection.find_one({"command": f"/{command_without_prefix}"})
    if gateway and gateway.get("status") == "off":
        return True  # Gateway is marked as inactive in database
    
    # Continue with debounce check
    command_history = await load_command_history()
    current_time = time.time()
    user_id_str = str(user_id)
    
    # Initialize user entry if not exists
    if user_id_str not in command_history:
        command_history[user_id_str] = {}
    
    # Check if command exists for this user
    if command in command_history[user_id_str]:
        last_execution = command_history[user_id_str][command]
        time_diff = current_time - last_execution['timestamp']
        
        # If message_id is provided and matches the last one, it's definitely a duplicate
        if message_id and last_execution.get('message_id') == message_id:
            return True
        
        # If the command was executed very recently, consider it a duplicate
        if time_diff < DEBOUNCE_THRESHOLD:
            return True
    
    # Update the command history with this execution
    command_history[user_id_str][command] = {
        'timestamp': current_time,
        'message_id': message_id
    }
    await save_command_history(command_history)
    
    # Periodically clean old entries (1% chance per call to avoid doing it too often)
    if hash(str(current_time)) % 100 == 0:
        asyncio.create_task(clean_command_history())  # Run cleaning in background
    
    return False