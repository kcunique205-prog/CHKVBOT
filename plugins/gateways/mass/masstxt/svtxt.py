import re
import time
import asyncio
import httpx
import random
import string
from proxy import proxies_aiohttp
from pyrogram import Client, filters
from Gates.skbasedoff import skintoff
from plugins.utility.db import (
    is_user_registered,
    is_user_authorized,
    get_user_credits,
    update_credits,
    get_user_rank,
)
from commands_status import get_command_status
from plugins.utility.banbin import is_bin_banned
from luhn import luhn_verification
import os

# Define the hits folder
HITS_FOLDER = "hits"
MAX_CARD_LIMIT = 2000

# Helper to generate a random secret key
def generate_key(user_id):
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"svtxt_{user_id}_{random_string}"

# Function to process a single card
async def process_card(cc_data):
    cc, mm, yy, cvv = cc_data
    if len(yy) == 2:
        yy = '20' + yy
    cccc = f"{cc}|{mm}|{yy}|{cvv}"

    if not luhn_verification(cc):
        return f"{cccc}\nStatus: Invalid card number (Luhn check failed)", False  # Mark as dead

    is_ban = await is_bin_banned(cc[:6])
    if is_ban:
        return f'{cccc}\nStatus: Banned BIN', False  # Mark as dead

    try:
        prx = await proxies_aiohttp()
        session = httpx.AsyncClient(proxies=prx, timeout=30)
        msg = await skintoff(session, cc, mm, yy, cvv)
    except Exception as e:
        return f"{cccc}\nStatus: Error: {str(e)}", False  # Mark as dead

    # Check for approval based on response
    status = '𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅' if any(
        error_msg in msg for error_msg in [
            "Your card's security code is incorrect.",
            'Succeeded',
            "Charged $1",
            'Your card has insufficient funds.',
            'Insufficient Funds',
            'Transaction Not Allowed',
            'Your card does not support this type of purchase.',
            '3D Secure authentication required',
            "Incorrect Cvc",
            "Invalid Cvc",
            "CVV Live",
        ]
    ) else '𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌'

    result = f"{cccc}\n𝐒𝐭𝐚𝐭𝐮𝐬: {status}\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {msg}"

    # Return result and whether it's live
    return result, status == '𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅'

