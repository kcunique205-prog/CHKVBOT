import requests
# from  plugins.utility.defe import *
r = requests.Session()
def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
response = r.get('https://www.sportystoolshop.com/600-lumen-collapsible-lantern.html')
form_key = getstr(response.text, 'form_key" type="hidden" value="', '"')
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': 'wcid=/efAV4nXOx1vAAAB; lagrange_session=22764e9d-6540-4873-9ad3-365fefc939ed; PHPSESSID=66ijnl1hpeftl05ecumot8m60q; X-Magento-Vary=abb1e68d9253f6a2496bf12d6e4a4da6729bacd5bf72e4b60b5c97c083dd2408; _gcl_au=1.1.197869587.1730828365; _ga=GA1.1.291784570.1730828365; ssUserId=7b8a8cb2-0686-4fb2-9740-e9322a870d67; _isuid=7b8a8cb2-0686-4fb2-9740-e9322a870d67; ssSessionIdNamespace=31b9e811-15ff-4d98-9f54-f1340eb590e9; last_visited_store=tool_shop; mage-cache-sessid=true; form_key=5VQEBEnNgpXl0lho; _pin_unauth=dWlkPU0yRXdNMk5oTjJFdE1qVXhOUzAwWXpZMExXSmpOREl0Wm1VM1pUaG1NelV6WmpNeg; GSIDAVzRzh4ThsWx=8b62b80b-a27e-488f-8ed7-7ff475570ebf; STSIDAVzRzh4ThsWx=7db61951-fdb8-43da-bc58-57913bbfe85b; ltkSubscriber-HomePageEmailSignup=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-AccountCreate=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; _vuid=c0c15fd5-1008-4f18-930f-e89ee08cdbf6; ltkpopup-suppression-f49ca663-f716-40aa-bd33-c49b85760ab7=1; _uetsid=e61d92109b9c11efbdcd3b4bad9bd07d; _uetvid=e61d8a009b9c11ef81262bfc036ed3dc; ltkpopup-session-depth=2-2; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYzJlNDg0MzgtNWM0Mi00NGYzLTk4NWItYjhkYWFiZGZkZDIwJTIyJTJDJTIyZSUyMiUzQTE3MzEzNTM5ODY5MzclN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyMjYwZTRkMjUtMTI5My00MGUxLTk2YWQtOWY0OWNmOTI3Yzg4JTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTczMDgzMDE4Nzk1NCU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyODNkNTNkMjUtMDQ2MC00OGEyLWJlMjctMDkxMDcwOWNkNDhjJTIyJTJDJTIyZSUyMiUzQTE3MzEzNTM5ODY5MzglN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMiUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE3MzA4MzAxODc5NTQlN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNzMwODMwMTg3OTU0JTdEJTdE; TTSVID=a5d6276e-ca5d-4da0-806d-f053f3d947cc; _ga_DSKPQ21442=GS1.1.1730828364.1.1.1730828394.30.0.0',
    'origin': 'https://www.sportystoolshop.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.sportystoolshop.com/600-lumen-collapsible-lantern.html',
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
    'product': '19032',
    'selected_configurable_option': '',
    'related_product': '',
    'item': '19032',
    'form_key': form_key,
    'options[12632]': '',
    'qty': '1',
    'uenc': 'aHR0cHM6Ly93d3cuc3BvcnR5c3Rvb2xzaG9wLmNvbS82MDAtbHVtZW4tY29sbGFwc2libGUtbGFudGVybi5odG1s',
}

response = r.post(
    'https://www.sportystoolshop.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuc3BvcnR5c3Rvb2xzaG9wLmNvbS82MDAtbHVtZW4tY29sbGFwc2libGUtbGFudGVybi5odG1s/product/19032/',
    headers=headers,
    data=data,
)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'wcid=pHsjBD0YO9PVAAAB; ssUserId=2d5b1e91-2702-438d-898f-758832e4ea80; _isuid=2d5b1e91-2702-438d-898f-758832e4ea80; ssSessionIdNamespace=ba01a0f3-6c56-406c-82cf-83c4565d4eca; last_visited_store=tool_shop; mage-cache-sessid=true; form_key=wRpAeXgtpqZZsZm5; PHPSESSID=d4lthph74dccohu7ggopnsrt05; X-Magento-Vary=abb1e68d9253f6a2496bf12d6e4a4da6729bacd5bf72e4b60b5c97c083dd2408; lagrange_session=43308c60-81fb-4787-82c4-83036196bd02; _fbp=fb.1.1730829490568.734518254927275807; _gcl_au=1.1.1118064574.1730829491; _ga=GA1.1.166579159.1730829491; _pin_unauth=dWlkPU1XRTRZalprT1RFdE5tWmxZUzAwT1RZNUxXRmpaV0l0TUdWaFptWXpORGd4WkdKaA; ltkpopup-session-depth=1-2; GSIDAVzRzh4ThsWx=44dae68d-c575-4cb7-9f0d-af01fddfe179; STSIDAVzRzh4ThsWx=aee22b8e-c386-4186-815b-b072291f915b; ltkSubscriber-HomePageEmailSignup=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-AccountCreate=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; TTSVID=e412f266-0f56-4263-a9d2-a6d4a7c6520e; _vuid=d97b217a-fa68-4d95-86bd-796de5db7841; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyM2NiYjg5MmMtMDU3Zi00MjMyLTgzMDEtNGUwZDdhNmE2YjYwJTIyJTJDJTIyZSUyMiUzQTE3MzEzNTUxMDU0NDYlN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNDZhNmE0N2MtODhmNi00NmNhLWI0ZDItY2I5ZWEwNTY4NjY1JTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTczMDgzMTMwNjQ1NyU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyYjZlYjRjNWItY2M1YS00YzcxLTlkZDktMTQ3OWNlNTQyZmYzJTIyJTJDJTIyZSUyMiUzQTE3MzEzNTUxMDU0NDclN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMiUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE3MzA4MzEzMDY0NTclN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNzMwODMxMzA2NDU3JTdEJTdE; _uetsid=854d0cb09b9f11efa4a8fd7e7a81022c; _uetvid=854d33d09b9f11ef9199a17b67fc8413; _ga_DSKPQ21442=GS1.1.1730829490.1.1.1730829511.39.0.0; private_content_version=e42dbcce57018ab775d1f8eedeb28e5d; section_data_ids=%7B%22messages%22%3A1730829511%2C%22customer%22%3A1730829511%2C%22compare-products%22%3A1730829511%2C%22last-ordered-items%22%3A1730829511%2C%22cart%22%3A1730829511%2C%22directory-data%22%3A1730829511%2C%22captcha%22%3A1730829511%2C%22wishlist%22%3A1730829511%2C%22instant-purchase%22%3A1730829511%2C%22loggedAsCustomer%22%3A1730829511%2C%22multiplewishlist%22%3A1730829511%2C%22persistent%22%3A1730829511%2C%22review%22%3A1730829511%2C%22payments%22%3A1730829511%2C%22faq%22%3A1730829511%2C%22hyva_checkout%22%3A1730829511%2C%22recently_viewed_product%22%3A1730829511%2C%22recently_compared_product%22%3A1730829511%2C%22product_data_storage%22%3A1730829511%2C%22paypal-billing-agreement%22%3A1730829511%7D',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.sportystoolshop.com/600-lumen-collapsible-lantern.html',
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

response = r.get('https://www.sportystoolshop.com/checkout/', headers=headers)
