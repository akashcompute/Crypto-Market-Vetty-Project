from flask import Blueprint, jsonify, request
from utils import *  # Assuming this contains the functions to fetch data from a source (e.g., database, API)

# Define a Blueprint for the API. The first argument ('api') is the name of the blueprint,
# and the second argument (__name__) is the current module.
api_bp = Blueprint('api', __name__)

# Health Check Endpoint: This route returns the health status of the application.
@api_bp.route('/health', methods=['GET'])
def health_check():

    # Returns a JSON response with status and a message
    return jsonify({"status": "healthy", "message": "The application is running!"}), 200

# Version Endpoint: This route returns the current version of the application.
@api_bp.route('/version', methods=['GET'])
def version():
    # Returns the current version in a JSON response
    return jsonify({"version": "1.0.0"}), 200

# Coin Details Endpoint: This route fetches coin details by coin_id.
@api_bp.route('/coins/<string:coin_id>', methods=['GET'])
def get_coin_by_id(coin_id):
    # Fetch coin data based on the coin_id
    coin_data = fetch_coin_by_id(coin_id)  # Assuming a function that fetches coin data
    return jsonify(coin_data)

# Categories Endpoint: This route returns a list of available categories.
@api_bp.route('/categories', methods=['GET'])
def get_categories():
    # Fetch and return a list of categories in JSON format
    categories = fetch_categories()  # Assuming a function that fetches categories
    return jsonify(categories)

# Coins List Endpoint: This route fetches a paginated list of coins.
@api_bp.route('/coins', methods=['GET'])
def get_coins():
    # Fetch pagination parameters from the query string (default values: page 1, per page 10)
    page_num = int(request.args.get('page_num', 1))
    per_page = int(request.args.get('per_page', 10))

    # Fetch the list of coins based on the pagination parameters
    coins = fetch_coins(page_num, per_page)  # Assuming a function that fetches coins
    return jsonify(coins)