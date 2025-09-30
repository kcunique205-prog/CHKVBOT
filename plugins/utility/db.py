import random
import string
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta
import asyncio
import certifi

# ✅ Use direct connection format instead of SRV
MONGO_URI = (
    "mongodb://YtInayatGaming:InayatGaming_Mongodb@"
    "ytinayatgaming-shard-00-00.lulqg.mongodb.net:27017,"
    "ytinayatgaming-shard-00-01.lulqg.mongodb.net:27017,"
    "ytinayatgaming-shard-00-02.lulqg.mongodb.net:27017/"
    "?ssl=true&replicaSet=atlas-dvg04r-shard-0"
    "&authSource=admin&retryWrites=true&w=majority&appName=YtInayatGaming"
)

# ✅ Add certifi so TLS works properly
client = AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where())

db = client['telegram_bot']

# Your collection definitions...
users_collection = db['users']
authorized_users_collection = db['authorized_users']
groups_collection = db['authorized_groups']
keys_collection = db['keys']
skpk_keys_collection = db['skpk_keys']
gateways_collection = db['gateways']

OWNER_ID = 5882652117  # Owner's ID
DEFAULT_CREDITS = 0  # Default credits for new users

async def add_or_update_skpk(sk_live, pk_live):

    
    # Delete the existing document with the same SK
    delete_result = await skpk_keys_collection.delete_many({})
    
    result = await skpk_keys_collection.insert_one({"sk": sk_live, "pk": pk_live})
    new_doc = await skpk_keys_collection.find_one({"sk": sk_live})
    
    return "SK and PK replaced successfully."


# Method to fetch SK/PK
async def get_skpk():

    skpk = await skpk_keys_collection.find_one({})
    
    if skpk:
        return skpk["sk"], skpk["pk"]
    else:
        return "SK not found." , "PK not found."
async def ensure_owner_is_authorized():
    if not await authorized_users_collection.find_one({"id": OWNER_ID}):
        await authorized_users_collection.insert_one({
            "id": OWNER_ID,
            "role": "owner",
            "credits": 1000,
            "expiry": None,
            "rank": "dev"
        })


async def register_user(user_id, username, first_name, last_name, credits=DEFAULT_CREDITS):
    if not await users_collection.find_one({"user_id": user_id}):
        user_data = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "credits": credits,
            "role": "free",
            "rank": "Free user",
            "registered_at": datetime.now()
        }
        await users_collection.insert_one(user_data)
        return True
    return False

async def add_owner(user_id):
    """
    Adds a user as an owner.
    """
    # Check if the user is already an owner
    existing_owner = await authorized_users_collection.find_one({"id": user_id, "role": "owner"})
    if existing_owner:
        return f"User {user_id} is already an owner."
    
    # Update or insert the user as an owner
    await authorized_users_collection.update_one(
        {"id": user_id},
        {"$set": {"role": "owner", "rank": "Owner", "credits": DEFAULT_CREDITS, "expiry": None}},
        upsert=True
    )
    return f"User {user_id} has been added as an owner."

async def remove_owner(user_id):
    """
    Removes a user from the owner role.
    """
    # Prevent the removal of the primary OWNER_ID
    if user_id == OWNER_ID:
        return "You cannot remove the primary owner."
    
    result = await authorized_users_collection.update_one(
        {"id": user_id, "role": "owner"},
        {"$set": {"role": "free", "rank": "Free user"}}
    )
    
    if result.matched_count == 0:
        return f"User {user_id} is not an owner."
    
    return f"User {user_id} has been removed from the owner role."
