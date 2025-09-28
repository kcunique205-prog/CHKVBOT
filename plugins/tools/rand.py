import requests 
from pyrogram import Client, filters
from pyrogram.types import Message
import iso3166,time,random,string
from plugins.utility.db import get_user_rank

@Client.on_message(filters.command(["rand", "fake", "rnd"], prefixes=['.', '/', '!', '?'], case_sensitive=False) & filters.text)
async def cmds(client, message):
    try:
        country = message.text.split()[1]
    except IndexError:
        await message.reply("<b>Error, Example: /rand  <code>MX - CA - ES - US - FR - UK</code></b>",reply_to_message_id=message.id)
        return
         
    if country.upper() not in iso3166.countries_by_alpha2:
        await message.reply(f"<b>The country code '{country}' is not valid. Enter a valid country code, example: /rand us</b>",reply_to_message_id=message.id)
        return
    
    tiempoinicio = time.perf_counter()
    api = requests.get(f"https://randomuser.me/api/?nat={country}&inc=name,location,phone&exc=location.city").json()

    nombre = api["results"][0]["name"]["first"]
    last = api["results"][0]["name"]["last"]
    loca = api["results"][0]["location"]["street"]["name"]
    nm = api["results"][0]["location"]["street"]["number"]
    city = api["results"][0]["location"]["city"]
    state = api["results"][0]["location"]["state"]
    country = api["results"][0]["location"]["country"]
    postcode = api["results"][0]["location"]["postcode"]
    phone = api["results"][0]["phone"]

    randstr = ''.join(random.choices(string.ascii_lowercase + string.digits, k=(random.randint(6, 15))))
    email = randstr + "@teleworm.us"
    email_link = f"https://www.fakemailgenerator.com/#/teleworm.us/{randstr}/"
    tiempofinal = time.perf_counter()

    ID = message.from_user.id
    first = message.from_user.first_name

    rank = await get_user_rank(ID)
      
    await message.reply(f"""             
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐅𝐚𝐤𝐞 𝐀𝐝𝐝𝐫𝐞𝐬𝐬 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐍𝐚𝐦𝐞: <code>{nombre} {last}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐒𝐭𝐫𝐞𝐞𝐭: <code>{loca} {nm}</code>                               
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐂𝐢𝐭𝐲: <code>{city}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐒𝐭𝐚𝐭𝐞: <code>{state}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐏𝐨𝐬𝐭𝐚𝐥 𝐂𝐨𝐝𝐞: <code>{postcode}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐏𝐡𝐨𝐧𝐞 𝐍𝐨.: <code>{phone}</code>
<b>[<a href="https://t.me/Instuff_bot">↯</a>]</b> 𝐄𝐦𝐚𝐢𝐥: <code>{email}</code> [<a href="{email_link}">Inbox</a>]
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">≹</a>]</b> 𝐓𝐢𝐦𝐞: <code>{tiempofinal - tiempoinicio:0.2f} seconds</code>
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={ID}">{first}</a> <b>[{rank}]</b>                   
""", disable_web_page_preview=True, reply_to_message_id=message.id)