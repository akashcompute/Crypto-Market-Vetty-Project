import os


class Config:
    """
    Configuration settings for the Flask application.
    """

    # Paths and URLs
    SWAGGER_YAML = os.path.join(os.path.dirname(__file__),
                                '../resources/swagger.yaml')
    BASE_URL = "https://api.coingecko.com/api/v3"

    # Application settings
    PORT = os.getenv("PORT", 5000)
    APP_VERSION = {"version": "1.0.0"}

    # Endpoints
    COINS_ENDPOINT = "coins"
    COINS_ENDPOINT_MARKETS = "markets"
    COINS_ENDPOINT_CATEGORIES = "categories"
    VERSION_ENDPOINT = "version"
    HEALTH_ENDPOINT = "health"

    # Libraries used
    LIBRARIES = [
        "Flask",
        "Flasgger",
        "requests",
        "Werkzeug",
        "flake8",
        "Jinja2",
        "PyYAML",
        "jsonschema"
    ]

    # Request types and response constants
    REQUEST_GET = "GET"
    ERROR_RESPONSE = "ERROR"
    SUCCESS_RESPONSE = "SUCCESS"
