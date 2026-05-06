from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    deployment_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins CI/CD Demo</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
                color: white;
            }}

            .container {{
                text-align: center;
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
                backdrop-filter: blur(8px);
            }}

            h1 {{
                font-size: 42px;
                margin-bottom: 20px;
            }}

            h2 {{
                color: #00ffcc;
                margin-bottom: 20px;
            }}

            p {{
                font-size: 18px;
                margin: 10px 0;
            }}

            .status {{
                margin-top: 20px;
                padding: 10px 20px;
                background: #00c853;
                display: inline-block;
                border-radius: 10px;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 Jenkins CI/CD Pipeline Demo</h1>

            <h2>Deployment Successful</h2>

            <p><strong>Application:</strong> Flask Demo App</p>
            <p><strong>Deployed Via:</strong> Jenkins Pipeline</p>
            <p><strong>Containerized Using:</strong> Docker</p>
            <p><strong>Deployment Time:</strong> {deployment_time}</p>

            <div class="status">
                ✅ Version 3 Live in Production
            </div>
        </div>
    </body>
    </html>
    """

app.run(host='0.0.0.0', port=5000)