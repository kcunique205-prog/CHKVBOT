from pyrogram import Client, filters
from plugins.utility.db import *
import asyncio,requests,time
import os.path, sys
from capsolv import *
LOG_CHAT_ID = -1002250449294
prefixes = ['!', '/', '.', '#', '$']
async def log_action(client, message, action, details):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    
    profile_link = f"<a href=\"tg://user?id={user_id}\">{first_name or username}</a>"
    log_text = f"""
<b>Action:</b> {action}
<b>Executor:</b> {profile_link} ({user_id})
<b>Details:</b> {details}
    """
    try:
        await client.send_message(chat_id=LOG_CHAT_ID, text=log_text, disable_web_page_preview=True)
    except Exception as e:
        
        await client.send_message(
            chat_id=OWNER_ID,
            text=f"Error logging action to LOG_CHAT_ID:\n{str(e)}",
            disable_web_page_preview=True
        )


@Client.on_message(filters.command('register', prefixes=prefixes))
async def register(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        if await register_user(user_id, username, first_name, last_name):
            await message.reply(f"User {first_name} has been successfully registered.", reply_to_message_id=message.id)
        else:
            await message.reply("You are already registered.", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply(f"Error during registration: {str(e)}", reply_to_message_id=message.id)

@Client.on_message(filters.command('promote', prefixes=prefixes))
async def promote(client, message):
    user_id = message.from_user.id

    # Check if the user is an admin
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    try:
        # Split the command arguments
        command_parts = message.text.split()

        # Validate command length
        if len(command_parts) < 3:
            await message.reply("Usage: /promote user_id duration [credits]", reply_to_message_id=message.id)
            return
        try:
            target_user_id = int(command_parts[1])
        except ValueError:
            await message.reply("Invalid user ID. Ensure it is a valid number.", reply_to_message_id=message.id)
            return

        # Extract duration
        duration = command_parts[2]

        credits = None
        if len(command_parts) > 3:
            try:
                credits = int(command_parts[3])
            except ValueError:
                await message.reply("Invalid credits. Ensure it is a valid number.", reply_to_message_id=message.id)
                return

        result = await promote_user(target_user_id, duration, credits)
        await message.reply(result, reply_to_message_id=message.id)

        details = f"Promoted user_id: {target_user_id}, Duration: {duration}, Credits: {credits or 'N/A'}"
        # await log_action(client, message, "Promote User", details)

    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)




@Client.on_message(filters.command('demote', prefixes=prefixes))
async def demote(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    try:
        command_parts = message.text.split()
        if len(command_parts) < 2:
            await message.reply("Usage: /demote user_id", reply_to_message_id=message.id)
            return

        target_user_id = int(command_parts[1])
        result = await demote_user(target_user_id)
        await message.reply(result, reply_to_message_id=message.id)
        details = f"Demoted user_id: {target_user_id}"
        # await log_action(client, message, "Demote User", details)

    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)

@Client.on_message(filters.command('gkey', prefixes=prefixes))
async def generate_key_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    try:
        command_parts = message.text.split()
        if len(command_parts) < 2:
            await message.reply("Usage: /gkey duration", reply_to_message_id=message.id)
            return

        duration = command_parts[1]
        key, expire = await generate_key(duration)
        await message.reply(f"Generated key: <code>{key}</code>\nExpiry: <code>{expire}</code>", reply_to_message_id=message.id)
        details = f"Generated key for duration: {duration}, Key: {key}, Expiry: {expire}"
        # await log_action(client, message, "Generate Key", details)

    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)

@Client.on_message(filters.command('claim', prefixes=prefixes))
async def claim_key_command(client, message):
    user_id = message.from_user.id
    command_parts = message.text.split()

    if len(command_parts) < 2:
        await message.reply("Usage: /claim key", reply_to_message_id=message.id)
        return

    key = command_parts[1]
    result = await claim_key(user_id, key)
    await message.reply(result, reply_to_message_id=message.id)