async def is_user_owner(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    if user:
        return user.get("role") == "owner"
    return False
async def is_group_authorized(group_id):
    """
    Check if a group is authorized.
    
    Args:
        group_id: The ID of the group to check.
        
    Returns:
        bool: True if the group is authorized, False otherwise.
    """
    group = await groups_collection.find_one({"id": group_id})
    return bool(group)
async def get_all_user_ids():
    return [user['user_id'] for user in await users_collection.find({}).to_list(length=None)]

async def get_user_expiry(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    return user.get("expiry") if user and user.get("expiry") else None

async def is_user_registered(user_id):
    return bool(await users_collection.find_one({"user_id": user_id}))

async def give_credits(user_id, credits):
    """
    Adds a specified number of credits to a user's account.
    """
    # Retrieve the user from the authorized_users_collection
    user = await authorized_users_collection.find_one({"id": user_id})
    
    if not user:
        return f"User {user_id} not found."

    # Retrieve the user's current credits and ensure it is treated as an integer
    current_credits = user.get("credits", 0)

    # Calculate the new credit total
    new_credit_count = current_credits + credits

    # Update the user's credit count in the database
    await authorized_users_collection.update_one(
        {"id": user_id}, 
        {"$set": {"credits": new_credit_count}}
    )

    # Return a message with the updated credit balance
    return f"Gave {credits} credits to user {user_id}. They now have {new_credit_count} credits."


async def update_credits(user_id, credit_change):
    """
    Update user's credits by adding/subtracting the specified credit change.
    `credit_change` can be a positive or negative integer.
    """
    user = await authorized_users_collection.find_one({"id": user_id})
    if not user:
        return f"User {user_id} not found."
    
    current_credits = user.get("credits", 0)
    new_credits = current_credits + credit_change  # Adjust the credits by the provided change

    # Ensure that the credits do not go below zero
    if new_credits < 0:
        new_credits = 0

    await authorized_users_collection.update_one(
        {"id": user_id}, 
        {"$set": {"credits": new_credits}}
    )
    
    return new_credits

async def get_user_credits(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    return user.get("credits", 0) if user else 0

async def show_credits(user_id):
    if not await is_user_authorized(user_id):
        return "You are not authorized."

    user = await authorized_users_collection.find_one({"id": user_id})
    return f"You have {user.get('credits', 0)} credits remaining. Your rank is {user.get('rank', 'free')}."

async def is_user_admin(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    return user and user.get("role") in ["admin", "owner"]

async def generate_key(duration):
    key_format = f"B3XAYAN-{generate_random_string(5)}-{generate_random_string(3)}"
    expiry_time = parse_duration(duration)

    if not expiry_time:
        return "Invalid duration format."

    await keys_collection.insert_one({"key": key_format, "expiry": expiry_time})
    return key_format, expiry_time

def parse_duration(duration):
    try:
        if duration.endswith('d'):
            return datetime.now() + timedelta(days=int(duration[:-1]))
        elif duration.endswith('h'):
            return datetime.now() + timedelta(hours=int(duration[:-1]))
        elif duration.endswith('m') and not duration.endswith('mi'):
            return datetime.now() + timedelta(minutes=int(duration[:-1]))
        elif duration.endswith('y'):
            return datetime.now() + timedelta(days=int(duration[:-1]) * 365)
        elif duration.endswith('mi'):
            return datetime.now() + timedelta(minutes=int(duration[:-2]))
    except ValueError:
        return None

async def promote_user(user_id, duration, credits=None):
    expiry_time = parse_duration(duration)
    if not expiry_time:
        return "Invalid duration format."

    await authorized_users_collection.update_one(
        {"id": user_id},
        {"$set": {
            "role": "authorized",
            "rank": "VIP",
            "expiry": expiry_time,
            "credits": credits if credits else DEFAULT_CREDITS
        }},
        upsert=True
    )

    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"role": "authorized", "rank": "VIP"}}
    )
    return f"User {user_id} is now authorized for {duration}."

async def demote_user(user_id):
    await authorized_users_collection.delete_one({"id": user_id})
    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"role": "free", "rank": "Free user"}}
    )
    return f"User {user_id} has been demoted to Free user."

async def claim_key(user_id, key):
    key_doc = await keys_collection.find_one({"key": key})
    if not key_doc:
        return "Key not found."

    if key_doc["expiry"] < datetime.now():
        return "Key has expired."

    authorized_user = await authorized_users_collection.find_one({"id": user_id})
    if not authorized_user:
        await authorized_users_collection.insert_one({
            "id": user_id,
            "expiry": key_doc["expiry"],
            "credits": DEFAULT_CREDITS,
            "role": "authorized",
            "rank": "VIP"
        })

    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"role": "authorized", "rank": "VIP"}}
    )

    await keys_collection.delete_one({"key": key})
    return "Key successfully claimed. You are now authorized."

async def unauth_user(user_id):
    result = await authorized_users_collection.delete_one({"id": user_id})
    if result.deleted_count == 0:
        return f"User {user_id} is not authorized or already removed."

    await users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"role": "free", "rank": "Free user"}}
    )

    return f"User {user_id} has been successfully unauthorized and is now a Free User."

async def clean_expired_authorizations_and_keys():
    now = datetime.now()

    expired_users = await authorized_users_collection.find({"expiry": {"$lt": now}}).to_list(length=None)
    for user in expired_users:
        await unauth_user(user["id"])

    await keys_collection.delete_many({"expiry": {"$lt": now}})

