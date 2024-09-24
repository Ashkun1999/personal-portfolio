from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://portfolio_db_hrjv_user:Rh2vNxRgrxN1EGMIGA8FAk0oDJomJ6kA@dpg-crpfprm8ii6s73chagng-a.oregon-postgres.render.com/portfolio_db_hrjv"
# initialize the app with the extension
db.init_app(app)

class Messages(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    message: Mapped[str]

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

@app.route("/admin")
def admin():
    messages = db.session.execute(db.select(Messages).order_by(Messages.id)).scalars()
    return render_template("admin.html", messages=messages)

@app.route("/projects")
def projects():
    return render_template("projects.html")
