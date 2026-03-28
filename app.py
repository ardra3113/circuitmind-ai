
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 🏠 Home route
@app.route("/")
def home():
    return "App is working perfectly 🚀"

# 🔍 Example route (you can modify for your project)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.get("input")

    # 👉 Replace this logic with your AI model
    result = f"You entered: {data}"

    return render_template("index.html", result=result)

# 🚀 Run app (IMPORTANT for deployment)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))