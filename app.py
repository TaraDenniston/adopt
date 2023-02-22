from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm 

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '4Wd65|V=N*Crmq"?G$L$Q,*KQfZQP+'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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

    # Create select list choices for species
    species_names = db.session.query(Pet.species)
    spec = [(s, s) for (s,) in species_names]
    form.species.choices = spec

    # If the form is valid on submission, update the db and redirect home
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

    # If coming from GET request or POST request is not valid, rerender form
    # and show any errors
    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'Post'])
def display_pet(pet_id):
    """Display details about a pet and show edit form"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    # If the form is valid on submission, update the db and redirect home
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f'/{pet_id}')
    
    # If coming from GET request or POST request is not valid, rerender form
    # and show any errors
    else:
        return render_template('pet_details.html', pet=pet, form=form)