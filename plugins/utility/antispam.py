import json
import os
import time
import requests


# Constants
SPAM_THRESHOLD_DEFAULT = 35  # 50 seconds wait for non-authorized users
SPAM_THRESHOLD_AUTHORIZED = 20  # 25 seconds wait for authorized users
SPAM_FILE = 'antispam_data.json'  # File to store spam data
SCRIPT_THRESHOLD = 5  # Number of repeated actions to flag as script user
LOG_FILE = 'script_users.log'  # Log file for script users
BOT_OWNER_ID = 6515961910  # Owner ID to receive logs

# Load or create spam data JSON file
def load_spam_data():
    try:
        with open(SPAM_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save spam data to JSON file
def save_spam_data(spam_data):
    with open(SPAM_FILE, 'w') as file:
        json.dump(spam_data, file, indent=4)

# Check if a user is spamming
def is_spamming(user_id, is_authorized):
    spam_data = load_spam_data()
    current_time = time.time()
    
    spam_threshold = SPAM_THRESHOLD_AUTHORIZED if is_authorized else SPAM_THRESHOLD_DEFAULT

    if str(user_id) in spam_data:
        last_action_time = spam_data[str(user_id)]['last_action_time']
        time_difference = current_time - last_action_time

        if time_difference < spam_threshold:
            remaining_time = spam_threshold - time_difference
            return True, f"ANTI_SPAM: Wait for {int(remaining_time)} seconds."

        spam_data[str(user_id)]['last_action_time'] = current_time
    else:
        spam_data[str(user_id)] = {'last_action_time': current_time, 'commands': []}
    
    save_spam_data(spam_data)
    return False, None

# Function to log script users
def log_script_user(user_id):
    with open(LOG_FILE, 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Script User Detected: {user_id}\n")
        
        response = requests.get(f"https://api.telegram.org/bot7908600153:AAEYDu3BwFkT-1_SyLr5Zm9OeDOAsbui_Ic/sendMessage", params={
            'chat_id': BOT_OWNER_ID,
            'text': f"🚨 Script User Detected: {user_id}\n",
            'parse_mode': 'HTML',
        })
        if response.status_code != 200:
            file.write(f"Failed to notify the bot owner about the script user.\n")
        
    

# Function to clear spam data for a user
def clear_user_spam(user_id):
    spam_data = load_spam_data()
    if str(user_id) in spam_data:
        del spam_data[str(user_id)]
        save_spam_data(spam_data)

# Function to periodically clean old spam data
def clean_spam_data():
    spam_data = load_spam_data()
    current_time = time.time()
    spam_data = {user_id: data for user_id, data in spam_data.items() if current_time - data['last_action_time'] < 3600}
    save_spam_data(spam_data)
