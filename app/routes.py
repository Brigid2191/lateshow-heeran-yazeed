from flask import Blueprint, jsonify, request
from .models import db, Episode, Guest, Appearance

# Create a blueprint
api_bp = Blueprint('api', __name__)

# Root route for testing
@api_bp.route('/')
def index():
    return {'message': 'Welcome to the Late Show API'}

# GET /episodes
@api_bp.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

# GET /episodes/<id>
@api_bp.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    return jsonify({'error': 'Episode not found'}), 404

# GET /guests
@api_bp.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])

# POST /appearances
@api_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        rating = int(data['rating'])
        guest_id = int(data['guest_id'])
        episode_id = int(data['episode_id'])

        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict(nested=True)), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

