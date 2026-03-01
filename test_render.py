import os
from flask import Flask
from models.base import db
import init_db
from routes.main_routes import main_bp

# Set sqlite DB for local testing
os.environ['DATABASE_URL'] = 'sqlite:///test_app.db'
app = Flask(__name__, template_folder='templates', static_folder='statics')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(main_bp)

# Initialize and seed database
with app.app_context():
    init_db.init_db()  # Note: this will create tables using a new app instance but uses the same env var. Let's just create tables directly here.

with app.app_context():
    # Make a dummy request to index page to test template rendering
    with app.test_client() as client:
        response = client.get('/')
        if response.status_code == 200:
            print("Successfully rendered index.html")
            print("Preview length:", len(response.data))
        else:
            print("Failed to render index.html. Status Code:", response.status_code)
            print("Error details:", response.data.decode('utf-8'))
