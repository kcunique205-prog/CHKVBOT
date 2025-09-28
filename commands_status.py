import os
import asyncio
from plugins.utility.gateway_status import is_gateway_active, update_gateway_status

COMMAND_STATUS_FILE = "command_status.txt"

# For backward compatibility
def write_command_statuses(command_statuses):
    with open(COMMAND_STATUS_FILE, 'w') as file:
        for command, status in command_statuses.items():
            file.write(f"{command}:{status}\n")

# Function to get the status of a specific command
def read_command_statuses():
    command_statuses = {}
    if os.path.exists(COMMAND_STATUS_FILE):
        with open(COMMAND_STATUS_FILE, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    command, status = line.split(':')
                    command_statuses[command] = status
    return command_statuses

# Get command status - checks database first, falls back to file
def get_command_status(command):
    # Create a new event loop for async operation in sync context
    loop = asyncio.new_event_loop()
    try:
        # Try to get status from database first
        is_active = loop.run_until_complete(is_gateway_active(command))
        return "on" if is_active else "off"
    except Exception:
        # Fall back to file-based status if database query fails
        command_statuses = read_command_statuses()
        return command_statuses.get(command, "off")  # Return "off" if command is not found
    finally:
        loop.close()

# Update command status in both database and file for backward compatibility
def update_command_status(command, status):
    # Update file-based status for backward compatibility
    command_statuses = read_command_statuses()
    command_statuses[command] = status
    with open(COMMAND_STATUS_FILE, 'w') as file:
        for cmd, sts in command_statuses.items():
            file.write(f"{cmd}:{sts}\n")
    
    # Update database status asynchronously
    try:
        loop = asyncio.new_event_loop()
        loop.run_until_complete(update_gateway_status(command, status))
        loop.close()
    except Exception:
        # If database update fails, at least the file is updated
        pass

# Initialize with default statuses if the file doesn't exist
def initialize_command_statuses():
    if not os.path.exists(COMMAND_STATUS_FILE):
        default_statuses = {
            "chk": "on",
            "cc": "off",
            "b3": "off",
            "cvv": "off",
            "btm": "off",
            "bt": "off",
            "vbv": "off",
            "mo": "on",
            "pf" : "on",
            "pt": "on",
            "lt": "on",
            "sa" : "on",
            "sc" : "on",
            "sd" : "on",
            "sx" : "off",
            "st" : "on",
            "sp" : "on",
            "atn" : "on",
            "pp" : "on",
            "ue" : "on",
            "mst" : "on",
        }
        write_command_statuses(default_statuses)