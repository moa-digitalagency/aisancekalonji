import os
from flask import Flask
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
from models.base import db

# Import models so SQLAlchemy knows about them
import models

def init_db():
    load_dotenv()
    app = Flask(__name__)

    # Configure the PostgreSQL database URI
    # In a real app, this should come from environment variables or a config file
    # For now, we will use a dummy URI that allows us to at least verify the context creation locally
    # e.g., using sqlite for a syntax test or requiring the user to provide correct env variables

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:password@localhost/aisancekalonji'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        try:
            # Create all tables
            print("Creating database tables...")
            db.create_all()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error creating tables (they might already exist): {e}")

        # Create admin user if it doesn't exist
        print("Checking admin user...")
        admin_username = os.environ.get('ADMIN_USERNAME')
        admin_password = os.environ.get('ADMIN_PASSWORD')

        if not admin_username or not admin_password:
            print("WARNING: ADMIN_USERNAME or ADMIN_PASSWORD not found in environment variables.")
            print("Falling back to default credentials. Please change them immediately in production.")
            admin_username = admin_username or 'admin'
            admin_password = admin_password or 'admin123'

        try:
            admin_user = models.AdminUser.query.filter_by(username=admin_username).first()
            if not admin_user:
                print(f"Creating admin user '{admin_username}'...")
                hashed_password = generate_password_hash(admin_password)
                new_admin = models.AdminUser(username=admin_username, password_hash=hashed_password)
                db.session.add(new_admin)
                db.session.commit()
                print("Admin user created successfully.")
            else:
                print("Admin user already exists.")
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating admin user: {e}")

        # Pre-fill PageImage default values
        print("Checking default page images...")
        default_images = [
            {'section_name': 'hero_light', 'image_url': 'https://i.ibb.co/23nxjv1R/AK-Light.png'},
            {'section_name': 'hero_dark', 'image_url': 'https://i.ibb.co/0RrbS4b1/AK-Dark.png'},
            {'section_name': 'vision', 'image_url': 'https://images.unsplash.com/photo-1531384441138-2736e62e0919?q=80&w=2000&auto=format&fit=crop'},
            {'section_name': 'portrait', 'image_url': 'https://i.ibb.co/N6GMYcy9/Use-my-photo-202511241827.jpg'},
            {'section_name': 'book', 'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=1000&auto=format&fit=crop'}
        ]

        try:
            for img_data in default_images:
                if not models.PageImage.query.filter_by(section_name=img_data['section_name']).first():
                    new_img = models.PageImage(
                        section_name=img_data['section_name'],
                        image_url=img_data['image_url'],
                        is_uploaded=False
                    )
                    db.session.add(new_img)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating default page images: {e}")

        # Pre-fill SeoSetting default values
        print("Checking SEO settings...")
        try:
            if not models.SeoSetting.query.first():
                print("Creating default SEO settings...")
                new_seo = models.SeoSetting(
                    meta_title="Aisance KALONJI | Consultant IA & Cybersécurité",
                    meta_description="15 années d'expertise. Consultant en Transformation Digitale, Intelligence Artificielle et Cybersécurité, je conçois des écosystèmes technologiques résilients pour les entreprises ambitieuses."
                )
                db.session.add(new_seo)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating SEO settings: {e}")

        # Pre-fill BookSection default values
        print("Checking Book section...")
        try:
            if not models.BookSection.query.first():
                print("Creating default Book section...")
                new_book = models.BookSection(
                    title={"fr": "Vade-mecum de la sécurité numérique"},
                    subtitle={"fr": "Aisance Kalonji"},
                    description={"fr": "Un guide essentiel et pratique conçu pour démystifier l'hygiène numérique. À travers cet ouvrage, je partage des stratégies concrètes et des protocoles de sécurité pour protéger les actifs digitaux des entreprises et des particuliers face aux menaces modernes."},
                    cta_link="https://www.cyberconfiance.com",
                    cta_text={"fr": "Obtenir mon exemplaire"},
                    image_url="https://images.unsplash.com/photo-1544947950-fa07a98d237f?q=80&w=1000&auto=format&fit=crop"
                )
                db.session.add(new_book)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating Book section: {e}")

        # Pre-fill Portfolio default values
        print("Checking default portfolio items...")
        try:
            if not models.PortfolioItem.query.first():
                print("Creating default portfolio items...")
                default_portfolio = [
                    models.PortfolioItem(
                        title={"fr": "Centre Lithiase Tshatshi"},
                        description={"fr": "Création d'une plateforme médicale spécialisée et déploiement d'écosystèmes technologiques résilients pour le secteur de la santé."},
                        link="#",
                        icon_class="fas fa-hospital",
                        color_class="blue-500"
                    ),
                    models.PortfolioItem(
                        title={"fr": "J'ai Besoin d'Aide"},
                        description={"fr": "Développement d'une plateforme à fort impact communautaire dédiée à la mise en relation et à l'entraide sociale."},
                        link="#",
                        icon_class="fas fa-hands-helping",
                        color_class="yellow-500"
                    ),
                    models.PortfolioItem(
                        title={"fr": "LaCyberConfiance"},
                        description={"fr": "Direction de la plateforme de sensibilisation. Création du Vade-mecum de LaCyberConfiance, réalisation d'audits cyber et R&D d'outils d'IA pour la détection de menaces."},
                        link="https://www.cyberconfiance.com",
                        icon_class="fas fa-shield-halved",
                        color_class="emerald-500"
                    )
                ]
                for item in default_portfolio:
                    db.session.add(item)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating default portfolio items: {e}")

        # Pre-fill GlobalSetting default values
        print("Checking default global settings...")
        default_global_settings = {
            'logo_type': 'text',
            'logo_text': 'Aisance KALONJI',
            'logo_image_url': '',
            'favicon_url': ''
        }

        try:
            for key, value in default_global_settings.items():
                if not models.GlobalSetting.query.filter_by(key=key).first():
                    new_setting = models.GlobalSetting(key=key, value=value)
                    db.session.add(new_setting)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error checking/creating global settings: {e}")

        print("Database seeding completed.")

if __name__ == '__main__':
    init_db()
