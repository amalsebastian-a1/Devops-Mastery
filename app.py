from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DevOps Mastery Challenge!"

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

@app.route("/about")
def about():
    return jsonify({"project": "DevOps Mastery Challenge"})

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
