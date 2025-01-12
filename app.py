from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def apis_available():
    return 'APIs available: /health'

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "The application is running!"}), 200

if __name__ == '__main__':
    app.run(debug=True)