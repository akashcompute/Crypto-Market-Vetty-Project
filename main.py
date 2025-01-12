from app import create_app

# Create an app instance
app = create_app()

if __name__ == '__main__':
    port = app.config.get('PORT', 5000)
    debug_mode = app.config.get('FLASK_ENV') == 'development'
    # Run the app on localhost
    app.run(host='0.0.0.0', port=app.config["PORT"], debug=True)
