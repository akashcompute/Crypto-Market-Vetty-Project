from app import create_app

# Create an app instance
app = create_app()

if __name__ == '__main__':
    # Run the app on localhost, port 5050
    app.run(host='0.0.0.0', port=5050, debug=True)
