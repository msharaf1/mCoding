from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = "HelloWorld.com1"

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    session["data"] = request.form
    return redirect("/result")

@app.route("/result")
def results():
	return render_template("result.html")


# @app.route("/danger")
# def danger():

#     return redirect("/")





if __name__=="__main__":
    app.run(debug=True)