from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy in-memory data (NO CSV FILE REQUIRED)
dummy_city_risk = [
    {"city": "Chennai", "risk": 720},
    {"city": "Bangalore", "risk": 680},
    {"city": "Hyderabad", "risk": 610},
    {"city": "Coimbatore", "risk": 590}
]

def analyze_data():
    influential_factor = "credit_score"
    return influential_factor, dummy_city_risk

@app.route('/')
def index():
    return render_template("index1.html")

@app.route('/analyze', methods=['GET'])
def analyze():
    influential_factor, city_risk_list = analyze_data()
    return jsonify({
        "most_influential": influential_factor,
        "city_risk": city_risk_list
    })

@app.route('/predict', methods=['POST'])
def predict():
    data_input = request.get_json()

    credit_score = int(data_input.get("credit_score", 0))
    income = int(data_input.get("income", 0))

    # Risk logic
    if credit_score < 600:
        risk = "High"
    elif credit_score < 750:
        risk = "Medium"
    else:
        risk = "Low"

    # Bank eligibility logic
    eligible_banks = []

    if risk == "Low" and income > 30000:
        eligible_banks = ["Bank 1", "bank 2", "Bank 3"]
    elif risk == "Medium" and income > 20000:
        eligible_banks = ["Bank 2", "Bank 4"]
    elif risk == "High" and income > 15000:
        eligible_banks = ["Bank 5"]

    return jsonify({
        "risk": risk,
        "eligible_banks": eligible_banks
    })

if __name__ == '__main__':
    app.run(debug=True)
