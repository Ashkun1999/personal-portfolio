from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://portfolio_db_hrjv_user:Rh2vNxRgrxN1EGMIGA8FAk0oDJomJ6kA@dpg-crpfprm8ii6s73chagng-a.oregon-postgres.render.com/portfolio_db_hrjv"
# initialize the app with the extension
db.init_app(app)

from models import Messages, Projects

with app.app_context():
    db.create_all()

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
        email = request.form['email']
        message = request.form['message']   
        new_message = Messages(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        return render_template("contact-success.html", name=name)

    return render_template("contact.html")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    messages = db.session.execute(db.select(Messages).order_by(Messages.id)).scalars()
    
    if request.method == 'POST': # Create a new project
        new_project = Projects(
            title=request.form['title'],
            description=request.form['description'],
            icon=request.form['icon'],
            link=request.form['link']
        )
        db.session.add(new_project)
        db.session.commit()

    projects = db.session.execute(db.select(Projects).order_by(Projects.id)).scalars()

    return render_template("admin.html", messages=messages, projects=projects)

@app.route("/projects")
def projects():
    projects = db.session.execute(db.select(Projects).order_by(Projects.id)).scalars()
    return render_template("projects.html", projects=projects)

@app.route("/projects/<id>", methods=['DELETE'])
def delete_project(id):
    project = db.session.execute(db.select(Projects).where(Projects.id == id)).scalar_one()
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted"})

@app.route("/projects/<id>", methods=['PUT'])
def update_project(id):
    project = db.session.execute(db.select(Projects).where(Projects.id == id)).scalar_one()
    project.title = request.json['title']
    project.description = request.json['description']
    project.icon = request.json['icon']
    project.link = request.json['link']
    db.session.commit()
    return jsonify({"message": "Project updated"})
