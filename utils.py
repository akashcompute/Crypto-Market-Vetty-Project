import requests

BASE_URL = "https://api.coingecko.com/api/v3"


def fetch_coin_by_id(coin_id):
    """
    Fetch details about a specific coin.
    """
    url = f"{BASE_URL}/coins/{coin_id}"
    params = {"localization": "false"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def fetch_categories():
    """
    Fetch all cryptocurrency categories.
    """
    url = f"{BASE_URL}/coins/categories"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_coins(page_num=1, per_page=10):
    """
    Fetch a paginated list of coins with market data in CAD.
    """
    url = f"{BASE_URL}/coins/markets"
    params = {"vs_currency": "cad", "page": page_num, "per_page": per_page}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()