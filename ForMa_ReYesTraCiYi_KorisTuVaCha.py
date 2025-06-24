from flask import Flask, render_template, request
import requests

app = Flask(__name__)
PHP_API_URL = "https://justconsole.tech/python/api.php?table=users"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            response = requests.get(PHP_API_URL)
            users = response.json()
            for user in users:
                if user["username"] == username and user["password"] == password:
                    return f"<h1>Ласкаво просимо, {username}!</h1>"
            return render_template("login.html", error="Невірний логін або пароль!")
        except requests.exceptions.RequestException as e:
            return f"Помилка при підключенні до сервера: {str(e)}</p>"
    return render_template("login.html", error=None)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        try:
            data = {
                'username': username,
                'email': email,
                'password': password
            }
            response = requests.post(PHP_API_URL, data=data)
            if response.status_code == 200:
                return render_template("register.html", success="Користувач успішно зареєстрований!")
            else:
                return render_template("register.html", error="Помилка реєстрації")
        except requests.exceptions.RequestException as e:
            return render_template("register.html", error=f"Помилка підключення: {str(e)}")
    return render_template("register.html", error=None, success=None)

if __name__ == "__main__":
    app.run(debug=True, port=5001)