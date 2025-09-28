from pyrogram import Client, filters
import requests, re
from plugins.utility.db import get_user_rank,is_user_registered

@Client.on_message(filters.command(["bin"], ["/", "."]))
async def bin(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    if not await is_user_registered(user_id):
        await message.reply_text("You are not registered. Use /register to register.")
        return
    input = re.findall(r'\b(\d{6})', message.text)
    BIN = input[0] if input else None

    # If no BIN is found in the command, check for a reply
    if not BIN and message.reply_to_message:
        ecx = message.reply_to_message.text.strip()
        BIN_match = re.findall(r'\b(\d{6})', ecx)
        BIN = BIN_match[0] if BIN_match else None

    # Get the user's rank
    rank = await get_user_rank(user_id)

    # Check if a valid 6-digit BIN was extracted
    if not BIN or len(BIN) < 6:
        return await message.reply("<b>𝐔𝐬𝐞 <code>/bin 440393</code></b>", reply_to_message_id=message.id)

    # Request the BIN info from the API
    try:
        response = requests.get(f"http://62.72.177.132:8000/bin/{BIN}")
        
        if response.status_code == 404:
            return await message.reply("Bin not found.")
        elif response.status_code != 200:
            return await message.reply("An error occurred while looking up the BIN.")

        req = response.json()
        brand = req.get('brand') or '------'
        typea = req.get('type') or '------'
        level = req.get('level') or '------'
        bank = req.get('bank') or '------'
        country = req.get('country') or '------'
        country_flag = req.get('flag') or '🏳️'

        await message.reply_text(f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐁𝐈𝐍 𝐥𝐨𝐨𝐤𝐮𝐩 𝐀𝐩𝐢
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐈𝐍 ⇢ <code>{BIN}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐈𝐧𝐟𝐨 ⇢ {brand}-{typea}-{level}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐈𝐬𝐬𝐮𝐞𝐫 ⇢ <code>{bank}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇢ {country} [<code>{country_flag}</code>]
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{first_name}</a> <b>[{rank}]</b>
""", reply_to_message_id=message.id, disable_web_page_preview=True)
    except requests.exceptions.RequestException as e:
        await message.reply("An error occurred while trying to look up the BIN.")
