import os
from flask import Flask, render_template, session, request, redirect, url_for
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

    # Multi-language setup
    from utils.i18n import get_translation

    @app.route('/set_lang/<lang_code>')
    def set_lang(lang_code):
        # Validate lang_code based on available files, but we can just set it
        available_langs = ['fr', 'en', 'es', 'pt', 'it', 'de', 'ar', 'zh', 'ja', 'ko']
        if lang_code in available_langs:
            session['lang'] = lang_code
        return redirect(request.referrer or url_for('main.index'))

    @app.context_processor
    def inject_lang():
        lang = session.get('lang', 'fr')

        def t(key):
            return get_translation(lang, key)

        return dict(current_lang=lang, t=t)

    @app.template_filter('fallback_lang')
    def fallback_lang_filter(field_data, lang_code='fr'):
        if isinstance(field_data, dict):
            return field_data.get(lang_code, field_data.get('fr', ''))
        return field_data or ''

    # Register error handlers
    from models.setting import GlobalSetting

    def get_whatsapp_number():
        try:
            whatsapp_setting = GlobalSetting.query.filter_by(key='whatsapp').first()
            number = whatsapp_setting.value if whatsapp_setting and whatsapp_setting.value else os.environ.get('WHATSAPP_NUMBER', '243860493345')
            # Nettoyer le numéro pour le lien wa.me (retirer espaces, +, etc.)
            clean_number = ''.join(filter(str.isdigit, number))
            return clean_number if clean_number else '243860493345'
        except Exception as e:
            # Fallback in case of database error to prevent cascading 500 errors
            number = os.environ.get('WHATSAPP_NUMBER', '243860493345')
            clean_number = ''.join(filter(str.isdigit, number))
            return clean_number if clean_number else '243860493345'


    @app.errorhandler(400)
    def bad_request_error(error):
        return render_template('400.html'), 400

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html', whatsapp_number=get_whatsapp_number()), 403

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html', whatsapp_number=get_whatsapp_number()), 404

    @app.errorhandler(451)
    def unavailable_for_legal_reasons_error(error):
        return render_template('451.html'), 451

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    # In production, use a production WSGI server instead of app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
