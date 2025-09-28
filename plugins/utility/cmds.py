from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from .db import *
from main import *
from commands_status import get_command_status, update_command_status
import re

# Command to add a new gateway to the database
@Client.on_message(filters.command("addgateway", prefixes=["/", "."]))
async def add_gateway_cmd(bot: Client, m: Message):
    user_id = m.from_user.id
    
    # Only owners can add gateways
    if not await is_user_owner(user_id):
        await m.reply_text("Only bot owners can add new gateways.", reply_to_message_id=m.id)
        return
    
    # Check command format
    if len(m.command) < 2:
        await m.reply_text(
            "Invalid format. Use: `/addgateway category:name:command:status`\n"
            "Example: `/addgateway auth:Stripe Auth 3:/sa3:on`", 
            reply_to_message_id=m.id
        )
        return
    
    # Parse the command arguments
    try:
        args = m.text.split(None, 1)[1]
        parts = args.split(":")
        
        if len(parts) < 3 or len(parts) > 4:
            await m.reply_text(
                "Invalid format. Use: `/addgateway category:name:command:status`\n"
                "Example: `/addgateway auth:Stripe Auth 3:/sa3:on`", 
                reply_to_message_id=m.id
            )
            return
        
        category = parts[0].strip().lower()
        name = parts[1].strip()
        command = parts[2].strip()
        
        # Add the '/' prefix if not present
        if not command.startswith("/"):
            command = "/" + command
        
        # Status is optional, defaults to 'on'
        status = "on"
        if len(parts) == 4:
            status = parts[3].strip().lower()
            if status not in ["on", "off"]:
                await m.reply_text("Status must be 'on' or 'off'.", reply_to_message_id=m.id)
                return
        
        # Add the gateway to the database
        cmd_without_prefix = command[1:] # Remove the '/' prefix for command status
        success = await add_gateway(category, name, command, status)
        
        # Also update the command status in the command_status.txt file
        update_command_status(cmd_without_prefix, status)
        
        if success:
            await m.reply_text(f"Gateway '{name}' added successfully to the '{category}' category.", reply_to_message_id=m.id)
        else:
            await m.reply_text("Failed to add gateway. Please try again.", reply_to_message_id=m.id)
    
    except Exception as e:
        await m.reply_text(f"Error: {str(e)}", reply_to_message_id=m.id)

# Database functions to check gateway access permissions
async def can_access_auth_gateways(user_id):
    # Check if user has permission to access auth gateways
    user = await authorized_users_collection.find_one({"id": user_id})
    return user is not None

async def can_access_charge_gateways(user_id):
    # Check if user has permission to access charge gateways
    user = await authorized_users_collection.find_one({"id": user_id})
    return user is not None

async def can_access_mass_gateways(user_id):
    # Check if user has permission to access mass gateways
    # Only premium users or owners can access mass gateways
    user = await authorized_users_collection.find_one({"id": user_id})
    if not user:
        return False
    return user.get("role") in ["premium", "owner"]

# Calculate total number of gateways dynamically
async def get_total_gateways():
    return await get_gateway_count()

async def is_user_registered(user_id):
    return bool(users_collection.find_one({"user_id": user_id}))

@Client.on_message(filters.command("start", prefixes=["/", "."]))
async def start(bot: Client, m: Message):
    user_id = m.from_user.id
    username = m.from_user.username
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Commands", callback_data="cmds")]]
    )
    txt = f'''
<b>Hello </b><b>@{username}</b><b>! </b>[<code>{user_id}</code>]<b>
Operational Bot!
- - - - - - - - - - - - - - - - - - - - - 
Status: Active ✅
- - - - - - - - - - - - - - - - - - - - - 
Use the button below to view commands or use '/cmds' .

Developer: </b><b>@XAY4N</b>
'''
    await m.reply_text(txt, reply_to_message_id=m.id, reply_markup=markup)

@Client.on_message(filters.command("cmds", prefixes=["/", "."]))
async def handle_cmds(bot: Client, m: Message):
    user_id = m.from_user.id

    if not await is_user_registered(user_id):
        await m.reply_text("Please register first using the /register command.", reply_to_message_id=m.id)
        return

    total_gateways = await get_total_gateways()   # Get dynamic count of gateways

    markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Gateways", callback_data="gateways_1"),
             InlineKeyboardButton(text="Tools", callback_data="tools")],
            [InlineKeyboardButton(text="Close", callback_data="close")]
        ]
    )
    txt = f'''
<b>Available Commands:
━━━━━━━━━━━━
Total Gateways: <code>{total_gateways}</code>
Total Tools: <code>7</code>
━━━━━━━━━━━━
Developer: @XAY4N</b>
'''
    await m.reply_text(txt, reply_markup=markup, reply_to_message_id=m.id)

