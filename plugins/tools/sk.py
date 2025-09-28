import re
import time
import requests
import base64,stripe
from requests.auth import HTTPBasicAuth
from pyrogram import Client, filters
from plugins.utility.db import get_user_rank
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Awesome Product',
                        },
                        'unit_amount': 100,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://your-website.com/success',
            cancel_url='https://your-website.com/cancel',
        )
        return session.url
    except Exception as e:
        pass


async def get_stripe_data(checkout_url):
    try:
        url = checkout_url.split('#')[1]
        encoded_url = url.replace('%2B', '+').replace('%2F', '/')
        encoded_url += '=' * (len(encoded_url) % 4)
        decoded_bytes = base64.urlsafe_b64decode(encoded_url)
        decoded_url = decoded_bytes.decode('utf-8')
        key = 5
        binary_key = bin(key)[2:].zfill(8)
        plaintext = ""
        for i in range(len(decoded_url)):
            binary_char = bin(ord(decoded_url[i]))[2:].zfill(8)
            xor_result = ""
            for j in range(8):
                xor_result += str(int(binary_char[j]) ^ int(binary_key[j]))
            plaintext += chr(int(xor_result, 2))
        pk = plaintext.split('pk_live_')[1].split('"')[0]
        return pk
    except:
        pass


async def retrieve_balance(sk):
    bln = "https://api.stripe.com/v1/balance"
    auth = HTTPBasicAuth(sk, '')
    stripe.api_key = sk
    res = requests.get(bln, auth=auth)
    return res.json()