async def is_user_authorized(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    if user:
        if user.get("expiry") and user["expiry"] < datetime.now():
            await unauth_user(user_id)
            return False
        return True
    return False

async def get_user_rank(user_id):
    user = await authorized_users_collection.find_one({"id": user_id})
    if not user:
        return "Free user"
    if user.get("role") == "owner" or user == OWNER_ID:
        return "Dev"
    elif user.get("role") in ["authorized"]:
        return "VIP"
    return "Free user"

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

async def assign_roles_to_all():
    all_users = await authorized_users_collection.find().to_list(length=None)
    for user in all_users:
        role = "owner" if user["id"] == OWNER_ID else ("authorized" if await is_user_authorized(user["id"]) else "free")
        rank = "Dev" if role == "owner" else ("VIP" if role == "authorized" else "Free user")

        await authorized_users_collection.update_one(
            {"id": user["id"]},
            {"$set": {"role": role, "rank": rank}}
        )

        await users_collection.update_one(
            {"user_id": user["id"]},
            {"$set": {"role": role, "rank": rank}}
        )

    all_users_in_db = await users_collection.find().to_list(length=None)
    for user in all_users_in_db:
        if not await authorized_users_collection.find_one({"id": user["user_id"]}):
            await users_collection.update_one(
                {"user_id": user["user_id"]},
                {"$set": {"role": "free", "rank": "Free user"}}
            )
# Gateway management functions
async def add_gateway(category, name, command, status="on"):
    """Add a new gateway to the database or update an existing one"""
    result = await gateways_collection.update_one(
        {"category": category, "command": command},
        {"$set": {
            "category": category,
            "name": name,
            "command": command,
            "status": status,
            "updated_at": datetime.now()
        }},
        upsert=True
    )
    return result.modified_count > 0 or result.upserted_id is not None

async def get_gateways_by_category(category):
    """Get all gateways for a specific category"""
    cursor = gateways_collection.find({"category": category})
    return await cursor.to_list(length=None)

async def get_all_gateways():
    """Get all gateways from the database"""
    cursor = gateways_collection.find({})
    return await cursor.to_list(length=None)

async def get_gateway_categories():
    """Get all unique gateway categories"""
    categories = await gateways_collection.distinct("category")
    return categories

async def update_gateway_status(command, status):
    """Update the status of a gateway"""
    result = await gateways_collection.update_one(
        {"command": command},
        {"$set": {"status": status, "updated_at": datetime.now()}}
    )
    return result.modified_count > 0

async def delete_gateway(command):
    """Delete a gateway from the database"""
    result = await gateways_collection.delete_one({"command": command})
    return result.deleted_count > 0

async def get_gateway_count():
    """Get the total number of gateways in the database"""
    return await gateways_collection.count_documents({})

async def initialize_default_gateways():
    """Initialize the database with default gateways if empty"""
    count = await get_gateway_count()
    if count == 0:
        # Default gateway data from the static dictionary
        default_gateways = {
            "auth": [
                ("Braintree Auth", "/chk"),
                ("Braintree Auth 2", "/b3"),
                ("Braintree Auth 3", "/cc"),
                ("Braintree Auth 4 (AVS)", "/auth"),
                ("Braintree + Moneris Auth", "/btm"),
                ("Moneris Auth", "/mo"),
                ("Payflow Auth", "/lt"),
                ("Stripe Auth", "/sa"),
                ("Stripe Auth 2", "/sa2"),
            ],
            "charge": [
                ("Braintree Charge €1" , "/bc"),
                ("Braintree Charge $5", "/bl"),
                ("Braintree Charge $275", "/bt"),
                ("Braintree CCN Charge $16.20", "/bcn"),
                ("Vantiv Charge $10", "/vc"),
                ("Payflow Charge $14.74", "/pf"),
                ("Payflow Charge $19.67", "/pt"),
                ("Stripe Charge $1", "/sc"),
                ("Stripe Charge $1.99", "/st"),
                ("Stripe Charge £5.00", "/sx"),
                ("Stripe Charge $5.50", "/sp"),
                ("SK Based $1", "/sv"),
                ("Cybersource Charge $1.53", "/scy"),
                ("PayPal Commerce $5", "/pp"),
                ("Auth.net Charge $4.99", "/atn"),
                ("Shopify Charge $1", "/sh"),
                ("Shopify Charge ₹100", "/shr"),
                ("USAePay Charge $22.50", "/ue"),
                ("USAePay Charge $33", "/ue2"),
            ],
            "mass": [
                ("Mass Stripe Charge $2", "/mst"),
                ("Mass Stripe Auth", "/mau"),
                ("Mass Sk based $1", "/msv"),
                ("Mass Stripe Charge $1", "/svtxt"),
                ("Mass Braintree Auth", "/mb3"),
            ],
            "special": [
                ("Braintree VBV Lookup", "/vbv"),
            ]
        }
        
        # Add all default gateways to the database
        for category, gateways in default_gateways.items():
            for name, command in gateways:
                cmd = command[1:]  # Remove the '/' prefix
                status = get_command_status(cmd)
                await add_gateway(category, name, command, status)

async def init():
    await assign_roles_to_all()
    await clean_expired_authorizations_and_keys()
    await ensure_owner_is_authorized()
    await initialize_default_gateways()

    print("MongoDB connection established and initialization complete.")










