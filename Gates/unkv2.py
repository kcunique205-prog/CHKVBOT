import requests,random,string
from datetime import datetime
import pytz

r = requests.Session()
def getstr(data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None
    
def random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=(random.randint(6, 10))))
    domain = random.choice(['gmail', 'yahoo', 'hotmail', 'outlook', 'icloud' , 'aol', 'live'])
    extension = 'com'

    return f'{random_string}@{domain}.{extension}'

def random_username():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=(random.randint(6, 10))))
    return random_string

def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
web = generate_boundary()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',}

response = r.get('https://www.uksafetystore.com/no-smoking-or-vaping-on-these-premises-sign.html', headers=headers)

form_key = getstr(response.text, 'form_key" type="hidden" value="', '"')
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': f'multipart/form-data; boundary=----{web}',
    # 'cookie': 'PHPSESSID=2126d6594qp8rc5pa926b96rk0; _uetsid=65e602a08fa411efbaf14d896e894e25; _uetvid=65e651508fa411efa9493db94cd27f36; _clck=16ghdlo%7C2%7Cfq7%7C0%7C1755; _ga=GA1.1.537020715.1729512172; form_key=TdAdfzt2IRtOE6Gq; _clsk=1ws52py%7C1729512173137%7C1%7C1%7Cd.clarity.ms%2Fcollect; mst_related_session_id=17295121732687548; ps_rvm_I2kx=%7B%22pssid%22%3A%22qx19mjnP9qxJa18T-1729512173302%22%7D; mst-cache-warmer-track=1729512168932; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; form_key=TdAdfzt2IRtOE6Gq; recently_viewed_product={}; product_data_storage={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; private_content_version=70715ea52d71de77ad0d64b49406b890; section_data_ids={}; _gcl_au=1.1.293014540.1729512178; _ga_W769D9LF8M=GS1.1.1729512171.1.0.1729512177.54.0.0',
    'origin': 'https://www.uksafetystore.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.uksafetystore.com/no-smoking-or-vaping-on-these-premises-sign.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = f"""
------{web}
Content-Disposition: form-data; name="product"

16147
------{web}
Content-Disposition: form-data; name="selected_configurable_option"

16156
------{web}
Content-Disposition: form-data; name="related_product"


------{web}
Content-Disposition: form-data; name="item"

16147
------{web}
Content-Disposition: form-data; name="form_key"

{form_key}
------{web}
Content-Disposition: form-data; name="super_attribute[1242]"

185
------{web}
Content-Disposition: form-data; name="super_attribute[1241]"

195
------{web}
Content-Disposition: form-data; name="qty"

