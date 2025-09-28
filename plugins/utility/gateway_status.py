import asyncio
from plugins.utility.db import gateways_collection

# Cache for gateway statuses to reduce database queries
gateway_status_cache = {}
gateway_cache_last_update = 0
CACHE_TTL = 30  # Cache time-to-live in seconds

# Create a semaphore to limit concurrent database operations
db_semaphore = asyncio.Semaphore(10)

# Function to check if a gateway is active directly from the database
async def is_gateway_active(command):
    """Check if a gateway command is active by querying the database
    
    Args:
        command (str): The command to check (with or without prefix)
        
    Returns:
        bool: True if the gateway is active, False otherwise
    """
    import time
    global gateway_status_cache, gateway_cache_last_update
    
    # Normalize command format
    if not command.startswith('/'):
        command = f'/{command}'
    
    # Check cache first
    current_time = time.time()
    if command in gateway_status_cache and current_time - gateway_cache_last_update < CACHE_TTL:
        return gateway_status_cache[command]
    
    # If not in cache or cache expired, query the database
    async with db_semaphore:
        gateway = await gateways_collection.find_one({"command": command})
    
    # Update cache
    if current_time - gateway_cache_last_update >= CACHE_TTL:
        # Refresh entire cache if it's expired
        gateway_status_cache = {}
        gateway_cache_last_update = current_time
    
    # Store result in cache
    is_active = gateway is not None and gateway.get("status") != "off"
    gateway_status_cache[command] = is_active
    
    return is_active

# Function to update gateway status in both database and cache
async def update_gateway_status(command, status):
    """Update a gateway's status in the database and cache
    
    Args:
        command (str): The command to update (with or without prefix)
        status (str): The new status ('on' or 'off')
        
    Returns:
        bool: True if the update was successful, False otherwise
    """
    from datetime import datetime
    global gateway_status_cache
    
    # Normalize command format
    if not command.startswith('/'):
        command = f'/{command}'
    
    # Update database
    async with db_semaphore:
        result = await gateways_collection.update_one(
            {"command": command},
            {"$set": {"status": status, "updated_at": datetime.now()}}
        )
    
    # Update cache
    gateway_status_cache[command] = (status == 'on')
    
    return result.modified_count > 0