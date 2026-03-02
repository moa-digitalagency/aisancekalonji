import os
import sys

# Ajouter le répertoire parent au path pour pouvoir importer l'application
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import create_app
from models.base import db
from models.portfolio import PortfolioItem
from sqlalchemy.exc import SQLAlchemyError

def init_demo_portfolio():
    app = create_app()

    with app.app_context():
        try:
            print("Nettoyage des réalisations existantes dans le portfolio...")
            # Vider la table pour éviter les doublons lors de l'exécution multiple
            PortfolioItem.query.delete()
            db.session.commit()

            print("Création des réalisations (portfolio) avec le support multilingue (10 langues)...")

            # Définition des éléments du portfolio à insérer
            items_to_insert = [
                {
                    "title": {"fr": "Centre Lithiase Tshatshi", "en": "Centre Lithiase Tshatshi", "es": "Centre Lithiase Tshatshi", "pt": "Centre Lithiase Tshatshi", "it": "Centre Lithiase Tshatshi", "de": "Centre Lithiase Tshatshi", "ar": "Centre Lithiase Tshatshi", "zh": "Centre Lithiase Tshatshi", "ja": "Centre Lithiase Tshatshi", "ko": "Centre Lithiase Tshatshi"},
                    "description": {"fr": "Conception du portail du Centre m\u00e9dical de recherche et de prise en charge sp\u00e9cialis\u00e9e de la lithiase urinaire.", "en": "Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "es": "[ES] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "pt": "[PT] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "it": "[IT] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "de": "[DE] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "ar": "[AR] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "zh": "[ZH] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "ja": "[JA] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis.", "ko": "[KO] Design of the portal for the Medical Center for Research and Specialized Care of Urinary Lithiasis."},
                    "icon_class": "fa-heartbeat",
                    "color_class": "blue-500",
                    "link": "https://centrelithiasetshatshi.com",
                    "order": 0
                },
                {
                    "title": {"fr": "J'ai Besoin d'Aide", "en": "J'ai Besoin d'Aide", "es": "J'ai Besoin d'Aide", "pt": "J'ai Besoin d'Aide", "it": "J'ai Besoin d'Aide", "de": "J'ai Besoin d'Aide", "ar": "J'ai Besoin d'Aide", "zh": "J'ai Besoin d'Aide", "ja": "J'ai Besoin d'Aide", "ko": "J'ai Besoin d'Aide"},
                    "description": {"fr": "Plateforme de soutien aux victimes dot\u00e9e d'un chat IA (SolangeBot) pour l'assistance rapide.", "en": "Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "es": "[ES] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "pt": "[PT] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "it": "[IT] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "de": "[DE] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "ar": "[AR] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "zh": "[ZH] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "ja": "[JA] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance.", "ko": "[KO] Victim support platform featuring an AI chat (SolangeBot) for rapid assistance."},
                    "icon_class": "fa-hands-helping",
                    "color_class": "pink-500",
                    "link": "https://jaibesoindaide.org",
                    "order": 10
                },
                {
                    "title": {"fr": "LaCyberConfiance", "en": "LaCyberConfiance", "es": "LaCyberConfiance", "pt": "LaCyberConfiance", "it": "LaCyberConfiance", "de": "LaCyberConfiance", "ar": "LaCyberConfiance", "zh": "LaCyberConfiance", "ja": "LaCyberConfiance", "ko": "LaCyberConfiance"},
                    "description": {"fr": "Portail d\u00e9di\u00e9 \u00e0 la sensibilisation \u00e0 l'hygi\u00e8ne num\u00e9rique, audits et protection des donn\u00e9es.", "en": "Portal dedicated to digital hygiene awareness, audits, and data protection.", "es": "[ES] Portal dedicated to digital hygiene awareness, audits, and data protection.", "pt": "[PT] Portal dedicated to digital hygiene awareness, audits, and data protection.", "it": "[IT] Portal dedicated to digital hygiene awareness, audits, and data protection.", "de": "[DE] Portal dedicated to digital hygiene awareness, audits, and data protection.", "ar": "[AR] Portal dedicated to digital hygiene awareness, audits, and data protection.", "zh": "[ZH] Portal dedicated to digital hygiene awareness, audits, and data protection.", "ja": "[JA] Portal dedicated to digital hygiene awareness, audits, and data protection.", "ko": "[KO] Portal dedicated to digital hygiene awareness, audits, and data protection."},
                    "icon_class": "fa-shield-alt",
                    "color_class": "blue-600",
                    "link": "https://cyberconfiance.com",
                    "order": 20
                },
                {
                    "title": {"fr": "Eric Hajjar", "en": "Eric Hajjar", "es": "Eric Hajjar", "pt": "Eric Hajjar", "it": "Eric Hajjar", "de": "Eric Hajjar", "ar": "Eric Hajjar", "zh": "Eric Hajjar", "ja": "Eric Hajjar", "ko": "Eric Hajjar"},
                    "description": {"fr": "Conception d'un site vitrine et portfolio professionnel personnalis\u00e9 pour le Dr Eric Hajjar \u00e0 Marrakech.", "en": "Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "es": "[ES] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "pt": "[PT] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "it": "[IT] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "de": "[DE] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "ar": "[AR] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "zh": "[ZH] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "ja": "[JA] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech.", "ko": "[KO] Design of a showcase site and personalized professional portfolio for Dr. Eric Hajjar in Marrakech."},
                    "icon_class": "fa-user-tie",
                    "color_class": "amber-500",
                    "link": "https://erichajjar.com",
                    "order": 30
                },
                {
                    "title": {"fr": "Ntanga", "en": "Ntanga", "es": "Ntanga", "pt": "Ntanga", "it": "Ntanga", "de": "Ntanga", "ar": "Ntanga", "zh": "Ntanga", "ja": "Ntanga", "ko": "Ntanga"},
                    "description": {"fr": "Conception d'un site vitrine et portfolio professionnel personnalis\u00e9 pour le Prof. Jean de Dieu Ntita Ntanga du PDDDRC.", "en": "Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "es": "[ES] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "pt": "[PT] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "it": "[IT] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "de": "[DE] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "ar": "[AR] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "zh": "[ZH] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "ja": "[JA] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC.", "ko": "[KO] Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of PDDDRC."},
                    "icon_class": "fa-shopping-bag",
                    "color_class": "orange-500",
                    "link": "https://ntanga.com",
                    "order": 40
                },
                {
                    "title": {"fr": "TFA ASBL", "en": "TFA ASBL", "es": "TFA ASBL", "pt": "TFA ASBL", "it": "TFA ASBL", "de": "TFA ASBL", "ar": "TFA ASBL", "zh": "TFA ASBL", "ja": "TFA ASBL", "ko": "TFA ASBL"},
                    "description": {"fr": "D\u00e9veloppement de l'\u00e9cosyst\u00e8me num\u00e9rique institutionnel pour l'Association Sans But Lucratif TFA.", "en": "Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "es": "[ES] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "pt": "[PT] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "it": "[IT] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "de": "[DE] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "ar": "[AR] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "zh": "[ZH] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "ja": "[JA] Development of the institutional digital ecosystem for the Non-Profit Organization TFA.", "ko": "[KO] Development of the institutional digital ecosystem for the Non-Profit Organization TFA."},
                    "icon_class": "fa-globe-africa",
                    "color_class": "emerald-500",
                    "link": "https://tfa-asbl.org",
                    "order": 50
                },
                {
                    "title": {"fr": "Shabaka InnovLab", "en": "Shabaka InnovLab", "es": "Shabaka InnovLab", "pt": "Shabaka InnovLab", "it": "Shabaka InnovLab", "de": "Shabaka InnovLab", "ar": "Shabaka InnovLab", "zh": "Shabaka InnovLab", "ja": "Shabaka InnovLab", "ko": "Shabaka InnovLab"},
                    "description": {"fr": "Incubateur technologique et laboratoire d'innovation orient\u00e9 vers la R&D et l'Intelligence Artificielle.", "en": "Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "es": "[ES] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "pt": "[PT] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "it": "[IT] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "de": "[DE] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "ar": "[AR] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "zh": "[ZH] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "ja": "[JA] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence.", "ko": "[KO] Technological incubator and innovation laboratory oriented towards R&D and Artificial Intelligence."},
                    "icon_class": "fa-flask",
                    "color_class": "purple-500",
                    "link": "https://shabakainnovlab.com",
                    "order": 60
                },
                {
                    "title": {"fr": "ClipFlow", "en": "ClipFlow", "es": "ClipFlow", "pt": "ClipFlow", "it": "ClipFlow", "de": "ClipFlow", "ar": "ClipFlow", "zh": "ClipFlow", "ja": "ClipFlow", "ko": "ClipFlow"},
                    "description": {"fr": "Outil SaaS de traitement vid\u00e9o permettant de d\u00e9couper, fusionner et extraire du contenu m\u00e9dia.", "en": "SaaS video processing tool for cutting, merging, and extracting media content.", "es": "[ES] SaaS video processing tool for cutting, merging, and extracting media content.", "pt": "[PT] SaaS video processing tool for cutting, merging, and extracting media content.", "it": "[IT] SaaS video processing tool for cutting, merging, and extracting media content.", "de": "[DE] SaaS video processing tool for cutting, merging, and extracting media content.", "ar": "[AR] SaaS video processing tool for cutting, merging, and extracting media content.", "zh": "[ZH] SaaS video processing tool for cutting, merging, and extracting media content.", "ja": "[JA] SaaS video processing tool for cutting, merging, and extracting media content.", "ko": "[KO] SaaS video processing tool for cutting, merging, and extracting media content."},
                    "icon_class": "fa-video",
                    "color_class": "indigo-500",
                    "link": "https://clipflow.site",
                    "order": 70
                },
                {
                    "title": {"fr": "Shabaka AdScreen", "en": "Shabaka AdScreen", "es": "Shabaka AdScreen", "pt": "Shabaka AdScreen", "it": "Shabaka AdScreen", "de": "Shabaka AdScreen", "ar": "Shabaka AdScreen", "zh": "Shabaka AdScreen", "ja": "Shabaka AdScreen", "ko": "Shabaka AdScreen"},
                    "description": {"fr": "Plateforme AdTech avanc\u00e9e de r\u00e9servation et de gestion d'\u00e9crans publicitaires (DOOH).", "en": "Advanced AdTech platform for booking and managing advertising screens (DOOH).", "es": "[ES] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "pt": "[PT] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "it": "[IT] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "de": "[DE] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "ar": "[AR] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "zh": "[ZH] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "ja": "[JA] Advanced AdTech platform for booking and managing advertising screens (DOOH).", "ko": "[KO] Advanced AdTech platform for booking and managing advertising screens (DOOH)."},
                    "icon_class": "fa-tv",
                    "color_class": "cyan-500",
                    "link": "https://shabaka-adscreen.com",
                    "order": 80
                },
                {
                    "title": {"fr": "Disparus.org", "en": "Disparus.org", "es": "Disparus.org", "pt": "Disparus.org", "it": "Disparus.org", "de": "Disparus.org", "ar": "Disparus.org", "zh": "Disparus.org", "ja": "Disparus.org", "ko": "Disparus.org"},
                    "description": {"fr": "Plateforme associative et communautaire facilitant les recherches de personnes port\u00e9es disparues.", "en": "Associative and community platform facilitating searches for missing persons.", "es": "[ES] Associative and community platform facilitating searches for missing persons.", "pt": "[PT] Associative and community platform facilitating searches for missing persons.", "it": "[IT] Associative and community platform facilitating searches for missing persons.", "de": "[DE] Associative and community platform facilitating searches for missing persons.", "ar": "[AR] Associative and community platform facilitating searches for missing persons.", "zh": "[ZH] Associative and community platform facilitating searches for missing persons.", "ja": "[JA] Associative and community platform facilitating searches for missing persons.", "ko": "[KO] Associative and community platform facilitating searches for missing persons."},
                    "icon_class": "fa-search",
                    "color_class": "red-500",
                    "link": "https://disparus.org",
                    "order": 90
                },
                {
                    "title": {"fr": "Shabaka Invest Group", "en": "Shabaka Invest Group", "es": "Shabaka Invest Group", "pt": "Shabaka Invest Group", "it": "Shabaka Invest Group", "de": "Shabaka Invest Group", "ar": "Shabaka Invest Group", "zh": "Shabaka Invest Group", "ja": "Shabaka Invest Group", "ko": "Shabaka Invest Group"},
                    "description": {"fr": "Vitrine num\u00e9rique et corporative pour un groupe d'investissement financier \u00e0 forte valeur ajout\u00e9e.", "en": "Digital and corporate showcase for a high value-added financial investment group.", "es": "[ES] Digital and corporate showcase for a high value-added financial investment group.", "pt": "[PT] Digital and corporate showcase for a high value-added financial investment group.", "it": "[IT] Digital and corporate showcase for a high value-added financial investment group.", "de": "[DE] Digital and corporate showcase for a high value-added financial investment group.", "ar": "[AR] Digital and corporate showcase for a high value-added financial investment group.", "zh": "[ZH] Digital and corporate showcase for a high value-added financial investment group.", "ja": "[JA] Digital and corporate showcase for a high value-added financial investment group.", "ko": "[KO] Digital and corporate showcase for a high value-added financial investment group."},
                    "icon_class": "fa-chart-pie",
                    "color_class": "green-500",
                    "link": "https://shabakainvestgroup.com",
                    "order": 100
                },
                {
                    "title": {"fr": "Urgence Gabon", "en": "Urgence Gabon", "es": "Urgence Gabon", "pt": "Urgence Gabon", "it": "Urgence Gabon", "de": "Urgence Gabon", "ar": "Urgence Gabon", "zh": "Urgence Gabon", "ja": "Urgence Gabon", "ko": "Urgence Gabon"},
                    "description": {"fr": "Portail d\u00e9di\u00e9 \u00e0 l'assistance rapide, aux urgences m\u00e9dicales et aux secours sur le territoire gabonais.", "en": "Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "es": "[ES] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "pt": "[PT] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "it": "[IT] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "de": "[DE] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "ar": "[AR] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "zh": "[ZH] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "ja": "[JA] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory.", "ko": "[KO] Portal dedicated to rapid assistance, medical emergencies, and rescue in the Gabonese territory."},
                    "icon_class": "fa-ambulance",
                    "color_class": "rose-500",
                    "link": "https://urgencegabon.com",
                    "order": 110
                },
                {
                    "title": {"fr": "Taalentio", "en": "Taalentio", "es": "Taalentio", "pt": "Taalentio", "it": "Taalentio", "de": "Taalentio", "ar": "Taalentio", "zh": "Taalentio", "ja": "Taalentio", "ko": "Taalentio"},
                    "description": {"fr": "Plateforme innovante de mise en relation B2B/B2C, d\u00e9di\u00e9e au recrutement et aux Ressources Humaines.", "en": "Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "es": "[ES] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "pt": "[PT] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "it": "[IT] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "de": "[DE] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "ar": "[AR] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "zh": "[ZH] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "ja": "[JA] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources.", "ko": "[KO] Innovative B2B/B2C matchmaking platform dedicated to recruitment and Human Resources."},
                    "icon_class": "fa-users",
                    "color_class": "violet-500",
                    "link": "https://taalentio.com",
                    "order": 120
                },
                {
                    "title": {"fr": "Villa \u00e0 Vendre Marrakech", "en": "Villa \u00e0 Vendre Marrakech", "es": "Villa \u00e0 Vendre Marrakech", "pt": "Villa \u00e0 Vendre Marrakech", "it": "Villa \u00e0 Vendre Marrakech", "de": "Villa \u00e0 Vendre Marrakech", "ar": "Villa \u00e0 Vendre Marrakech", "zh": "Villa \u00e0 Vendre Marrakech", "ja": "Villa \u00e0 Vendre Marrakech", "ko": "Villa \u00e0 Vendre Marrakech"},
                    "description": {"fr": "Site d'annonces immobili\u00e8res premium, centr\u00e9 sur la vente de villas de luxe \u00e0 Marrakech.", "en": "Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "es": "[ES] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "pt": "[PT] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "it": "[IT] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "de": "[DE] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "ar": "[AR] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "zh": "[ZH] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "ja": "[JA] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech.", "ko": "[KO] Premium real estate classifieds site, focused on the sale of luxury villas in Marrakech."},
                    "icon_class": "fa-home",
                    "color_class": "stone-500",
                    "link": "https://villaavendremarrakech.com",
                    "order": 130
                },
                {
                    "title": {"fr": "Transfert Space", "en": "Transfert Space", "es": "Transfert Space", "pt": "Transfert Space", "it": "Transfert Space", "de": "Transfert Space", "ar": "Transfert Space", "zh": "Transfert Space", "ja": "Transfert Space", "ko": "Transfert Space"},
                    "description": {"fr": "Micro web app de mise en relation pour le transfert d'argent dite peer to peer, de personne \u00e0 personne.", "en": "Micro web app for peer-to-peer money transfer matchmaking.", "es": "[ES] Micro web app for peer-to-peer money transfer matchmaking.", "pt": "[PT] Micro web app for peer-to-peer money transfer matchmaking.", "it": "[IT] Micro web app for peer-to-peer money transfer matchmaking.", "de": "[DE] Micro web app for peer-to-peer money transfer matchmaking.", "ar": "[AR] Micro web app for peer-to-peer money transfer matchmaking.", "zh": "[ZH] Micro web app for peer-to-peer money transfer matchmaking.", "ja": "[JA] Micro web app for peer-to-peer money transfer matchmaking.", "ko": "[KO] Micro web app for peer-to-peer money transfer matchmaking."},
                    "icon_class": "fa-cloud-upload-alt",
                    "color_class": "sky-500",
                    "link": "https://transfert.space",
                    "order": 140
                },
            ]

            # Insertion dans la base de données
            for item_data in items_to_insert:
                new_item = PortfolioItem(
                    title=item_data["title"],
                    description=item_data["description"],
                    icon_class=item_data["icon_class"],
                    color_class=item_data["color_class"],
                    link=item_data["link"],
                    order=item_data["order"],
                    is_active=True
                )
                db.session.add(new_item)

            db.session.commit()
            print("Les réalisations du portfolio ont été initialisées avec succès dans la base de données !")

        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Une erreur base de données est survenue : {e}")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur est survenue lors de l'initialisation du portfolio : {e}")

if __name__ == "__main__":
    init_demo_portfolio()
