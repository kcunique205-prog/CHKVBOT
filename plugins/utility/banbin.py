import os
import aiohttp  # For making asynchronous HTTP requests
from pyrogram import Client, filters
from .db import OWNER_ID

file = 'bannedbin.txt'

# Ensure the bannedbin.txt file exists
if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write('')

async def ban_bin_direct(bin_number: str):
    with open(file, 'r') as f:
        banned_bins = f.read().splitlines()

    if bin_number not in banned_bins:
        with open(file, 'a') as f:
            f.write(f"{bin_number}\n")
        return f"BIN <code>{bin_number}</code> has been banned successfully."
    else:
        return f"BIN <code>{bin_number}</code> is already banned."

async def is_bin_banned(bin_number: str):
    with open(file, 'r') as f:
        banned_bins = f.read().splitlines()

    if bin_number in banned_bins:
        return f"{bin_number} bin is banned."
    else:
        url = f"hhttps://bins.antipublic.cc/bins/{bin_number}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()

                        if "prepaid" in data.get("level", "").lower():
                            return "All prepaid bins are banned."
            except aiohttp.ClientError as e:
                pass
            
@Client.on_message(filters.command("banbin", prefixes=["/", "."]))
async def ban_bin_handler(bot: Client, message):
    user_id = message.from_user.id
    if user_id!= OWNER_ID:
        await message.reply_text("Only the bot owner can use this command.", reply_to_message_id=message.id)
        return
    if len(message.text.split()) < 2:
        await message.reply_text("Please provide a BIN to ban.",quote=True)
        return

    input_value = message.text.split(" ", 1)[1].strip()
    bin_number, bin_type = extract_bin(input_value)

    if bin_type == "invalid":
        await message.reply_text("Invalid input. Please provide a valid BIN (6 digits) or a full credit card number (16 digits or more).",quote=True)
        return

    response = await ban_bin_direct(bin_number)
    await message.reply_text(response,quote=True)
def extract_bin(input_value):
    if len(input_value) >= 16 and input_value.isdigit():
        return input_value[:6], "cc"
    elif len(input_value) == 6 and input_value.isdigit():
        return input_value, "bin"
    else:
        # Invalid input
        return None, "invalid"
