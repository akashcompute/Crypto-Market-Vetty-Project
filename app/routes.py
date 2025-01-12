from flask import Blueprint, jsonify, request
from app.utils import (
    setup_logging,
    log_api_call,
    get_library_versions,
    fetch_coins,
    fetch_categories,
    fetch_coin_by_id
)
from app.config import Config as config

# Create a blueprint for API routes
api_bp = Blueprint('api', __name__)

# Set up logging
setup_logging()


# Health Check Endpoint: This route returns the health status
@api_bp.route(f'/{config.HEALTH_ENDPOINT}', methods=['GET'])
def health():
    """
    Health check endpoint to check if the application is running
    """
    log_api_call(f'/{config.HEALTH_ENDPOINT}', config.REQUEST_GET, 'STARTED')
    try:
        # Return healthy status
        log_api_call(f'/{config.HEALTH_ENDPOINT}',
                     config.REQUEST_GET, config.SUCCESS_RESPONSE)
        return jsonify({"status": "healthy",
                        "message": "The application is running!"}), 200
    except Exception as e:
        log_api_call(f'/{config.HEALTH_ENDPOINT}', config.REQUEST_GET,
                     config.ERROR_RESPONSE, str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})


# Version Endpoint: This route returns the current version of the application.
@api_bp.route(f'/{config.VERSION_ENDPOINT}', methods=[config.REQUEST_GET])
def version():
    libraries_versions = get_library_versions()
    log_api_call(f'/{config.VERSION_ENDPOINT}', config.REQUEST_GET, 'STARTED')
    try:
        # Return version info
        return jsonify({
            "app_version": config.APP_VERSION,
            "libraries_versions": libraries_versions
        }), 200
    except Exception as e:
        log_api_call(f'/{config.VERSION_ENDPOINT}', config.REQUEST_GET,
                     config.ERROR_RESPONSE, str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})


# Coin Details Endpoint: This route fetches coin details by coin_id.
@api_bp.route(f'/{config.COINS_ENDPOINT}/<string:coin_id>',
              methods=[config.REQUEST_GET])
def get_coin_by_id(coin_id):
    """
    Fetch details about a specific coin by its ID
    """
    # Fetch coin data based on the coin_id
    log_api_call(f'/{config.COINS_ENDPOINT}/{coin_id}',
                 config.REQUEST_GET, 'STARTED')
    coin_data = fetch_coin_by_id(coin_id)
    if coin_data is None:
        log_api_call(f'/{config.COINS_ENDPOINT}/{coin_id} '
                     f'{config.REQUEST_GET}', config.ERROR_RESPONSE,
                     'Coin not found')
        return jsonify({"error": "Coin not found"}), 404
    log_api_call(f'/{config.COINS_ENDPOINT}/{coin_id}',
                 config.REQUEST_GET, config.SUCCESS_RESPONSE, coin_data)
    return jsonify(coin_data)


# Categories Endpoint: This route returns a list of available categories.
@api_bp.route(f'/{config.COINS_ENDPOINT_CATEGORIES}',
              methods=[config.REQUEST_GET])
def get_categories():
    """
    List all cryptocurrency categories
    """
    log_api_call(f'/{config.COINS_ENDPOINT_CATEGORIES}',
                 config.REQUEST_GET, 'STARTED')
    try:
        categories = fetch_categories()

        # Log the successful response
        log_api_call(f'/{config.COINS_ENDPOINT_CATEGORIES}',
                     config.REQUEST_GET, config.SUCCESS_RESPONSE, categories)

        return jsonify(categories)
    except Exception as e:
        log_api_call(f'/{config.COINS_ENDPOINT_CATEGORIES}',
                     config.REQUEST_GET, config.ERROR_RESPONSE, str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})


# Coins List Endpoint: This route fetches a paginated list of coins.
@api_bp.route(f'/{config.COINS_ENDPOINT}', methods=[config.REQUEST_GET])
def get_coins():
    """
    List all cryptocurrencies with pagination
    """
    page_num = int(request.args.get('page_num', 1))
    per_page = int(request.args.get('per_page', 10))

    # Log the API request
    log_api_call(f'/{config.COINS_ENDPOINT}', config.REQUEST_GET, 'STARTED',
                 {"page_num": page_num, "per_page": per_page})

    try:
        coins = fetch_coins(page_num, per_page)

        # Log the successful response
        log_api_call(f'/{config.COINS_ENDPOINT}', config.REQUEST_GET,
                     config.SUCCESS_RESPONSE, coins)

        # Return formatted response
        return jsonify(coins)
    except Exception as e:
        # Log the error response
        log_api_call(f'/{config.COINS_ENDPOINT}',
                     config.REQUEST_GET, config.ERROR_RESPONSE, str(e))

        # Return error response
        return jsonify({"status": "error",
                        "message": str(e),
                        "status_code": 500})
