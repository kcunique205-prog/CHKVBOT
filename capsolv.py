import httpx
import asyncio
import time

API_KEY = None
CAPTCHA_SERVER = None
TIMEOUT = 300  # Timeout in seconds


# Function to load solver configuration
def load_solver_config():
    global API_KEY, CAPTCHA_SERVER
    try:
        with open("solver_api.txt", "r") as file:
            config = file.read().strip().split("|")
            if config[0] == "1":
                # ensure scheme is included
                if not config[1].startswith("http"):
                    CAPTCHA_SERVER = f"http://{config[1]}"
                else:
                    CAPTCHA_SERVER = config[1]
                API_KEY = config[2]
            elif config[0] == "2":
                CAPTCHA_SERVER = "https://api.2captcha.com"
                API_KEY = config[1]
    except Exception as e:
        return f"Error loading solver configuration: {e}"


# Function to get captcha solver balance
async def get_balance():
    url = f"{CAPTCHA_SERVER}/res.php?key={API_KEY}&action=getbalance"
    retries = 5
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        for attempt in range(retries):
            try:
                response = await client.get(url)
                if response.status_code == 200:
                    return response.text
                else:
                    return f"Error getting balance: {response.status_code}"
            except httpx.TimeoutException:  # ✅ handles connect/read/write timeouts
                await asyncio.sleep(2)  # retry after delay
            except httpx.HTTPError as e:  # ✅ base class for all httpx errors
                return f"Error getting balance: {e}"
        return "Failed to connect after multiple retries."


# Function to solve reCAPTCHA
async def solve_recaptcha(url, site_key, invisible=0):
    max_retries = 5
    retry_delay = 5

    for attempt in range(max_retries):
        create_task_data = {
            "key": API_KEY,
            "method": "userrecaptcha",
            "googlekey": site_key,
            "pageurl": url,
            "invisible": invisible
        }

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.post(f"{CAPTCHA_SERVER}/in.php", data=create_task_data)
            create_task_response = response.text

            if response.status_code != 200 or "ERROR" in create_task_response:
                if "ERROR_NO_SLOT_AVAILABLE" in create_task_response and attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    continue
                return f"Error creating reCAPTCHA task: {create_task_response}"

            task_id = create_task_response.split('|')[-1]

        result_url = f"{CAPTCHA_SERVER}/res.php?key={API_KEY}&action=get&id={task_id}"
        start_time = time.time()

        while time.time() - start_time < TIMEOUT:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                response = await client.get(result_url)
                result_text = response.text

                if response.status_code != 200:
                    return f"Error getting reCAPTCHA result: {response.status_code}"

                if result_text.startswith("CAPCHA_NOT_READY"):
                    await asyncio.sleep(2)
                    continue
                elif result_text.startswith("ERROR"):
                    return f"Error in reCAPTCHA result: {result_text}"

                captcha_solution = result_text.split('|')[-1]
                return captcha_solution

        return "reCAPTCHA solving timed out."


# Function to solve hCaptcha
async def solve_hcaptcha(url, site_key, invisible=0):
    max_retries = 5
    retry_delay = 5

    for attempt in range(max_retries):
        create_task_data = {
            "key": API_KEY,
            "method": "hcaptcha",
            "googlekey": site_key,
            "pageurl": url,
            "invisible": invisible
        }

        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.post(f"{CAPTCHA_SERVER}/in.php", data=create_task_data)
            create_task_response = response.text

            if response.status_code != 200 or "ERROR" in create_task_response:
                if "ERROR_NO_SLOT_AVAILABLE" in create_task_response and attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    continue
                return f"Error creating hCaptcha task: {create_task_response}"

            task_id = create_task_response.split('|')[-1]

        result_url = f"{CAPTCHA_SERVER}/res.php?key={API_KEY}&action=get&id={task_id}"
        start_time = time.time()

        while time.time() - start_time < TIMEOUT:
            async with httpx.AsyncClient(timeout=TIMEOUT) as client:
                response = await client.get(result_url)
                result_text = response.text

                if response.status_code != 200:
                    return f"Error getting hCaptcha result: {response.status_code}"

                if result_text.startswith("CAPCHA_NOT_READY"):
                    await asyncio.sleep(2)
                    continue
                elif result_text.startswith("ERROR"):
                    return f"Error in hCaptcha result: {result_text}"

                captcha_solution = result_text.split('|')[-1]
                return captcha_solution

        return "hCaptcha solving timed out."
