from pyrogram import Client, filters
from googletrans import Translator
from googletrans import LANGUAGES
from plugins.utility.db import get_user_rank, is_user_registered  # Ensure correct path
translator = Translator()

@Client.on_message(filters.command(["tr"], prefixes=["/", "."]))
async def translate(bot, message):
    if not await is_user_registered(message.from_user.id):
        await message.reply_text("You are not registered. Use /register to register.")
        return
    try:
        user_id = message.from_user.id
        inp = message.text[len('/tr '):]

        rd3_lang = inp[:2].lower()
        if rd3_lang not in LANGUAGES:
            return await message.reply_text('Invalid language code. Use /langcode to see available language codes.')

        if message.reply_to_message:
            source_text = message.reply_to_message.text
        else:
            source_text = inp[3:]
        
        # Fetch rank
        rank = await get_user_rank(user_id)

        # Perform translation
        translation = translator.translate(source_text, dest=rd3_lang)
        translated_text = translation.text

        # Format the message
        msg = f'''
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐨𝐫 𝐀𝐩𝐢
━━━━━━━━━━━━━━
𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐞𝐝 𝐋𝐚𝐧𝐠: <code>{rd3_lang.upper()}</code>
<u>𝐓𝐫𝐚𝐧𝐬𝐥𝐚𝐭𝐞𝐝 𝐓𝐞𝐱𝐭:</u>
{translated_text}
━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> <b>[{rank}]</b>
'''
        await message.reply_text(msg, reply_to_message_id=message.id, disable_web_page_preview=True)

    except Exception as e:
        # Catch any kind of error and respond appropriately
        await message.reply_text(
            'Invalid Format. Example: /tr (language code) text to translate\n'
            'To see available language codes, type /langcode'
        , reply_to_message_id=message.id)


@Client.on_message(filters.command(["langcode"], prefixes=["/", "."]))
async def language_codes(bot, message):
    if not await is_user_registered(message.from_user.id):
        await message.reply_text("You are not registered. Use /register to register.")
        return
    try:
        unique_languages = {}
        for k, v in LANGUAGES.items():
            if v not in unique_languages.values():
                unique_languages[k] = v

        # Format the language codes line by line
        language_codes = '\n'.join([f'{k}: {v}' for k, v in unique_languages.items()])

        # Send the message with the list of unique language codes
        await message.reply(f"𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐥𝐚𝐧𝐠𝐮𝐚𝐠𝐞 𝐜𝐨𝐝𝐞𝐬:\n{language_codes}", reply_to_message_id=message.id)
    
    except Exception as e:
        await message.reply(f"An error occurred while fetching language codes: {e}", reply_to_message_id=message.id)
