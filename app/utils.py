import requests
import pkg_resources
import logging
from app.config import Config as config


def fetch_coin_by_id(coin_id):
    """
    Fetch details about a specific coin.
    """
    url = f"{config.BASE_URL}/{config.COINS_ENDPOINT}/{coin_id}"
    params = {"localization": "false"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_categories():
    """
    Fetch all cryptocurrency categories.
    """
    url = (f"{config.BASE_URL}/{config.COINS_ENDPOINT}"
           f"/{config.COINS_ENDPOINT_CATEGORIES}")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_coins(page_num=1, per_page=10):
    """
    Fetch a paginated list of coins with market data in CAD.
    """
    url = (f"{config.BASE_URL}/{config.COINS_ENDPOINT}"
           f"/{config.COINS_ENDPOINT_MARKETS}")
    params = {"vs_currency": "cad", "page": page_num, "per_page": per_page}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


# Get the versions of the third-party libraries used in the application
def get_library_versions():
    libraries = config.LIBRARIES
    versions = {}

    for library in libraries:
        try:
            version = pkg_resources.get_distribution(library).version
            versions[library] = version
        except pkg_resources.DistributionNotFound:
            versions[library] = "Not installed"

    return versions


# Set up logging configuration
def setup_logging():
    """ Set up basic logging configuration. """
    logging.basicConfig(level=config.LOG_LEVEL,
                        filename=config.LOG_FILE,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Logging setup complete.")


# Utility function to log API requests and responses
def log_api_call(endpoint, method, status, response_data=None):
    """ Log each API call with its status and response data. """
    logging.info(f"API called - Endpoint: {endpoint}, "
                 f"Method: {method}, Status: {status}")
    if response_data:
        logging.info(f"Response: {response_data}")
