import os
from datetime import datetime


class Config:
    """
    Configuration settings for the Flask application.
    """
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", True)

    # Defined hashed password and username
    ALLOWED_USERS = ["admin", "dummy"]
    PASSWORD = {
        "admin": (
            "pbkdf2:sha256:1000000$DGm7bURyXc8EhhXL$"
            "662d11d1fa2f25669beb2a23c64c529a13579920a811cc81e972c42edca300cf"
        ),
        "dummy": (
            "pbkdf2:sha256:1000000$a3FLnducd5kRxfwu$"
            "0c413162b57e8ef023939e228b07c9b1f53f3100d745a4b21f1fddf9fbc75a59"
        ),
    }

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

    # Logging settings
    LOG_LEVEL = "INFO"
    LOG_FILE = f"app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
