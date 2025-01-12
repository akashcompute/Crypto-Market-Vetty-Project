from flask import Flask
from flasgger import Swagger
from app.routes import api_bp
from app.config import Config


def create_app():
    # Create the Flask application instance
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Swagger with the Flask app
    Swagger(app, template_file=app.config['SWAGGER_YAML'])

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
                    <li>
                        <a href="/api/v1/version">/api/v1/version</a>
                        <!-- Version information -->
                    </li>
                    <li>
                        <a href="/api/v1/health">/api/v1/health</a>
                        <!-- Health check -->
                    </li>
                    <li>
                        <a href="/api/v1/categories">/api/v1/categories</a>
                        <!-- List of categories -->
                    </li>
                    <li>
                        <a href="/api/v1/coins/bitcoin">
                        /api/v1/coins/&lt;coin_id&gt;</a>
                        eg: bitcoin
                        <!-- Coin details by ID -->
                    </li>
                    <li>
                        <a href="/api/v1/coins">/api/v1/coins</a>
                        <!-- List of coins (with pagination) -->
                    </li>
                    <li>
                        <a href="/apidocs">/apidocs</a>
                        <!-- Swagger UI -->
                    </li>
                </ul>
            </body>
        </html>
        '''

    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
