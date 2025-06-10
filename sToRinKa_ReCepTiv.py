from flask import Flask, render_template, request

app = Flask(__name__)

recipes = [
    {"name": "Омлет", "type": "сніданок", "difficulty": "легка"},
    {"name": "Суп", "type": "обід", "difficulty": "середня"},
    {"name": "Паста Карбонара", "type": "вечеря", "difficulty": "складна"},
    {"name": "Салат Цезар", "type": "обід", "difficulty": "легка"},
    {"name": "Млинці", "type": "сніданок", "difficulty": "середня"},
    {"name": "Запечена риба", "type": "вечеря", "difficulty": "середня"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        meal_type = request.form.get("meal_type")
        difficulty = request.form.get("difficulty")
        filtered_recipes = [
            recipe for recipe in recipes
            if (not meal_type or recipe["type"] == meal_type) and
            (not difficulty or recipe["difficulty"] == difficulty)
        ]
        return render_template("index.html", recipes=filtered_recipes)
    return render_template("index.html", recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)