1
------{web}--"""

response = r.post(
    'https://www.uksafetystore.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cudWtzYWZldHlzdG9yZS5jb20vbm8tc21va2luZy1vci12YXBpbmctb24tdGhlc2UtcHJlbWlzZXMtc2lnbi5odG1s/product/16147/',
    headers=headers,
    data = data,
)
print(response.text)
# enity_id = getstr(response.text, '"entity_id":"', '"').strip()
# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json',
#     # 'cookie': 'PHPSESSID=2126d6594qp8rc5pa926b96rk0; _clck=16ghdlo%7C2%7Cfq7%7C0%7C1755; _ga=GA1.1.537020715.1729512172; form_key=TdAdfzt2IRtOE6Gq; mst_related_session_id=17295121732687548; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; form_key=TdAdfzt2IRtOE6Gq; recently_viewed_product={}; product_data_storage={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; _gcl_au=1.1.293014540.1729512178; mst-cache-warmer-track=1729512554616; _uetsid=65e602a08fa411efbaf14d896e894e25; _uetvid=65e651508fa411efa9493db94cd27f36; ps_rvm_I2kx=%7B%22pssid%22%3A%22qx19mjnP9qxJa18T-1729512561476%22%2C%22last-visit%22%3A%221729512555538%22%7D; _clsk=1ws52py%7C1729512562118%7C3%7C1%7Cd.clarity.ms%2Fcollect; private_content_version=74a9df928d240d5505b7ccdf3cbc9221; section_data_ids={%22cart%22:1729512217%2C%22directory-data%22:1729512217%2C%22messages%22:1729513276}; _ga_W769D9LF8M=GS1.1.1729512171.1.1.1729513332.60.0.0',
#     'origin': 'https://www.uksafetystore.com',
#     'pragma': 'no-cache',
#     'priority': 'u=1, i',
#     'referer': 'https://www.uksafetystore.com/checkout/',
#     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }

# json_data = {
#     'addressInformation': {
#         'shipping_address': {
#             'countryId': 'GB',
#             'region': 'Richmond',
#             'street': [
#                 'Richmond',
#                 '',
#             ],
#             'company': '',
#             'telephone': '0442658789',
#             'postcode': 'TW91JL',
#             'city': 'Richmond',
#             'firstname': 'Albedo',
#             'lastname': 'Jones',
#         },
#         'billing_address': {
#             'countryId': 'GB',
#             'postcode': None,
#             'saveInAddressBook': None,
#         },
#         'shipping_method_code': 'amstrates11',
#         'shipping_carrier_code': 'amstrates',
#         'extension_attributes': {},
#     },
# }

# response = r.post(
#     f'https://www.uksafetystore.com/rest/default/V1/guest-carts/{enity_id}/shipping-information',
#     headers=headers,
#     json=json_data,
# )
# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json',
#     # 'cookie': 'PHPSESSID=2126d6594qp8rc5pa926b96rk0; _clck=16ghdlo%7C2%7Cfq7%7C0%7C1755; _ga=GA1.1.537020715.1729512172; form_key=TdAdfzt2IRtOE6Gq; mst_related_session_id=17295121732687548; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-messages=; form_key=TdAdfzt2IRtOE6Gq; recently_viewed_product={}; product_data_storage={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; _gcl_au=1.1.293014540.1729512178; mst-cache-warmer-track=1729512554616; _uetsid=65e602a08fa411efbaf14d896e894e25; _uetvid=65e651508fa411efa9493db94cd27f36; ps_rvm_I2kx=%7B%22pssid%22%3A%22qx19mjnP9qxJa18T-1729512561476%22%2C%22last-visit%22%3A%221729512555538%22%7D; _clsk=1ws52py%7C1729512562118%7C3%7C1%7Cd.clarity.ms%2Fcollect; private_content_version=74a9df928d240d5505b7ccdf3cbc9221; section_data_ids={%22cart%22:1729512217%2C%22directory-data%22:1729512217%2C%22messages%22:1729513276}; _ga_W769D9LF8M=GS1.1.1729512171.1.1.1729513332.60.0.0',
#     'origin': 'https://www.uksafetystore.com',
#     'pragma': 'no-cache',
#     'priority': 'u=1, i',
#     'referer': 'https://www.uksafetystore.com/checkout/',
#     'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }

# json_data = {
#     'addressInformation': {
#         'address': {
#             'countryId': 'GB',
#             'region': 'Richmond',
#             'postcode': 'TW91JL',
#             'city': 'Richmond',
#             'extension_attributes': {
#                 'advanced_conditions': {
#                     'payment_method': 'sagepaysuitepi',
#                     'city': 'Richmond',
#                     'shipping_address_line': [
#                         'Richmond',
#                         '',
#                     ],
#                     'billing_address_country': 'GB',
#                     'currency': 'GBP',
#                 },
#             },
#         },
#         'shipping_method_code': 'amstrates11',
#         'shipping_carrier_code': 'amstrates',
#     },
# }

# response = r.post(
#     f'https://www.uksafetystore.com/rest/default/V1/guest-carts/{enity_id}/totals-information',
#     headers=headers,
#     json=json_data,
# )
# print(response.text)