@Client.on_callback_query()
async def callpri(bot: Client, callback_query: CallbackQuery):
    # Check if the callback query is from a message that was a reply to a command
    if callback_query.message.reply_to_message:
        # Get the original command sender's ID
        original_sender_id = callback_query.message.reply_to_message.from_user.id
        # Get the ID of the user clicking the button
        clicking_user_id = callback_query.from_user.id
        
        # If the user clicking is not the original sender
        if original_sender_id != clicking_user_id:
            await callback_query.answer("❗️ Error: Only the user who sent the command can use these buttons.", show_alert=True)
            return
    
    await callback_query.continue_propagation()

@Client.on_callback_query(filters.regex("cmds|gateways_\\d+|tools|nexttool1|close|auth|charge|mass|special|auth_page_\\d+|charge_page_\\d+|mass_page_\\d+|special_page_\\d+"))
async def callback_query_handler(bot: Client, call: CallbackQuery):
    user_id = call.from_user.id

    if call.data.startswith("gateways_"):
        # Extract page number from callback data
        page_number = int(call.data.split("_")[1])
        
        # Create buttons for different gateway categories
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Auth Gateways", callback_data="auth"), 
             InlineKeyboardButton("Charge Gateways", callback_data="charge")],
            [InlineKeyboardButton("Mass Gateways", callback_data="mass"),
             InlineKeyboardButton("Special Gateways", callback_data="special")],
            [InlineKeyboardButton("Back", callback_data="cmds"),
             InlineKeyboardButton("Close", callback_data="close")]
        ])
        
        total_gateways = await get_total_gateways()
        txt = f'''
<b>Gateway Categories:</b>
━━━━━━━━━━━━
<b>Total Gateways: <code>{total_gateways}</code></b>
━━━━━━━━━━━━
<b>Select a gateway category from below:</b>
'''
        
        await call.message.edit_text(txt, reply_markup=markup)
        return
    user_id = call.from_user.id

    if call.data == "cmds":
        total_gateways = await get_total_gateways()  # Get dynamic count of gateways
        txt = f'''
<b>Available Commands:
━━━━━━━━━━━━
Total Gateways: <code>{total_gateways}</code>
Total Tools: <code>7</code>
━━━━━━━━━━━━
Developer: @XAY4N</b>
'''
        markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Auth Gates", callback_data="auth"), InlineKeyboardButton("Charge Gates", callback_data="charge")],
                [InlineKeyboardButton("Mass Gates", callback_data="mass"), InlineKeyboardButton("Tools", callback_data="tools")],
                [InlineKeyboardButton("Close", callback_data="close")]
            ]
        )
        await call.message.edit_text(txt, reply_markup=markup)

    elif call.data == "auth" or call.data.startswith("auth_page_"):
        # Check if user has permission to access auth gateways
        if not await can_access_auth_gateways(user_id):
            await call.answer("You don't have permission to access Auth gateways. Please upgrade your subscription.", show_alert=True)
            return
        
        # Extract page number from callback data
        if call.data == "auth":
            page = 1
        else:
            page = int(call.data.split("_")[-1])
            
        auth_commands = await get_gateways_by_category("auth")
        total_gateways = len(auth_commands)
        total_pages = (total_gateways + 4) // 5  # Calculate total pages (5 gateways per page)
        
        # Calculate start and end indices for current page
        start_idx = (page - 1) * 5
        end_idx = min(start_idx + 5, total_gateways)
        
        txt = f"<b>Authentication Gateways:</b> (Page {page}/{total_pages})\n━━━━━━━━━━━━\n"
        
        # Display only gateways for current page
        for i in range(start_idx, end_idx):
            gateway = auth_commands[i]
            command_name = gateway["name"]
            command = gateway["command"]
            status = gateway["status"]
            status_icon = "✅" if status == "on" else "❌"
            txt += f'𝐍𝐚𝐦𝐞: {command_name}\n𝐒𝐭𝐚𝐭𝐮𝐬: {status_icon}\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>{command}</code>\n━━━━━━━━━━━━\n'
        
        # Create navigation buttons
        buttons = []
        if total_pages > 1:
            nav_buttons = []
            if page > 1:
                nav_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"auth_page_{page-1}"))
            if page < total_pages:
                nav_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"auth_page_{page+1}"))
            buttons.append(nav_buttons)
        
        buttons.append([InlineKeyboardButton(text="Back", callback_data="cmds"), InlineKeyboardButton(text="Close", callback_data="close")])
        markup = InlineKeyboardMarkup(buttons)
        
        await call.message.edit_text(txt, reply_markup=markup)
        
    elif call.data == "charge" or call.data.startswith("charge_page_"):
        # Check if user has permission to access charge gateways
        if not await can_access_charge_gateways(user_id):
            await call.answer("You don't have permission to access Charge gateways. Please upgrade your subscription.", show_alert=True)
            return
        
        # Extract page number from callback data
        if call.data == "charge":
            page = 1
        else:
            page = int(call.data.split("_")[-1])
            
        charge_commands = await get_gateways_by_category("charge")
        total_gateways = len(charge_commands)
        total_pages = (total_gateways + 4) // 5  # Calculate total pages (5 gateways per page)
        
        # Calculate start and end indices for current page
        start_idx = (page - 1) * 5
        end_idx = min(start_idx + 5, total_gateways)
        
        txt = f"<b>Charge Gateways:</b> (Page {page}/{total_pages})\n━━━━━━━━━━━━\n"
        
        # Display only gateways for current page
        for i in range(start_idx, end_idx):
            gateway = charge_commands[i]
            command_name = gateway["name"]
            command = gateway["command"]
            status = gateway["status"]
            status_icon = "✅" if status == "on" else "❌"
            txt += f'𝐍𝐚𝐦𝐞: {command_name}\n𝐒𝐭𝐚𝐭𝐮𝐬: {status_icon}\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>{command}</code>\n━━━━━━━━━━━━\n'
        
        # Create navigation buttons
        buttons = []
        if total_pages > 1:
            nav_buttons = []
            if page > 1:
                nav_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"charge_page_{page-1}"))
            if page < total_pages:
                nav_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"charge_page_{page+1}"))
            buttons.append(nav_buttons)
        
        buttons.append([InlineKeyboardButton(text="Back", callback_data="cmds"), InlineKeyboardButton(text="Close", callback_data="close")])
        markup = InlineKeyboardMarkup(buttons)
        
        await call.message.edit_text(txt, reply_markup=markup)
        
    elif call.data == "mass" or call.data.startswith("mass_page_"):
        # Check if user has permission to access mass gateways
        if not await can_access_mass_gateways(user_id):
            await call.answer("Mass gateways are only available for premium users. Please upgrade your subscription.", show_alert=True)
            return
        
        # Extract page number from callback data
        if call.data == "mass":
            page = 1
        else:
            page = int(call.data.split("_")[-1])
            
        mass_commands = await get_gateways_by_category("mass")
        total_gateways = len(mass_commands)
        total_pages = (total_gateways + 4) // 5  # Calculate total pages (5 gateways per page)
        
        # Calculate start and end indices for current page
        start_idx = (page - 1) * 5
        end_idx = min(start_idx + 5, total_gateways)
        
        txt = f"<b>Mass Gateways:</b> (Page {page}/{total_pages})\n━━━━━━━━━━━━\n"
        
        # Display only gateways for current page
        for i in range(start_idx, end_idx):
            gateway = mass_commands[i]
            command_name = gateway["name"]
            command = gateway["command"]
            status = gateway["status"]
            status_icon = "✅" if status == "on" else "❌"
            txt += f'𝐍𝐚𝐦𝐞: {command_name}\n𝐒𝐭𝐚𝐭𝐮𝐬: {status_icon}\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>{command}</code>\n━━━━━━━━━━━━\n'
        
        # Create navigation buttons
        buttons = []
        if total_pages > 1:
            nav_buttons = []
            if page > 1:
                nav_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"mass_page_{page-1}"))
            if page < total_pages:
                nav_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"mass_page_{page+1}"))
            buttons.append(nav_buttons)
        
        buttons.append([InlineKeyboardButton(text="Back", callback_data="cmds"), InlineKeyboardButton(text="Close", callback_data="close")])
        markup = InlineKeyboardMarkup(buttons)
        
        await call.message.edit_text(txt, reply_markup=markup)
        
    elif call.data == "special" or call.data.startswith("special_page_"):
        # Special gateways like VBV lookup
        # Extract page number from callback data
        if call.data == "special":
            page = 1
        else:
            page = int(call.data.split("_")[-1])
            
        special_commands = await get_gateways_by_category("special")
        total_gateways = len(special_commands)
        total_pages = (total_gateways + 4) // 5  # Calculate total pages (5 gateways per page)
        
        # Calculate start and end indices for current page
        start_idx = (page - 1) * 5
        end_idx = min(start_idx + 5, total_gateways)
        
        txt = f"<b>Special Gateways:</b> (Page {page}/{total_pages})\n━━━━━━━━━━━━\n"
        
        # Display only gateways for current page
        for i in range(start_idx, end_idx):
            gateway = special_commands[i]
            command_name = gateway["name"]
            command = gateway["command"]
            status = gateway["status"]
            status_icon = "✅" if status == "on" else "❌"
            txt += f'𝐍𝐚𝐦𝐞: {command_name}\n𝐒𝐭𝐚𝐭𝐮𝐬: {status_icon}\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>{command}</code>\n━━━━━━━━━━━━\n'
        
        # Create navigation buttons
        buttons = []
        if total_pages > 1:
            nav_buttons = []
            if page > 1:
                nav_buttons.append(InlineKeyboardButton(text="⬅️ Previous", callback_data=f"special_page_{page-1}"))
            if page < total_pages:
                nav_buttons.append(InlineKeyboardButton(text="Next ➡️", callback_data=f"special_page_{page+1}"))
            buttons.append(nav_buttons)
        
        buttons.append([InlineKeyboardButton(text="Back", callback_data="cmds"), InlineKeyboardButton(text="Close", callback_data="close")])
        markup = InlineKeyboardMarkup(buttons)
        
        await call.message.edit_text(txt, reply_markup=markup)

    elif call.data == "tools":
        txt = '''
<b>Available Tools:</b>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐂𝐂 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐀𝐩𝐢 - ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/gen 440393</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐁𝐈𝐍 𝐥𝐨𝐨𝐤𝐮𝐩 𝐀𝐩𝐢 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/bin 440393</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐏𝐢𝐧𝐠 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/ping</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐅𝐚𝐤𝐞 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/fake us</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/id</code>
'''
        markup = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Back", callback_data="cmds")],
        [InlineKeyboardButton(text="Next", callback_data="nexttool1")],
        [InlineKeyboardButton(text="Close", callback_data="close")]
    ]
)

        await call.message.edit_text(txt, reply_markup=markup)
    
    elif call.data == "nexttool1":
        txt = '''
<b>Available Tools:</b>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐨𝐫 𝐀𝐩𝐢 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/tr en</code>
━━━━━━━━━━━━
𝐍𝐚𝐦𝐞: 𝐒𝐭𝐫𝐢𝐩𝐞 𝐊𝐞𝐲 𝐋𝐨𝐨𝐤𝐮𝐩 𝐀𝐩𝐢 ✅
𝐂𝐨𝐦𝐦𝐚𝐧𝐝: <code>/sk sk_live...</code>
'''
        markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text="Back", callback_data="tools")],
            [InlineKeyboardButton(text="Close", callback_data="close")]
        ]
    )

        await call.message.edit_text(txt, reply_markup=markup)

    elif call.data == "close":
        await call.message.delete()
        
    else:
        # Handle case where the gateway is not found
        await call.message.edit_text(
            "❗️ Error: Gateway not found.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="gateways_1")]])
        )

