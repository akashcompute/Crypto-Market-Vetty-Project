from app import create_app

# Create an app instance
app = create_app()

if __name__ == '__main__':
    # Run the app on localhost
    app.run(host='0.0.0.0', port=app.config["PORT"], debug=True)
