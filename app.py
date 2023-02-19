from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

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
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'Post'])
def add_pet():
    """Display the form to add a new pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, \
                      age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')   
    else:
        return render_template('add_pet.html', form=form)