@Client.on_message(filters.command("svtxt", prefixes=["/", "."]))
async def svtxt(client, message):
    user_id = message.from_user.id
    first_n = message.from_user.first_name
    mid = message.id

    # Check if the command is turned off
    if get_command_status('svtxt') == 'off':
        await message.reply_text("Gate is on maintenance, come back later.", reply_to_message_id=mid)
        return

    # Check if the user is registered
    if not await is_user_registered(user_id):
        await message.reply_text("Please register first using the /register command.", reply_to_message_id=mid)
        return

    # Check if the user is authorized
    is_authorized = await is_user_authorized(user_id)
    if not is_authorized:
        await message.reply_text(
            "Free users are not allowed to use this command.\nTo purchase a bot subscription, use '/buy' for details.",
            reply_to_message_id=mid
        )
        return

    # Check if the user has enough credits
    user_credits = await get_user_credits(user_id) or 0

    rank = await get_user_rank(user_id)
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply("Please reply to a text document containing card details.", reply_to_message_id=mid)
        return

    # Download the document
    doc_path = await message.reply_to_message.download()
    with open(doc_path, 'r') as file:
        ccs = file.read()

    # Reformat and validate card information
    ccs = re.sub(r'[ /\\:]', '|', ccs)
    cc_list = re.findall(r'\b(\d{15}|\d{16})\|(\d{2}|\d{4})\|(\d{4}|\d{2})\|(\d{4}|\d{3})', ccs)
    card_count = len(cc_list)

    if card_count == 0:
        await message.reply('Invalid format! Use: XXXXXXXXXXXXXXXX|MM|YYYY|CVV', reply_to_message_id=mid)
        return

    # Check if card count exceeds the max limit
    if card_count > MAX_CARD_LIMIT:
        await message.reply(f"Maximum allowed cards per batch is {MAX_CARD_LIMIT}. You provided {card_count} cards.", reply_to_message_id=mid)
        return

    # Check if the user has enough credits for the card check
    if user_credits < card_count:
        await message.reply(f"Insufficient credits. You have {user_credits} credits, but {card_count} cards require {card_count} credits.", reply_to_message_id=mid)
        return

    # Deduct credits for the number of cards checked
    await update_credits(user_id, -card_count)

    # Generate a secret key for this session
    secret_key = generate_key(user_id)

    # Create the hits folder if it doesn't exist
    if not os.path.exists(HITS_FOLDER):
        os.makedirs(HITS_FOLDER)

    # Processing message
    progress_message = await message.reply(
        f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED $1 CVV\n"
        f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
        f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭 - {card_count}\n"
        f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 - Checking CC...\n"
        f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing your cards...⌛️\n"
        f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
        f"<b>[<a href='https://t.me/Instuff_bot'>⎇</a>]</b> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 - <a href='tg://user?id={user_id}'>{first_n}</a> <b>[{rank}]</b>\n",
        reply_to_message_id=mid,
        disable_web_page_preview=True
    )

    start_time = time.perf_counter()
    live, dead, checked = 0, 0, 0
    results = []
    live_results = []  # To store live results
    tasks = [process_card(cc) for cc in cc_list]

    for i in range(0, len(tasks), 50):  # Process in batches of 50
        batch_tasks = tasks[i:i + 50]
        batch_results = await asyncio.gather(*batch_tasks)
        
        for result, is_live in batch_results:
            checked += 1
            if is_live:
                live_results.append(result)
                live += 1
            else:
                dead += 1

        # Update progress
        await progress_message.edit(
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED $1 CVV\n"
            f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐂𝐂 𝐀𝐦𝐨𝐮𝐧𝐭 - {card_count}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 - {checked}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐋𝐢𝐯𝐞 - {live}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐃𝐞𝐚𝐝 - {dead}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲 - <code>{secret_key}</code>\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐭𝐚𝐭𝐮𝐬 - Processing your cards...⌛️\n"
            f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>⎇</a>]</b> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 - <a href='tg://user?id={user_id}'>{first_n}</a> <b>[{rank}]</b>\n",
            disable_web_page_preview=True
        )

        # Save to hits folder, limit file size
        if len(live_results) >= 2000:
            result_file_path = f"{HITS_FOLDER}/results_{secret_key}.txt"
            with open(result_file_path, "w") as result_file:
                result_file.write("\n".join(live_results))

            # Reset for the next batch
            live_results = []
            live = 0
            dead = 0

    # Final message and document creation
    end_time = time.perf_counter()
    elapsed_time = f"{int((end_time - start_time) // 3600)}h {int((end_time - start_time) % 3600 // 60)}m {int((end_time - start_time) % 60)}s"

    await progress_message.delete()
    if live_results:
    # If there are live results, save and send the document
        result_file_path = f"{HITS_FOLDER}/results_{secret_key}.txt"
        with open(result_file_path, "w") as result_file:
            result_file.write("\n".join(live_results))

    # Send the result file
        await client.send_document(
            chat_id=message.chat.id,
            document=result_file_path,
            caption=(f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED $1 CVV\n"
                     f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {card_count}\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐋𝐢𝐯𝐞 - {live}\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐃𝐞𝐚𝐝 - {dead}\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐭𝐚𝐭𝐮𝐬 - Checked All ✅\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐞𝐜𝐫𝐞𝐭 𝐊𝐞𝐲 - <code>{secret_key}</code>\n"
                    f"<b>Note: </b> (Retrieve hits: /gethits <i>{secret_key})</i>\n"
                    f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐓𝐢𝐦𝐞 - {elapsed_time}\n"
                    f"<b>[<a href='https://t.me/Instuff_bot'>⎇</a>]</b> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 - <a href='tg://user?id={user_id}'>{first_n}</a> <b>[{rank}]</b>\n"
                    ),
            reply_to_message_id=mid,
        )
    else:
        await message.reply(
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 - SK BASED $1 CVV\n"
            f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐓𝐨𝐭𝐚𝐥 𝐂𝐂 𝐈𝐧𝐩𝐮𝐭 - {card_count}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐋𝐢𝐯𝐞 - {live}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐃𝐞𝐚𝐝 - {dead}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐒𝐭𝐚𝐭𝐮𝐬 - No live cards found. All cards are dead. ❌\n"
            f"<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>ϟ</a>]</b> 𝐓𝐢𝐦𝐞 - {elapsed_time}\n"
            f"<b>[<a href='https://t.me/Instuff_bot'>⎇</a>]</b> 𝐂𝐡𝐞𝐜𝐤𝐞𝐝 𝐁𝐲 - <a href='tg://user?id={user_id}'>{first_n}</a> <b>[{rank}]</b>\n"
            , quote=True,disable_web_page_preview=True
        )

    # Delete the result file from the hits folder if it exists
    if os.path.exists(result_file_path):
        os.remove(result_file_path)


@Client.on_message(filters.command("gethits", prefixes=["/", "."]))
async def gethits(client, message):
    user_id = message.from_user.id
    secret_key = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else None
    mid = message.id

    if not secret_key:
        await message.reply("Please provide a valid secret key.", reply_to_message_id=mid)
        return

    result_file_path = f"{HITS_FOLDER}/results_{secret_key}.txt"

    if not os.path.exists(result_file_path):
        await message.reply("No results found for this key or file has already been deleted.", reply_to_message_id=mid)
        return

    # Send the result file to the user
    await client.send_document(
        chat_id=message.chat.id,
        document=result_file_path,
        caption="Here are the results for the provided key."
    )

    # Delete the result file from the hits folder
    os.remove(result_file_path)
