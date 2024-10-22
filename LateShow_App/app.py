from flask import Flask, jsonify, request
from models import db, Episode, Guest, Appearance
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app=Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///app.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

db.init_app(app)

# tables in the database
migrate = Migrate(app, db)
def create_tables():
    db.create_all()

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)

    if episode:
        return jsonify(episode.to_dict())
    else:
        return jsonify({"error": "Episode not found"}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(rating=data['rating'], episode_id=data['episode_id'], guest_id=data['guest_id'])
    
    try:
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except Exception as e:
        db.session.rollback()  # Roll back the session on error
        return jsonify({"errors": ["validation errors"]}), 400

if __name__ == '__main__':
    app.run(debug=True)