@Client.on_message(filters.command("updategateway", prefixes=["/", "."]))
async def update_gateway_cmd(bot: Client, m: Message):
    user_id = m.from_user.id
    
    # Only owners can update gateways
    if not await is_user_owner(user_id):
        await m.reply_text("Only bot owners can update gateway details.", reply_to_message_id=m.id)
        return
    
    # Check command format
    if len(m.command) < 2:
        await m.reply_text(
            "Invalid format. Use: `/updategateway command:status`\n"
            "Example: `/updategateway sa3:off`", 
            reply_to_message_id=m.id
        )
        return
    
    # Parse the command arguments
    try:
        args = m.text.split(None, 1)[1]
        parts = args.split(":")
        
        if len(parts) != 2:
            await m.reply_text(
                "Invalid format. Use: `/updategateway command:status`\n"
                "Example: `/updategateway sa3:off`", 
                reply_to_message_id=m.id
            )
            return
        
        command = parts[0].strip()
        # Add the '/' prefix if not present for database lookup
        if not command.startswith("/"):
            command = "/" + command
            
        status = parts[1].strip().lower()
        
        # Validate status
        if status not in ["on", "off"]:
            await m.reply_text("Status must be 'on' or 'off'.", reply_to_message_id=m.id)
            return
            
        # Update the gateway in the database
        gateway = await get_gateway_by_command(command)
        if not gateway:
            await m.reply_text(f"Gateway with command '{command}' not found.", reply_to_message_id=m.id)
            return
            
        success = await update_gateway_status(command, status)
        
        # Also update the command status in the command_status.txt file
        cmd_without_prefix = command[1:] # Remove the '/' prefix for command status
        update_command_status(cmd_without_prefix, status)
        
        if success:
            await m.reply_text(f"Gateway status updated to '{status}' successfully.", reply_to_message_id=m.id)
        else:
            await m.reply_text("Failed to update gateway status. Please try again.", reply_to_message_id=m.id)
    
    except Exception as e:
        await m.reply_text(f"Error: {str(e)}", reply_to_message_id=m.id)