@Client.on_message(filters.command('ac', prefixes=prefixes))
async def add_credits_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):  # Allow any owner or admin to use this command
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    command_parts = message.text.split()
    if len(command_parts) < 3:
        await message.reply("Usage: /ac user_id credits", reply_to_message_id=message.id)
        return
    user = int(command_parts[1])
    credits = int(command_parts[2])
    result = await give_credits(user, credits)
    await message.reply(result, reply_to_message_id=message.id)
    try:
        user_details = f"<a href='tg://user?id={user_id}'>{user_id}</a>"
        log_message = (
            f"#AddCredits\n"
            f"Admin: {user_details}\n"
            f"Target User ID: {user}\n"
            f"Credits Added: {credits}\n"
            f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}"
        )
        await client.send_message(LOG_CHAT_ID, log_message,disable_web_page_preview=True)
    except Exception as e:
        print(f"Error logging add credits action: {e}")


async def message_forward(original_message, user_id):
    try:
        await original_message.copy(chat_id=user_id)
        return True
    except Exception as e:
        return False

@Client.on_message(filters.command('addsk', prefixes=prefixes))
async def add_sk_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    command_parts = message.text.split()
    if len(command_parts) < 3:
        await message.reply("Usage: /addsk sk pk", reply_to_message_id=message.id)
        return
    sk = command_parts[1]
    pk = command_parts[2]
    result = await add_or_update_skpk(sk, pk)
    await message.reply(result, reply_to_message_id=message.id)
    
@Client.on_message(filters.command('addgrp', prefixes=prefixes))
async def add_group_command(client, message):
    user_id = message.from_user.id
    
    # Check if the user is an admin
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    try:
        # Check if message is in a group
        if not message.chat.type in ["group", "supergroup"]:
            await message.reply("This command must be used in a group.", reply_to_message_id=message.id)
            return

        group_id = message.chat.id
        group_title = message.chat.title

        # Add group to authorized groups collection
        result = await groups_collection.update_one(
            {"id": group_id},
            {"$set": {
                "id": group_id,
                "title": group_title,
                "added_by": user_id,
                "added_at": datetime.now()
            }},
            upsert=True
        )

        if result.upserted_id:
            await message.reply(f"Group {group_title} has been authorized successfully.", reply_to_message_id=message.id)
        else:
            await message.reply(f"Group {group_title} was already authorized.", reply_to_message_id=message.id)

    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)

@Client.on_message(filters.command('rmgrp', prefixes=prefixes))
async def remove_group_command(client, message):
    """
    Remove a group from authorized groups list
    Usage: /rmgrp [group_id] (in group chat)
    """
    user_id = message.from_user.id

    # Authorization check
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    try:
        # Validate group context
        if not message.chat.type in ["group", "supergroup"]:
            await message.reply("This command must be used in a group.", reply_to_message_id=message.id)
            return

        group_id = message.chat.id
        group_title = message.chat.title

        # Remove group from collection
        result = await groups_collection.delete_one({"id": group_id})

        # Handle response based on deletion result
        if result.deleted_count:
            await message.reply(f"Group {group_title} has been removed from authorized groups.", reply_to_message_id=message.id)
        else:
            await message.reply(f"Group {group_title} was not authorized.", reply_to_message_id=message.id)

    except Exception as e:
        try:
            # Handle direct group ID input
            command_parts = message.text.split()
            if len(command_parts) < 2:
                await message.reply("Usage: /rmgrp group_id", reply_to_message_id=message.id)
                return

            group_id = int(command_parts[1])
            result = await groups_collection.delete_one({"id": group_id})

            if result.deleted_count:
                await message.reply(f"Group with ID {group_id} has been removed from authorized groups.", reply_to_message_id=message.id)
            else:
                await message.reply(f"Group with ID {group_id} was not authorized.", reply_to_message_id=message.id)

        except ValueError:
            await message.reply("Invalid group ID.", reply_to_message_id=message.id)
        except Exception as e:
            await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)
            
@Client.on_message(filters.command('addowner', prefixes=prefixes))
async def add_owner_command(client, message):
    
    if message.from_user.id != OWNER_ID:  # Only the primary owner can use this command
        await message.reply("Only the primary owner can use this command.", reply_to_message_id=message.id)
        return

    command_parts = message.text.split()
    if len(command_parts) < 2:
        await message.reply("Usage: /addowner user_id", reply_to_message_id=message.id)
        return

    target_user_id = int(command_parts[1])
    result = await add_owner(target_user_id)
    await message.reply(result, reply_to_message_id=message.id)


