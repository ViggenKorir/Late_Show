from flask import Flask, jsonify, request
from models import db, Episode, Guest, Appearance

app = Flask(__name__)    
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()

    # Seed data
    guest1 = Guest(name="John Doe", occupation="Actor")
    guest2 = Guest(name="Jane Doe", occupation="Actress")
    guest3 = Guest(name="Bob Smith", occupation="Actor")
    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    episode1 = Episode(date="2022-01-01", number=1)
    episode2 = Episode(date="2022-01-02", number=2)
    episode3 = Episode(date="2022-01-03", number=3)
    db.session.add_all([episode1, episode2, episode3])
    db.session.commit()

    appearance1 = Appearance(rating=5, episode_id=1, guest_id=1)
    appearance2 = Appearance(rating=4, episode_id=2, guest_id=2)
    appearance3 = Appearance(rating=3, episode_id=3, guest_id=3)
    db.session.add_all([appearance1, appearance2, appearance3])
    db.session.commit()

    # Get all guests
    guests = Guest.query.all()
    for guest in guests:
        print(guest.to_dict())

    # Get guest by ID
    guest = Guest.query.get(1)
    print(guest.to_dict())

    # Get guest by name
    guests = Guest.query.filter_by(name="John Doe").all()
    for guest in guests:
        print(guest.to_dict())

    # Get guest by occupation
    guests = Guest.query.filter_by(occupation="Actor").all()
    for guest in guests:
        print(guest.to_dict())

    # Get all episodes
    episodes = Episode.query.all()
    for episode in episodes:
        print(episode.to_dict())

    # Get episode by ID
    episode = Episode.query.get(1)
    print(episode.to_dict())

    # Get episode by date
    episodes = Episode.query.filter_by(date="2022-01-01").all()
    for episode in episodes:
        print(episode.to_dict())

    # Get all appearances
    appearances = Appearance.query.all()
    for appearance in appearances:
        print(appearance.to_dict())

    # Get appearance by ID
    appearance = Appearance.query.get(1)
    print(appearance.to_dict()) 

    # Get appearance by rating
    appearances = Appearance.query.filter_by(rating=5).all()
    for appearance in appearances:
        print(appearance.to_dict())

    # Get appearance by episode ID
    appearances = Appearance.query.filter_by(episode_id=1).all()
    for appearance in appearances:
        print(appearance.to_dict())

    # Get appearance by guest ID
    appearances = Appearance.query.filter_by(guest_id=1).all()
    for appearance in appearances:
        print(appearance.to_dict())

    # Get all appearances for a guest
    guest = Guest.query.get(1)
    appearances = guest.appearances
    for appearance in appearances:
        print(appearance.to_dict())

    # Get all appearances for a guest
    guest = Guest.query.get(1)
    appearances = guest.appearances
    for appearance in appearances:
        print(appearance.to_dict())

    # Get all appearances for an episode
    episode = Episode.query.get(1)
    appearances = episode.appearances
    for appearance in appearances:
        print(appearance.to_dict())
        