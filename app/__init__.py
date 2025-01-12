from flask import Flask
from flasgger import Swagger
from app.routes import api_bp

def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    # Initialize Swagger with the Flask app
    Swagger(app, template_file='../resources/swagger.yaml')

    # Define the root endpoint that lists all available API endpoints
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
                    <li><a href="/api/v1/version">/api/v1/version</a></li>  <!-- Version information -->
                    <li><a href="/api/v1/health">/api/v1/health</a></li>    <!-- Health check -->
                    <li><a href="/api/v1/categories">/api/v1/categories</a></li>  <!-- List of categories -->
                    <li><a href="/api/v1/coins/bitcoin">/api/v1/coins/&lt;coin_id&gt;</a> eg: bitcoin</li> <!-- Coin details by ID -->
                    <li><a href="/api/v1/coins">/api/v1/coins</a></li>  <!-- List of coins (with pagination) -->
                    <li><a href="/apidocs">/apidocs</a></li>  <!-- Swagger UI -->
                </ul>
            </body>
        </html>
        '''

    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app