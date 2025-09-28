from pyrogram import Client, filters
import json

SHOPIFY_DATA_FILE = "shopify_data.json"

# Load Shopify gateway data from the JSON file
def load_shopify_data():
    try:
        with open(SHOPIFY_DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"commands": []}

# Save Shopify gateway data to the JSON file
def save_shopify_data(data):
    with open(SHOPIFY_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add new Shopify gateway
@Client.on_message(filters.command("addsh", prefixes=["/", "."]))
async def add_shopify_gateway(client, message):
    try:
        args = message.text.split(" ")[1].split("|")
        if len(args) != 4:
            await message.reply_text("Invalid format. Use `/addshopify <name>|<command>|<type>|<url>`", reply_to_message_id=message.id)
            return

        name, command, gateway_type, url = args

        data = load_shopify_data()

        data["commands"].append({
            "name": name,
            "command": command,
            "type": gateway_type,
            "url": url,
            "status": "on"  # New gateways start as 'on'
        })

        # Save updated data
        save_shopify_data(data)

        await message.reply_text(f"New gateway '{name}' added successfully!", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}", reply_to_message_id=message.id)

@Client.on_message(filters.command("usho", prefixes=["/", "."]))
async def update_shopify_status(client, message):
    try:
        args = message.text.split(" ")[1].split("|")
        if len(args) != 2:
            await message.reply_text("Invalid format. Use `/usho <command>|<status>`", reply_to_message_id=message.id)
            return

        command, status = args

        if status not in ["on", "off"]:
            await message.reply_text("Invalid status. Use 'on' or 'off'.", reply_to_message_id=message.id)
            return

        # Load existing data
        data = load_shopify_data()

        # Find and update the command's status
        for gateway in data["commands"]:
            if gateway["command"] == command:
                gateway["status"] = status
                save_shopify_data(data)
                await message.reply_text(f"Gateway '{command}' status updated to {status}.", reply_to_message_id=message.id)
                return

        await message.reply_text(f"Gateway '{command}' not found.", reply_to_message_id=message.id)
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}", reply_to_message_id=message.id)
