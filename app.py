from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    payment_data = {
        "Bank BRI": "1234567890",
        "SeaBank": "0987654321",
        "ShopeePay": "081234567890",
        "DANA": "081234567890",
        "GoPay": "081234567890"
    }

    return render_template("index.html", payments=payment_data)

if __name__ == "__main__":
    app.run(debug=True)