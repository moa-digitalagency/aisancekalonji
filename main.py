import os
from flask import Flask, render_template
from flask_login import LoginManager
from models.base import db
from models.admin_user import AdminUser
from routes.main_routes import main_bp
from routes.auth_routes import auth_bp
from routes.api_routes import api_bp
from routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__, static_folder='statics')

    # Configuration
    # Uses DATABASE_URL environment variable, defaults to a local postgres DB
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost/aisancekalonji'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key')

    # Initialize database
    db.init_app(app)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'admin.login'
    login_manager.login_message = "Veuillez vous connecter pour accéder à cette page."
    login_manager.login_message_category = "error"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return AdminUser.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app

if __name__ == '__main__':
    app = create_app()
    # In production, use a production WSGI server instead of app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
