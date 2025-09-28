from pyrogram import Client, filters
import pyrogram
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from random import randint
import requests,re
import time
from datetime import datetime
import os
from plugins.utility.db import get_user_rank, is_user_registered
# Luhn Algorithm to calculate the last digit and check Luhn validation
def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
        if isSecond:
            d = d * 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond
     
    return (nSum % 10 == 0)

# Updated cc_gen function to generate valid cards with correct length
# Updated cc_gen function
def cc_gen(bin_code, amount, mes=None, ano=None, cvv=None):
    generated_cards = []
    current_year = datetime.now().year

    while len(generated_cards) < amount:
        # Replace 'x' characters with random digits in the BIN
        if 'x' in bin_code:
            random_digits = ''.join([str(randint(0, 9)) for _ in range(bin_code.count('x'))])
            bin_code_with_random = bin_code.replace('x', '{}').format(*random_digits)
        else:
            bin_code_with_random = bin_code

        # Ensure the BIN is exactly 16 digits for most cards (15 for American Express)
        card_length = 15 if bin_code_with_random.startswith('37') else 16

        # Generate the remaining part of the card number
        if len(bin_code_with_random) < card_length:
            cc_base = bin_code_with_random + ''.join([str(randint(0, 9)) for _ in range(card_length - len(bin_code_with_random))])
        else:
            cc_base = bin_code_with_random

        # Validate using Luhn algorithm
        if not checkLuhn(cc_base):
            continue

        # Use provided month/year or randomize them
        card_mes = mes if mes != 'xx' else f'{randint(1, 12):02}'
        card_ano = ano if ano != 'xx' else str(randint(current_year + 1, current_year + 5))
        
        # Generate CVV if not provided
        if cvv == 'xxx' or not cvv.isdigit():
            card_cvv = str(randint(1000, 9999) if cc_base.startswith('37') else randint(100, 999))
        else:
            card_cvv = cvv

        generated_cards.append(f"{cc_base}|{card_mes}|{card_ano}|{card_cvv}")

    return generated_cards



@Client.on_message(filters.command(["gen"], ["/", "."]))
async def gen(client: Client, message: Message):
    
    if not await is_user_registered(message.from_user.id):
        await message.reply_text("You are not registered. Use /register to register.")
        return

    if len(message.text.split()) < 2:
        return await message.reply("<b>Usage: /gen 456789|month|year|cvv (optional)</b>")

    input_data = message.text.split()[1].lower()
    parts = re.split(r'[/:;.,\s|]+', input_data)  # Split on | or other delimiters

    bin_code = parts[0]
    mes = parts[1] if len(parts) > 1 and parts[1].isdigit() else 'xx'  # Default to 'xx' if not provided
    ano = parts[2] if len(parts) > 2 and parts[2].isdigit() else 'xx'  # Default to 'xx' if not provided

    cvv = parts[3] if len(parts) > 3 and parts[3].isdigit() and parts[3] is not None else 'xxx'

    if ano != 'xx' and len(ano) == 2:
        ano = '20' + ano

    # Validate BIN length
    clean_bin_code = bin_code.replace('x', '')  # Strip placeholders for length validation
    if not (6 <= len(clean_bin_code) <= 16):
        await message.reply("<b>Invalid BIN format. Please provide a BIN with 6 to 16 digits.</b>", reply_to_message_id=message.id)
        return
    
    

    amount = int(message.text.split()[2]) if len(message.text.split()) > 2 and (message.text.split()[2]).isdigit() else 10

    try:
        req = requests.get(f"https://bins.antipublic.cc/bins/{clean_bin_code[:6]}").json()
        brand = req.get('brand') or '------'
        country_name = req.get('country') or '------'
        country_flag = req.get('flag') or '🏳️'
        bank = req.get('bank') or '------'
        level = req.get('level') or '------'
        typea = req.get('type') or '------'
    except Exception as e:
        return await message.reply(f"Bin Lookup Api Error: {e}", reply_to_message_id=message.id)

    rank = await get_user_rank(message.from_user.id)
    tiempoinicio = time.perf_counter()

    # Generate valid cards
    generated_cards = cc_gen(bin_code, amount, mes, ano, cvv)

    tiempofinal = time.perf_counter()

    try:
        # Respond with generated card details
        if amount > 50:
            file_path = f"{amount}✘_𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝_𝐁𝐲_{message.from_user.id}.txt"
            with open(file_path, "w") as file:
                file.write("\n".join(generated_cards))
            
            caption = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐂𝐂 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐀𝐩𝐢
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐢𝐧: <code>{bin_code[:6]}</code> || 𝐄𝐱𝐩𝐢𝐫𝐞: <code>{mes}|{ano}</code> || 𝐂𝐯𝐯: <code>{cvv}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐀𝐦𝐨𝐮𝐧𝐭: <code>{amount}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: {brand} - {typea} - {level}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐚𝐧𝐤: <code>{bank}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} [<code>{country_flag}</code>]
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">≹</a>]</b> 𝐓𝐢𝐦𝐞: <code>{tiempofinal - tiempoinicio:0.2f} seconds</code>
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> <b>[{rank}]</b>
"""
            await client.send_document(message.chat.id, file_path, caption=caption, reply_to_message_id=message.id)
            os.remove(file_path)
        else:
            card_list = '\n'.join([f"<code>{card}</code>" for card in generated_cards])
            text = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐂𝐂 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐀𝐩𝐢
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐢𝐧: <code>{bin_code[:6]}</code> || 𝐄𝐱𝐩𝐢𝐫𝐞: <code>{mes}|{ano}</code> || 𝐂𝐯𝐯: <code>{cvv}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐀𝐦𝐨𝐮𝐧𝐭: <code>{amount}</code>
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎐</a>]</b> 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞𝐝 𝐂𝐚𝐫𝐝𝐬:
- - - - - - - - - - - - - - - - - - 
{card_list}
- - - - - - - - - - - - - - - - - - 
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: {brand} - {typea} - {level}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐁𝐚𝐧𝐤: <code>{bank}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} [<code>{country_flag}</code>]
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">≹</a>]</b> 𝐓𝐢𝐦𝐞: <code>{tiempofinal - tiempoinicio:0.2f} seconds</code>
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> <b>[{rank}]</b>
"""
            await message.reply_text(f'{text}', reply_to_message_id=message.id, disable_web_page_preview=True)
    except pyrogram.errors.BadRequest as e:
        if "TOPIC_CLOSED" in str(e):
            await message.reply("Topic is closed. Please open it to use this command.", reply_to_message_id=message.id)
        else:
            await message.reply(f"An error occurred", reply_to_message_id=message.id)
