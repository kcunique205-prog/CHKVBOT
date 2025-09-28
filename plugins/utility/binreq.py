import requests
async def bin_data(bin):
    try:
        api = requests.get(f'https://bins.antipublic.cc/bins/{bin}',timeout=10).json()
        ch = api.get('brand') or '------'
        type = api.get('type') or '------'
        ra = api.get('level') or '------'
        ame = api.get('bank') or '------' 
        cou = api.get('country') or '------' 
        emoji = api.get('flag') or '🏳️'

        return ch, type, ra, ame, cou, emoji
    except:
        return '------', '------', '------', '------', '------', '🏳️'
