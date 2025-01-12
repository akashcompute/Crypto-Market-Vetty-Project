from app import create_app

# Create an app instance
app = create_app()

if __name__ == '__main__':
    port = app.config.get('PORT', 5000)
    # Run the app on localhost
    app.run(host='0.0.0.0', port=port, debug=app.config.get('FLASK_DEBUG'))
