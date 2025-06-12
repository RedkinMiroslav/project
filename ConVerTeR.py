from flask import Flask, render_template, request

app = Flask(__name__)

def convert_units(value, from_unit, to_unit):
    weight_conversion_factors = {
        'g': {'kg': 0.001, 'mg': 1000, 'lb': 0.00220462},
        'kg': {'g': 1000, 'mg': 1000000, 'lb': 2.20462},
        'mg': {'g': 0.001, 'kg': 0.000001, 'lb': 0.00000220462},
        'lb': {'g': 453.592, 'kg': 0.453592, 'mg': 453592}
    }

    volume_conversion_factors = {
        'ml': {'l': 0.001, 'gal': 0.000264172, 'oz': 0.033814},
        'l': {'ml': 1000, 'gal': 0.264172, 'oz': 33.814},
        'gal': {'ml': 3785.41, 'l': 3.78541, 'oz': 128},
        'oz': {'ml': 29.5735, 'l': 0.0295735, 'gal': 0.0078125}
    }

    if from_unit == to_unit:
        return value

    conversion_factors = weight_conversion_factors if from_unit in weight_conversion_factors else volume_conversion_factors

    return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            result = convert_units(value, from_unit, to_unit)
        except ValueError:
            result = "Помилка: Введи число!"
    return render_template("index1.html", result=result)

@app.route("/more_info")
def more_info():
    return render_template("more_info.html")

if __name__ == "__main__":
    app.run(debug=True)
