import requests,random,string
from urllib.parse import urlparse, parse_qs, urlunparse

r = requests.Session()

def getstr( data, first, last ):
    try:
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None

def generate_boundary():
    return 'WebKitFormBoundary' + ''.join(random.choices(string.ascii_letters + string.digits, k=16))

web = generate_boundary()
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-17%2017%3A17%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-17%2017%3A17%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; __stripe_mid=2400a0bf-9de8-4108-86af-151ce842309e5ab74e; __stripe_sid=e11e8b66-3504-40bf-b00f-23fd242bc3f590957f; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://spiritinsport.org.uk/donation/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

params = {
    'givewp-route': 'donation-form-view',
    'form-id': '12954',
}

response = r.get('https://spiritinsport.org.uk/', params=params, headers=headers)
signature = getstr(response.text, 'givewp-route-signature="', '&')
signature_expire = getstr(response.text, 'givewp-route-signature-expiration=', '"')

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': f'multipart/form-data; boundary=----{web}',
    # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; __stripe_mid=5510842a-bd69-4f11-ba42-d47baa3101bf6d6efa; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-10-17%2017%3A11%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-10-17%2017%3A11%3A12%7C%7C%7Cep%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F129.0.0.0%20Safari%2F537.36; __stripe_sid=e135366c-0724-42a9-9289-a1518566926d421b2f; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fspiritinsport.org.uk%2Fdonation%2F',
    'origin': 'https://spiritinsport.org.uk',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://spiritinsport.org.uk/?givewp-route=donation-form-view&form-id=12954',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

params = {
    'givewp-route': 'donate',
    'givewp-route-signature': signature,
    'givewp-route-signature-id': 'givewp-donate',
    'givewp-route-signature-expiration': signature_expire,
}

data = f"""
------{web}
Content-Disposition: form-data; name="amount"

1
------{web}
Content-Disposition: form-data; name="currency"

GBP
------{web}
Content-Disposition: form-data; name="donationType"

single
------{web}
Content-Disposition: form-data; name="subscriptionPeriod"

one-time
------{web}
Content-Disposition: form-data; name="subscriptionFrequency"

1
------{web}
Content-Disposition: form-data; name="subscriptionInstallments"

0
------{web}
Content-Disposition: form-data; name="formId"

12954
------{web}
Content-Disposition: form-data; name="gatewayId"

stripe_payment_element
------{web}
Content-Disposition: form-data; name="feeRecovery"

0
------{web}
Content-Disposition: form-data; name="firstName"

Albedo
------{web}
Content-Disposition: form-data; name="lastName"

Jones
------{web}
Content-Disposition: form-data; name="email"

ddddddrdrdr6d@yahoo.com
------{web}
Content-Disposition: form-data; name="anonymous"

false
------{web}
Content-Disposition: form-data; name="donationBirthday"


------{web}
Content-Disposition: form-data; name="originUrl"

https://spiritinsport.org.uk/donation/
------{web}
Content-Disposition: form-data; name="isEmbed"

true
------{web}
Content-Disposition: form-data; name="embedId"

give-form-shortcode-1
------{web}
Content-Disposition: form-data; name="gatewayData[stripePaymentMethod]"

card
------{web}
Content-Disposition: form-data; name="gatewayData[stripePaymentMethodIsCreditCard]"

true
------{web}
Content-Disposition: form-data; name="gatewayData[formId]"

12954
------{web}
Content-Disposition: form-data; name="gatewayData[stripeKey]"

pk_live_51FRIl0GFC210vRrU131niFXdKpyHtMvxVgdKr6DxTHtZJVrNV2whig1Y1imMx2RLRv5DCJGWcndk2Vtkse3E3elu00dWj0bOnY
------{web}
Content-Disposition: form-data; name="gatewayData[stripeConnectedAccountId]"

acct_1FRIl0GFC210vRrU
------{web}--
"""

response = r.post('https://spiritinsport.org.uk/',headers=headers, data=data)
open('response.html', 'wb').write(response.content)