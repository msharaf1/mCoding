from flask import Flask, session, render_template, redirect
app = Flask(__name__)

app.secret_key="Password123"


@app.route("/")
def index():

    if "count" in session:

        session["count"] += 1
    else:
        session["count"] =1

    return render_template("index.html")




if __name__=="__main__":
    app.run(debug=True)