# from flask import Flask, render_template
# from app import routes
# import os

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     # Use the $PORT environment variable to bind to the correct port
#     port = int(os.environ.get("PORT", 8000))  # Default to 8000 for local testing
#     app.run(host="0.0.0.0", port=port)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
