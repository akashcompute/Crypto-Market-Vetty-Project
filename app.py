from flask import Flask, jsonify, request

from utils import *

app = Flask(__name__)

@app.route('/')
def apis_available():
    return '''
    <html>
        <head>
            <title>API Endpoints</title>
        </head>
        <body>
            <h1>APIs available:</h1>
            <ul>
                <li><a href="/version">/version</a></li>
                <li><a href="/health">/health</a></li>
                <li><a href="/coins/bitcoin">/coins/&lt;coin_id&gt;</a>eg: bitcoin</li>
                <li><a href="/categories">/categories</a></li>
                <li><a href="/coins">/coins</a></li>
            </ul>
        </body>
    </html>
    '''

@app.route('/version', methods=['GET'])
def version():
    return jsonify({"version": "1.0.0"}), 200

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "The application is running!"}), 200

@app.route('/coins/<string:coin_id>', methods=['GET'])
def get_coin_by_id(coin_id):
    coin_data = fetch_coin_by_id(coin_id)
    return jsonify(coin_data)

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = fetch_categories()
    return jsonify(categories)

@app.route('/coins', methods=['GET'])
def get_coins():
    page_num = int(request.args.get('page_num', 1))
    per_page = int(request.args.get('per_page', 10))
    coins = fetch_coins(page_num, per_page)
    return jsonify(coins)

if __name__ == '__main__':
    app.run(debug=True)