from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    db_host = os.getenv("DB_HOST", "not-set")
    return f"App is running! Connected to DB at {db_host}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