@Client.on_message(filters.command('removeowner', prefixes=prefixes))
async def remove_owner_command(client, message):
    if message.from_user.id != OWNER_ID:  # Only the primary owner can use this command
        await message.reply("Only the primary owner can use this command.", reply_to_message_id=message.id)
        return

    command_parts = message.text.split()
    if len(command_parts) < 2:
        await message.reply("Usage: /removeowner user_id", reply_to_message_id=message.id)
        return

    target_user_id = int(command_parts[1])
    result = await remove_owner(target_user_id)
    await message.reply(result, reply_to_message_id=message.id)


@Client.on_message(filters.command(commands=['broad', 'broadcast', 'bcast', 'brod'], prefixes=prefixes))
async def brod_cmd(client, message):
    try:
        user_id = message.from_user.id
        if not await is_user_admin(user_id):  # Allow any owner or admin to use this command
            await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
            return
        original_message = message.reply_to_message
        if not original_message:
            await message.reply("Please reply to the message you want to broadcast.")
            return

        all_users = await get_all_user_ids()
        sent_brod = 0
        not_sent = 0
        total_users = len(all_users)
        start = time.perf_counter()

        # Notify the start of the broadcast
        text = f"""
𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 ✅
━━━━━━━━━━━━━━
𝐓𝐨𝐭𝐚𝐥 𝐮𝐬𝐞𝐫: <b>{total_users}</b>
𝐒𝐭𝐚𝐭𝐮𝐬: 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠....
"""
        x = await message.reply_text(text, quote=True)

        async def send_message(user_id):
            nonlocal sent_brod, not_sent
            if await message_forward(original_message, user_id):
                sent_brod += 1
            else:
                not_sent += 1

        tasks = [send_message(user_id) for user_id in all_users]
        worker_num = 25  # Adjust this number based on performance needs

        for i in range(0, len(tasks), worker_num):
            batch = tasks[i:i + worker_num]
            await asyncio.gather(*batch)

        # Calculate the time taken
        taken = str(timedelta(seconds=time.perf_counter() - start))
        hours, minutes, seconds = map(float, taken.split(":"))
        hour = int(hours)
        min = int(minutes)

        success_ratio = (sent_brod / total_users) * 100 if total_users > 0 else 0

        # Final message
        done = f"""
𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
━━━━━━━━━━━━━━
𝐓𝐨𝐭𝐚𝐥 𝐮𝐬𝐞𝐫: <b>{total_users}</b>
𝐒𝐮𝐜𝐜𝐞𝐬𝐬: <b>{sent_brod}</b>
𝐅𝐚𝐢𝐥𝐞𝐝: <b>{not_sent}</b>
𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐑𝐚𝐭𝐢𝐨: <b>{success_ratio:.2f}%</b>
━━━━━━━━━━━━━━
𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧: {hour} 𝐇. {min} 𝐌𝐢𝐧. {seconds:.2f} 𝐒𝐞𝐜.
"""
        await x.edit(done)

    except Exception as e:
        import traceback
        await error_log(traceback.format_exc())
        await message.reply_text(f"Error occurred during broadcast: {str(e)}", quote=True)

async def error_log(error_msg):
    open("error.log", "a").write(error_msg + "\n")

@Client.on_message(filters.command('addproxy', prefixes=prefixes))
async def add_proxy_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    command_parts = message.text.split()
    if len(command_parts) < 2:
        await message.reply("Usage: /addproxy proxy(ip:port:username:password)", reply_to_message_id=message.id)
        return
    proxy = command_parts[1]
    open("proxy.txt", "a").write(proxy + "\n")
    await message.reply("Proxy added successfully.", reply_to_message_id=message.id)

