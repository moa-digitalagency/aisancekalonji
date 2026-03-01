from flask import Flask
from models.base import db

# Import models so SQLAlchemy knows about them
import models.user
import models.item

def init_db():
    app = Flask(__name__)

    # Configure the PostgreSQL database URI
    # In a real app, this should come from environment variables or a config file
    # For now, we will use a dummy URI that allows us to at least verify the context creation locally
    # e.g., using sqlite for a syntax test or requiring the user to provide correct env variables

    import os
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost/aisancekalonji'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()
        print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
