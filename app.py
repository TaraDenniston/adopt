from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '4Wd65|V=N*Crmq"?G$L$Q,*KQfZQP+'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def display_home_page():
    """Display the home page"""
    return render_template('index.html')