from pyrogram import Client, filters
from plugins.utility.db import delete_gateway, is_user_admin, is_user_owner
from commands_status import update_command_status
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Create a thread pool for CPU-bound operations
thread_pool = ThreadPoolExecutor(max_workers=4)

# Create a semaphore to limit concurrent database operations
db_semaphore = asyncio.Semaphore(10)

@Client.on_message(filters.command("delgate", prefixes=["/", "."]))
async def delete_gate_command(client, message):
    # Process the command in a non-blocking way
    asyncio.create_task(process_delete_gate_command(client, message))
    
    # Send an immediate acknowledgment to improve user experience
    await message.reply_text("Processing your request...", reply_to_message_id=message.id)

async def process_delete_gate_command(client, message):
    user_id = message.from_user.id
    
    # Check if the user is an admin or owner
    is_admin = await is_user_admin(user_id)
    is_owner = await is_user_owner(user_id)
    
    if not is_admin and not is_owner:
        await message.reply_text("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    
    # Check command format
    if len(message.command) < 2:
        await message.reply_text(
            "Invalid format. Use: `/delgate command`\n"
            "Example: `/delgate sa3`", 
            reply_to_message_id=message.id
        )
        return
    
    # Parse the command arguments
    try:
        command = message.command[1].strip()
        
        # Add the '/' prefix if not present
        if not command.startswith("/"):
            command = "/" + command
        
        # Use a semaphore to limit concurrent database operations
        async with db_semaphore:
            # Delete the gateway from the database
            result = await delete_gateway(command)
        
        # Update command status in a separate thread to avoid blocking
        cmd_without_prefix = command[1:] # Remove the '/' prefix for command status
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(
            thread_pool,
            update_command_status,
            cmd_without_prefix,
            "off"
        )
        
        if result.deleted_count > 0:
            await message.reply_text(f"Gateway '{command}' has been deleted successfully.", reply_to_message_id=message.id)
        else:
            await message.reply_text(f"Gateway '{command}' not found in the database.", reply_to_message_id=message.id)
    
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}", reply_to_message_id=message.id)