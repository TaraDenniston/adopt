from models import db, Pet
from app import app

# Create (or recreate) tables
db.drop_all()
db.create_all()


# Create data for pets table
pet1 = Pet(name='Bethany',
           species = 'cat',
           photo_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/A_Calico_cat.jpg/800px-A_Calico_cat.jpg',
           age = '3',
           notes = 'Bethany is independent, sassy, and talkative, and would prefer a home without children.')
pet2 = Pet(name='Buddy',
           species = 'dog',
           photo_url = 'https://cleverpuppies.com/wp-content/uploads/2022/01/Beagle-Dog-Breed-Everything-You-Need-to-Know.jpg',
           age = '1',
           notes = 'Buddy is sweet, social, confident, and loving. He is already housebroken and does well around children.')
pet3 = Pet(name='Marley',
           species = 'ferret',
           photo_url = 'https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/59757137/2/?bust=1674945527&width=720',
           age = '2',
           notes = 'Marley is energetic and shy but loves to snuggle once comfortable. He would do best in a home without children under 8 years old.')

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

db.session.commit()