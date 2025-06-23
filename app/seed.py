import csv
from . import db
from .models import Episode, Guest, Appearance

def seed_data():
    with open('lateshow.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            guest = Guest(name=row['name'], occupation=row['occupation'])
            db.session.add(guest)
        db.session.commit()

        # Optional dummy episodes & appearances for test
        ep1 = Episode(date='1/11/99', number=1)
        ep2 = Episode(date='1/12/99', number=2)
        db.session.add_all([ep1, ep2])
        db.session.commit()

        app1 = Appearance(rating=4, episode_id=ep1.id, guest_id=1)
        app2 = Appearance(rating=5, episode_id=ep2.id, guest_id=2)
        db.session.add_all([app1, app2])
        db.session.commit()
