
from flask import Flask, render_template_string, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Sample regression data
X = np.array([[0], [10], [20], [30], [40], [50]])
y = np.array([32, 50, 68, 86, 104, 122])

model = LinearRegression()
model.fit(X, y)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>FLAME'26 Regression</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #101827;
            color: white;
            text-align: center;
            padding: 30px 15px;
        }
        .card {
            background: #1e293b;
            max-width: 520px;
            margin: 30px auto;
            padding: 25px;
            border-radius: 16px;
        }
        input, button {
            padding: 12px;
            margin: 8px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
        }
        button {
            background: #38bdf8;
            cursor: pointer;
            font-weight: bold;
        }
        .result { color: #67e8a5; font-size: 22px; }
    </style>
</head>
<body>
    <h1>FLAME'26</h1>
    <h2>Linear Regression Experiment</h2>
    <div class="card">
        <p>Enter a Celsius temperature to predict Fahrenheit.</p>
        <form method="POST">
            <input type="number" step="any" name="temp"
                   placeholder="Temperature in °C" required>
            <button type="submit">Predict</button>
        </form>
        {% if result is not none %}
            <p class="result">Predicted: {{ result }} °F</p>
        {% endif %}
        <p>Model: y = 1.8x + 32</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        temp = float(request.form["temp"])
        result = round(float(model.predict(np.array([[temp]]))[0]), 2)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
