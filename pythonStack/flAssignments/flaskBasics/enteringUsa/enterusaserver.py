from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return (render_template("index.html"))

@app.route("/states")
def first():
    return (render_template("states.html"))

@app.route("/cities")
def second():
    return (render_template("cities.html"))

@app.route("/food")
def third():
    return (render_template("food.html"))





@app.route("/fifth")
def home():
	return render_template("fifth")

if __name__ == "__main__":
	app.run(debug = True)