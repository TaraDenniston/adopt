from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG = 'https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'

class Pet(db.Model):
    """A pet potentially available for adoption"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    name = db.Column(db.Text,
                     nullable = False)
    species = db.Column(db.Text,
                        nullable = False)
    photo_url = db.Column(db.Text,
                          default = DEFAULT_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)

    def __repr__(self):
        return f'<Pet {self.id}: {self.name} the {self.species}>'
