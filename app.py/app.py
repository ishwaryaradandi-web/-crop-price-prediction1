from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Crop Price Prediction</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f7f2;
            text-align: center;
            padding: 40px 20px;
        }

        .box {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2e7d32;
        }

        input, select, button {
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            border-radius: 10px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        button {
            background: #2e7d32;
            color: white;
            border: none;
            font-size: 16px;
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>🌾 Crop Price Prediction</h1>
        <p>Enter crop details to predict the price.</p>

        <select>
            <option>Select Crop</option>
            <option>Rice</option>
            <option>Wheat</option>
            <option>Maize</option>
            <option>Tomato</option>
            <option>Potato</option>
        </select>

        <input type="number" placeholder="Enter quantity (kg)">

        <input type="text" placeholder="Enter location">

        <button>Predict Price</button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()
