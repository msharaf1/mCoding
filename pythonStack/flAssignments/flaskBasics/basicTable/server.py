from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def student_info():
    users = (
        {'first_name' : 'Jason', 'last_name' : 'Smith'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Azadi'},
        {'first_name' : 'Tom', 'last_name' : 'Tonel'}
    )
    return render_template("index.html", users = users)


# print(__name__)

if __name__ =="__main__":
	app.run(debug=True)