async def check_status(message, sk):
    first = message.from_user.first_name
    rank = await get_user_rank(message.from_user.id)
    tic = time.perf_counter()
    bal_dt = await retrieve_balance(sk)
    try:
        avl_bln = bal_dt['available'][0]['amount']
        pnd_bln = bal_dt['pending'][0]['amount']
        crn = bal_dt['available'][0]['currency']
    except KeyError:
        txtx = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐒𝐭𝐫𝐢𝐩𝐞 𝐊𝐞𝐲 𝐋𝐨𝐨𝐤𝐮𝐩
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐒𝐤: <code>{sk}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: 𝐒𝐤 𝐊𝐞𝐲 𝐑𝐞𝐯𝐨𝐤𝐞𝐝 ❌
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{first}</a> <b>[{rank}]</b>
<b>[<a href="https://t.me/Instuff_bot">⌤</a>]</b> 𝐃𝐞𝐯 𝐛𝐲: <code>@XAY4N</code> 🍀
"""
        return txtx
    
    resp = "https://api.stripe.com/v1/account"
    auth = HTTPBasicAuth(sk, '')
    res = requests.get(resp, auth=auth)
    try:
        acc_id = res.json()['id']
        pay_meth = res.json()['capabilities']['card_payments']
    except KeyError:
        txtx = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐒𝐭𝐫𝐢𝐩𝐞 𝐊𝐞𝐲 𝐋𝐨𝐨𝐤𝐮𝐩
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐒𝐤: <code>{sk}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Your account cannot currently make live charges.
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{first}</a> <b>[{rank}]</b>
<b>[<a href="https://t.me/Instuff_bot">⌤</a>]</b> 𝐃𝐞𝐯 𝐛𝐲: <code>@XAY4N</code> 🍀
"""
        return txtx
    if "inactive" in pay_meth:
        texxt = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐒𝐭𝐫𝐢𝐩𝐞 𝐊𝐞𝐲 𝐋𝐨𝐨𝐤𝐮𝐩
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐒𝐤: <code>{sk}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Your account cannot currently make live charges.
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{first}</a> <b>[{rank}]</b>
<b>[<a href="https://t.me/Instuff_bot">⌤</a>]</b> 𝐃𝐞𝐯 𝐛𝐲: <code>@XAY4N</code> 🍀
"""
        return texxt

    payments = res.json()['charges_enabled']
    url = res.json()['business_profile']['url']
    checkout_url = create_checkout_session()
    pk = await get_stripe_data(checkout_url)
    pk1 = 'pk_live_' + str(pk)

    chk = "https://api.stripe.com/v1/tokens"
    data = 'card[number]=5581585612888772&card[exp_month]=12&card[exp_year]=2029&card[cvc]=354'
    auth = HTTPBasicAuth(sk, '')
    rep = requests.post(chk, data=data, auth=auth)
    repp = rep.text

    if 'rate_limit' in repp:
        r_text = '𝐑𝐚𝐭𝐞 𝐋𝐢𝐦𝐢𝐭 ✅'
    elif 'tok_' in repp:
        r_text = '𝐋𝐢𝐯𝐞 𝐊𝐞𝐲 ✅'
    elif 'Invalid API Key provided' in repp:
        r_text = "𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐀𝐏𝐈 𝐊𝐞𝐲 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝 ❌"
    elif 'You did not provide an API key.' in repp:
        r_text = "𝐍𝐨 𝐒𝐤 𝐤𝐞𝐲 𝐩𝐫𝐨𝐯𝐢𝐝𝐞𝐝 ❌"
    elif 'testmode_charges_only' in repp or 'test_mode_live_card' in repp:
        r_text = "𝐓𝐞𝐬𝐭 𝐌𝐨𝐝𝐞 𝐜𝐡𝐚𝐫𝐠𝐞 𝐨𝐧𝐥𝐲 ❌"
    elif 'api_key_expired' in repp:
        r_text = "𝐀𝐏𝐈 𝐤𝐞𝐲 𝐞𝐱𝐩𝐢𝐫𝐞𝐝 ❌"
    elif 'Sending credit' in repp:
        r_text = "𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧 𝐨𝐟𝐟 ⚠️"
    else:
        r_text = "𝐒𝐤 𝐃𝐞𝐚𝐝 ❌"

    toc = time.perf_counter() 
    elapsed_time = f"{toc - tic:.2f}"
    txtxtx = f"""
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐒𝐭𝐫𝐢𝐩𝐞 𝐊𝐞𝐲 𝐋𝐨𝐨𝐤𝐮𝐩
━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐒𝐤: <code>{sk}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐏𝐤: <code>{pk1}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>{r_text}</code>
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈𝐃: <code>{acc_id}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐔𝐑𝐋: <code>{url}</code>
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐚𝐫𝐝 𝐏𝐚𝐲𝐦𝐞𝐧𝐭𝐬: {pay_meth}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐡𝐚𝐫𝐠𝐞 𝐄𝐧𝐚𝐛𝐥𝐞𝐝: {payments}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐂𝐮𝐫𝐫𝐞𝐧𝐜𝐲: {crn}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐁𝐚𝐥𝐚𝐧𝐜𝐞: {avl_bln}
<b>[<a href="https://t.me/Instuff_bot">⌬</a>]</b> 𝐏𝐞𝐧𝐝𝐢𝐧𝐠 𝐁𝐚𝐥𝐚𝐧𝐜𝐞: {pnd_bln}
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌥</a>]</b> 𝐓𝐢𝐦𝐞: <code>{elapsed_time}</code> 𝐒𝐞𝐜.
<b>[<a href="https://t.me/Instuff_bot">⎇</a>]</b> 𝐑𝐞𝐪 𝐁𝐲: <a href="tg://user?id={message.from_user.id}">{first}</a> <b>[{rank}]</b>
━━━━━━━━━━━━━━━━━
<b>[<a href="https://t.me/Instuff_bot">⌤</a>]</b> 𝐃𝐞𝐯 𝐛𝐲: <code>@XAY4N</code> 🍀
"""

    return txtxtx

@Client.on_message(filters.command("sk", prefixes=["/", "."]))
async def sk1(client, message):
    if len(message.text.split()) >= 2:
        sk = message.text.split()[1]
    elif message.reply_to_message and message.reply_to_message.text:
        ttt = message.reply_to_message.text
        skm = re.search(r"sk_live_[a-zA-Z0-9]+", ttt)
        sk = skm.group(0)
    else:
        await message.reply("<b>NO SK KEY PROVIDED</b>\n<b>USE /sk [ YOUR SK KEY ]</b>", quote=True)
        return
    rest_in_peace = await check_status(message, sk)

    await message.reply(rest_in_peace, quote=True, disable_web_page_preview=True)
