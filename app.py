from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("contact-success.html", name=name)

    return render_template("contact.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")
