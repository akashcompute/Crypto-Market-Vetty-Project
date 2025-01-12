from flask import Blueprint, jsonify, request
from app.utils import *

# Define a Blueprint for the API. The first argument ('api') is the name of the blueprint,
# and the second argument (__name__) is the current module.
api_bp = Blueprint('api', __name__)

# Set up logging
setup_logging()


# Health Check Endpoint: This route returns the health status of the application.
@api_bp.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint to check if the application is running
    """
    log_api_call('/health', 'GET', 'STARTED')
    try:
        # Return healthy status
        log_api_call('/health', 'GET', 'SUCCESS')
        return jsonify({"status": "healthy", "message": "The application is running!"}), 200
    except Exception as e:
        log_api_call('/health', 'GET', 'ERROR', str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})

# Version Endpoint: This route returns the current version of the application.
@api_bp.route('/version', methods=['GET'])
def version():
    app_version = {"version": "1.0.0"}

    libraries_versions = get_library_versions()
    log_api_call('/version', 'GET', 'STARTED')
    try:
        # Return version info
        return jsonify({
            "app_version": app_version,
            "libraries_versions": libraries_versions
        }), 200
    except Exception as e:
        log_api_call('/version', 'GET', 'ERROR', str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})


# Coin Details Endpoint: This route fetches coin details by coin_id.
@api_bp.route('/coins/<string:coin_id>', methods=['GET'])
def get_coin_by_id(coin_id):
    """
    Fetch details about a specific coin by its ID
    """
    # Fetch coin data based on the coin_id
    log_api_call(f'/coins/{coin_id}', 'GET', 'STARTED')
    coin_data = fetch_coin_by_id(coin_id)
    if coin_data is None:
        log_api_call(f'/coins/{coin_id}' 'GET', 'ERROR', 'Coin not found')
        return jsonify({"error": "Coin not found"}), 404
    log_api_call(f'/coins/{coin_id}', 'GET', 'SUCCESS', coin_data)
    return jsonify(coin_data)

# Categories Endpoint: This route returns a list of available categories.
@api_bp.route('/categories', methods=['GET'])
def get_categories():
    """
    List all cryptocurrency categories
    """
    log_api_call('/categories', 'GET', 'STARTED')
    try:
        categories = fetch_categories()

        # Log the successful response
        log_api_call('/categories', 'GET', 'SUCCESS', categories)

        return jsonify(categories)
    except Exception as e:
        log_api_call('/categories', 'GET', 'ERROR', str(e))
        return jsonify({"status": "error", "message": str(e),
                        "status_code": 500})

# Coins List Endpoint: This route fetches a paginated list of coins.
@api_bp.route('/coins', methods=['GET'])
def get_coins():
    """
    List all cryptocurrencies with pagination
    """
    # Fetch pagination parameters from the query string (default values: page 1, per page 10)
    page_num = int(request.args.get('page_num', 1))
    per_page = int(request.args.get('per_page', 10))

    # Log the API request
    log_api_call('/coins', 'GET', 'STARTED',
                 {"page_num": page_num, "per_page": per_page})

    try:
        coins = fetch_coins(page_num, per_page)

        # Log the successful response
        log_api_call('/coins', 'GET', 'SUCCESS', coins)

        # Return formatted response
        return jsonify(coins)
    except Exception as e:
        # Log the error response
        log_api_call('/coins', 'GET', 'ERROR', str(e))

        # Return error response
        return jsonify({"status": "error",
                        "message": str(e),
                        "status_code": 500})