from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Version 1 - Jenkins CI/CD Demo"

app.run(host='0.0.0.0', port=5000)