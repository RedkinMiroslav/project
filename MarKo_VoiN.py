from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def character():
    return render_template("index.html")

@app.route("/hero")
def hero_page():
    name = "Марко Воїн"
    age = "25 років"
    weapon = "Меч"
    skills = "Бій, стрільба, захист"
    description = "Марко захищає село від ворогів та допомагає людям."
    
    return render_template("index.html", 
                         character_name=name,
                         character_age=age,
                         character_weapon=weapon,
                         character_skills=skills,
                         character_description=description)

if __name__ == "__main__":
    app.run(debug=True)