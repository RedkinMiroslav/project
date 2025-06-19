from flask import Flask, render_template, request, session, url_for, redirect

app = Flask(__name__)
app.secret_key = "KaLcuLaToR"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Помилка! Ділення на ноль неможливо!"
            result = num1 / num2

        session["last_result"] = result
        return redirect(url_for("index"))

    last_result = session.get("last_result", None)
    return render_template("KaLcuLaToR.html", last_result=last_result)

if __name__ == "__main__":
    app.run(debug=True)
