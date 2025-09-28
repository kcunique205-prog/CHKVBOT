import random
import requests
import httpx
import asyncio
import aiohttp
import time
import os

# Load proxies from a file
def load_proxies_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Proxy file not found: {file_path}")

    with open(file_path, 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

    if not proxies:
        raise ValueError("No proxies found in the file.")

    return proxies

# Format a proxy string into a dictionary format
def format_proxy(proxy):
    try:
        # Split the proxy string into parts
        parts = proxy.split(':')

        if len(parts) != 4:
            raise ValueError(f"Malformed proxy entry (expected 4 parts): {proxy}")

        # Extract the host, port, username, and password from the parts
        host, port, username, password = parts[0], parts[1], parts[2], parts[3]

        # Construct the URL format for the proxy
        formatted_proxy = f"http://{username}:{password}@{host}:{port}"

        return formatted_proxy
    except (IndexError, ValueError) as e:
        raise ValueError(f"Malformed proxy entry: {proxy}") from e

# Check if a proxy is live using requests
def check_proxy_live_requests(proxy_dict):
    test_url = "http://ip-api.com/json"
    try:
        response = requests.get(test_url, proxies=proxy_dict, timeout=10)
        return response.status_code == 200
    except (requests.exceptions.RequestException, 
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout):
        return False

# Check if a proxy is live using httpx
def check_proxy_live_httpx(proxy_dict):
    test_url = "http://ip-api.com/json"
    try:
        with httpx.Client(proxies=proxy_dict, timeout=10) as client:
            response = client.get(test_url)
        return response.status_code == 200
    except (httpx.RequestError, httpx.HTTPStatusError):
        return False

# Check if a proxy is live using aiohttp
async def check_proxy_live_aiohttp(proxy_dict):
    test_url = "http://ip-api.com/json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(test_url, proxy=proxy_dict["http"], timeout=10) as response:
                return response.status == 200
    except (aiohttp.ClientError, asyncio.TimeoutError):
        return False

# Find a live proxy from the list (generic function for requests and httpx)
def find_live_proxy(proxies_list, check_proxy_function):
    random.shuffle(proxies_list)  # Shuffle proxies to randomize the order

    for proxy in proxies_list:
        try:
            # Format proxy and check if it's live
            proxy_dict = {
                'http': format_proxy(proxy),
                'https': format_proxy(proxy)
            }
            if check_proxy_function(proxy_dict):
                return proxy_dict  # Return the first live proxy found
        except ValueError as e:
            continue

    return None

# Find a live proxy using aiohttp
async def find_live_proxy_aiohttp(proxies_list):
    random.shuffle(proxies_list)

    for proxy in proxies_list:
        try:
            # Format proxy and check if it's live
            proxy_dict = {
                'http': format_proxy(proxy),
                'https': format_proxy(proxy)
            }
            if await check_proxy_live_aiohttp(proxy_dict):
                return proxy_dict
        except ValueError as e:
            continue

    return None

# Main function to get a live proxy with retries (requests and httpx)
def proxies(file_path='proxy.txt', max_retries=5, library="requests"):
    try:
        proxies_list = load_proxies_from_file(file_path)
    except (FileNotFoundError, ValueError) as e:
        return None

    # Choose the checking function based on the selected library (requests or httpx)
    check_function = check_proxy_live_requests if library == "requests" else check_proxy_live_httpx

    for attempt in range(max_retries):
        live_proxy = find_live_proxy(proxies_list, check_function)
        if live_proxy:
            return live_proxy
        else:
            time.sleep(0.2)  # Short delay between retries

    return None 

# Async version of proxy checker using aiohttp
async def proxies_aiohttp(file_path='proxy.txt', max_retries=5):
    try:
        proxies_list = load_proxies_from_file(file_path)
    except (FileNotFoundError, ValueError) as e:
        return None

    for attempt in range(max_retries):
        live_proxy = await find_live_proxy_aiohttp(proxies_list)
        if live_proxy:
            return live_proxy
        else:
            await asyncio.sleep(0.2)  # Short delay between retries

    return None  # Return None if no live proxy is found after max retries
