from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚀 Flask + ArgoCD</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #1f1c2c, #928dab);
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                flex-direction: column;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 0.5em;
                animation: glow 2s ease-in-out infinite alternate;
            }
            p {
                font-size: 1.5em;
                opacity: 0.8;
            }
            @keyframes glow {
                from { text-shadow: 0 0 10px #fff, 0 0 20px #00f, 0 0 30px #00f; }
                to { text-shadow: 0 0 20px #fff, 0 0 40px #0ff, 0 0 60px #0ff; }
            }
        </style>
    </head>
    <body>
        <h1>👨‍💻 Welcome to Damyan Myashkov’s Web App</h1>
        <p>Deployed with 🚀 Flask + 🌀 ArgoCD on Kubernetes!</p>
    </body>
    </html>
    """)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