@Client.on_message(filters.command('getproxies', prefixes=prefixes))
async def get_proxies(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    try:
        file_path = "proxy.txt"
        if os.path.exists(file_path):
            await client.send_document(message.chat.id, file_path)
        else:
            await message.reply("No proxies file found.", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)


@Client.on_message(filters.command('updateproxy', prefixes=prefixes))
async def update_proxy_text(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("Please reply to a document containing proxies in the format: ip:port[:username:password].", reply_to_message_id=message.id)
        return
    try:
        # Get the file ID and download the file
        file_id = message.reply_to_message.document.file_id
        file_path = f"proxy.txt"  # Specify the desired file name
        await client.download_media(file_id, file_name=file_path)

        await message.reply("Proxies updated successfully.", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply(f"Error: {str(e)}", reply_to_message_id=message.id)


@Client.on_message(filters.command('restart', prefixes=prefixes))
async def restart_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):  # Allow any owner or admin to use this command
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    await message.reply("Restarting the bot...", reply_to_message_id=message.id)

    try:
        await asyncio.sleep(1)  # Short delay before restarting
        os.execl(sys.executable, sys.executable, *sys.argv)  # Restart the bot process
    except Exception as e:
        print(f"Error during bot restart: {e}")
        sys.exit(1)

@Client.on_message(filters.command('capbal', prefixes=prefixes))
async def capture_balance_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id) and user_id != 6753323467:
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    result = await get_balance()
    await message.reply(f"<b>Your captcha API Balance: <code>{result}</code></b>", reply_to_message_id=message.id)

# Command to update solver configuration
def update_solver_config(path, key, ip_port=None):
    try:
        with open("solver_api.txt", "w") as file:
            if path == "1" and ip_port:
                file.write(f"1|{ip_port}|{key}")
            elif path == "2":
                file.write(f"2|{key}")
        load_solver_config()
        return "Solver configuration updated successfully."
    except Exception as e:
        return f"Error updating solver configuration: {e}"
    
@Client.on_message(filters.command('upsolver', prefixes=prefixes))
async def update_solver_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id):
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return

    command_parts = message.text.split()
    if len(command_parts) < 3:
        await message.reply("Usage: /upsolver <path> <key> [ip:port]", reply_to_message_id=message.id)
        return

    path = command_parts[1]
    key = command_parts[2]
    ip_port = command_parts[3] if len(command_parts) > 3 else None

    if path not in ["1", "2"]:
        await message.reply("Invalid path. Use '1' for custom server or '2' for 2Captcha API.", reply_to_message_id=message.id)
        return

    update_result = update_solver_config(path, key, ip_port)
    await message.reply(update_result, reply_to_message_id=message.id)
    
@Client.on_message(filters.command('testcap', prefixes=prefixes))
async def test_captcha_command(client, message):
    user_id = message.from_user.id
    if not await is_user_admin(user_id) and user_id != 6753323467:
        await message.reply("You are not authorized to use this command.", reply_to_message_id=message.id)
        return
    
    x = await message.reply("Solving captcha...", quote=True)
    start_time = time.perf_counter()
    substring = None  # Initialize the variable
    try:
        solve = await solve_recaptcha("https://www.google.com/recaptcha/api2/demo", "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-")
        if "ERROR" in solve:
            msg = "Error occurred during captcha solving."
        else:
            substring = solve[:10] + "..." + solve[-8:]
            msg = "Captcha solved successfully."
    except:
        msg = "Error occurred during captcha solving."
    
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    
    r = requests.Session()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.google.com',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.google.com/recaptcha/api2/demo',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-form-factors': '"Desktop"',
        'sec-ch-ua-full-version': '"131.0.6778.265"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.265", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-browser-channel': 'stable',
        'x-browser-copyright': 'Copyright 2025 Google LLC. All rights reserved.',
        'x-browser-validation': 'Nbt54E7jcg8lQ4EExJrU2ugNG6o=',
        'x-browser-year': '2025',
        'x-client-data': 'CJC2yQEIpbbJAQiKksoBCKmdygEI3efKAQiWocsBCIWgzQEIydHOAQiz084BCPrXzgEIwdjOAQjN2M4BGPbJzQEYz9XOARjt2s4B',
    }
    data = {
        'g-recaptcha-response': solve,
    }
    response = r.post('https://www.google.com/recaptcha/api2/demo', headers=headers, data=data)
    if "Verification Success" in response.text:
        msg = "Captcha solved successfully."
    else:
        msg = "Captcha solving failed."
    
    text = f"<b>MSG:</b> <i>{msg}</i>\n"
    if substring:  # Check if substring is not None
        text += f"<b>Solution:</b> <code>{substring}</code>\n"
    text += f"<b>Time Taken:</b> <code>{time_taken:.2f}</code> seconds"
    
    await x.edit(text)

