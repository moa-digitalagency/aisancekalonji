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
                {
                    "title": {"fr": "AI Journalist Manager", "en": "AI Journalist Manager", "es": "AI Journalist Manager", "pt": "AI Journalist Manager", "it": "AI Journalist Manager", "de": "AI Journalist Manager", "ar": "AI Journalist Manager", "zh": "AI Journalist Manager", "ja": "AI Journalist Manager", "ko": "AI Journalist Manager"},
                    "description": {"fr": "Plateforme de veille strat\u00e9gique multilingue int\u00e9grant le clonage vocal (ElevenLabs) et la validation factuelle en temps r\u00e9el (Perplexity).", "en": "Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "es": "[ES] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "pt": "[PT] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "it": "[IT] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "de": "[DE] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "ar": "[AR] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "zh": "[ZH] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "ja": "[JA] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "ko": "[KO] Multilingual strategic intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity)."},
                    "icon_class": "fa-robot",
                    "color_class": "indigo-600",
                    "link": "#",
                    "order": 150
                },
                {
                    "title": {"fr": "Busconnect", "en": "Busconnect", "es": "Busconnect", "pt": "Busconnect", "it": "Busconnect", "de": "Busconnect", "ar": "Busconnect", "zh": "Busconnect", "ja": "Busconnect", "ko": "Busconnect"},
                    "description": {"fr": "Solution d'optimisation de la mobilit\u00e9 urbaine via l'analyse des flux pour une gestion pr\u00e9dictive des transports publics.", "en": "Urban mobility optimization solution via flow analysis for predictive management of public transport.", "es": "[ES] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "pt": "[PT] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "it": "[IT] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "de": "[DE] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "ar": "[AR] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "zh": "[ZH] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "ja": "[JA] Urban mobility optimization solution via flow analysis for predictive management of public transport.", "ko": "[KO] Urban mobility optimization solution via flow analysis for predictive management of public transport."},
                    "icon_class": "fa-bus",
                    "color_class": "yellow-500",
                    "link": "#",
                    "order": 160
                },
                {
                    "title": {"fr": "Algorithme AAPCMLU", "en": "Algorithme AAPCMLU", "es": "Algorithme AAPCMLU", "pt": "Algorithme AAPCMLU", "it": "Algorithme AAPCMLU", "de": "Algorithme AAPCMLU", "ar": "Algorithme AAPCMLU", "zh": "Algorithme AAPCMLU", "ja": "Algorithme AAPCMLU", "ko": "Algorithme AAPCMLU"},
                    "description": {"fr": "Moteur d'inf\u00e9rence propri\u00e9taire (Dr. KALONJI) corr\u00e9lant imagerie et biologie pour classifier et pr\u00e9venir les lithiases urinaires.", "en": "Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "es": "[ES] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "pt": "[PT] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "it": "[IT] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "de": "[DE] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "ar": "[AR] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "zh": "[ZH] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "ja": "[JA] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis.", "ko": "[KO] Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urinary lithiasis."},
                    "icon_class": "fa-dna",
                    "color_class": "blue-400",
                    "link": "#",
                    "order": 170
                },
                {
                    "title": {"fr": "Shabaka Safety", "en": "Shabaka Safety", "es": "Shabaka Safety", "pt": "Shabaka Safety", "it": "Shabaka Safety", "de": "Shabaka Safety", "ar": "Shabaka Safety", "zh": "Shabaka Safety", "ja": "Shabaka Safety", "ko": "Shabaka Safety"},
                    "description": {"fr": "Solution IA (hardware/software) analysant les flux vid\u00e9o pour d\u00e9tecter le non-port des \u00c9quipements de Protection Individuelle (EPI).", "en": "AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "es": "[ES] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "pt": "[PT] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "it": "[IT] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "de": "[DE] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "ar": "[AR] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "zh": "[ZH] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "ja": "[JA] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE).", "ko": "[KO] AI solution (hardware/software) analyzing video feeds to detect non-compliance with Personal Protective Equipment (PPE)."},
                    "icon_class": "fa-hard-hat",
                    "color_class": "orange-600",
                    "link": "#",
                    "order": 180
                },
                {
                    "title": {"fr": "GEC (Gestion \u00c9lectronique des Courriels)", "en": "GEC (Gestion \u00c9lectronique des Courriels)", "es": "GEC (Gestion \u00c9lectronique des Courriels)", "pt": "GEC (Gestion \u00c9lectronique des Courriels)", "it": "GEC (Gestion \u00c9lectronique des Courriels)", "de": "GEC (Gestion \u00c9lectronique des Courriels)", "ar": "GEC (Gestion \u00c9lectronique des Courriels)", "zh": "GEC (Gestion \u00c9lectronique des Courriels)", "ja": "GEC (Gestion \u00c9lectronique des Courriels)", "ko": "GEC (Gestion \u00c9lectronique des Courriels)"},
                    "description": {"fr": "Syst\u00e8me fluidifiant les circuits de d\u00e9cision via une tra\u00e7abilit\u00e9 immuable des \u00e9changes administratifs et officiels.", "en": "System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "es": "[ES] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "pt": "[PT] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "it": "[IT] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "de": "[DE] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "ar": "[AR] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "zh": "[ZH] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "ja": "[JA] System streamlining decision circuits via an immutable traceability of administrative and official exchanges.", "ko": "[KO] System streamlining decision circuits via an immutable traceability of administrative and official exchanges."},
                    "icon_class": "fa-envelope-open-text",
                    "color_class": "teal-500",
                    "link": "#",
                    "order": 190
                },
                {
                    "title": {"fr": "AfrikaID", "en": "AfrikaID", "es": "AfrikaID", "pt": "AfrikaID", "it": "AfrikaID", "de": "AfrikaID", "ar": "AfrikaID", "zh": "AfrikaID", "ja": "AfrikaID", "ko": "AfrikaID"},
                    "description": {"fr": "Solution KYC avanc\u00e9e prot\u00e9geant contre l'usurpation d'identit\u00e9 via l'analyse de hash MRZ et la v\u00e9rification biom\u00e9trique.", "en": "Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "es": "[ES] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "pt": "[PT] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "it": "[IT] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "de": "[DE] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "ar": "[AR] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "zh": "[ZH] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "ja": "[JA] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "ko": "[KO] Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification."},
                    "icon_class": "fa-id-card",
                    "color_class": "fuchsia-500",
                    "link": "#",
                    "order": 200
                },
                {
                    "title": {"fr": "SGI-GP (GoPass)", "en": "SGI-GP (GoPass)", "es": "SGI-GP (GoPass)", "pt": "SGI-GP (GoPass)", "it": "SGI-GP (GoPass)", "de": "SGI-GP (GoPass)", "ar": "SGI-GP (GoPass)", "zh": "SGI-GP (GoPass)", "ja": "SGI-GP (GoPass)", "ko": "SGI-GP (GoPass)"},
                    "description": {"fr": "Syst\u00e8me Zero Trust maximisant les recettes a\u00e9roportuaires par la r\u00e9conciliation infaillible des manifestes de vol et des flux financiers.", "en": "Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "es": "[ES] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "pt": "[PT] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "it": "[IT] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "de": "[DE] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "ar": "[AR] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "zh": "[ZH] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "ja": "[JA] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows.", "ko": "[KO] Zero Trust system maximizing airport revenues through infallible reconciliation of flight manifests and financial flows."},
                    "icon_class": "fa-plane-departure",
                    "color_class": "sky-600",
                    "link": "#",
                    "order": 210
                },
                {
                    "title": {"fr": "Gestion Chantiers", "en": "Gestion Chantiers", "es": "Gestion Chantiers", "pt": "Gestion Chantiers", "it": "Gestion Chantiers", "de": "Gestion Chantiers", "ar": "Gestion Chantiers", "zh": "Gestion Chantiers", "ja": "Gestion Chantiers", "ko": "Gestion Chantiers"},
                    "description": {"fr": "Outil de contr\u00f4le financier en temps r\u00e9el \u00e9radiquant le gaspillage via le pointage automatis\u00e9 et la tra\u00e7abilit\u00e9 par preuve visuelle (Bellari).", "en": "Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "es": "[ES] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "pt": "[PT] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "it": "[IT] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "de": "[DE] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "ar": "[AR] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "zh": "[ZH] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "ja": "[JA] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari).", "ko": "[KO] Real-time financial control tool eradicating waste via automated timekeeping and visual proof traceability (Bellari)."},
                    "icon_class": "fa-tools",
                    "color_class": "amber-600",
                    "link": "#",
                    "order": 220
                },
                {
                    "title": {"fr": "Shabaka Syndic", "en": "Shabaka Syndic", "es": "Shabaka Syndic", "pt": "Shabaka Syndic", "it": "Shabaka Syndic", "de": "Shabaka Syndic", "ar": "Shabaka Syndic", "zh": "Shabaka Syndic", "ja": "Shabaka Syndic", "ko": "Shabaka Syndic"},
                    "description": {"fr": "Plateforme collaborative digitalisant appels de fonds et quittances pour une transparence totale de la gestion des copropri\u00e9t\u00e9s.", "en": "Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "es": "[ES] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "pt": "[PT] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "it": "[IT] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "de": "[DE] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "ar": "[AR] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "zh": "[ZH] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "ja": "[JA] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management.", "ko": "[KO] Collaborative platform digitizing fund calls and receipts for total transparency in condominium management."},
                    "icon_class": "fa-building",
                    "color_class": "emerald-600",
                    "link": "#",
                    "order": 230
                },
                {
                    "title": {"fr": "Shabaka IMMO", "en": "Shabaka IMMO", "es": "Shabaka IMMO", "pt": "Shabaka IMMO", "it": "Shabaka IMMO", "de": "Shabaka IMMO", "ar": "Shabaka IMMO", "zh": "Shabaka IMMO", "ja": "Shabaka IMMO", "ko": "Shabaka IMMO"},
                    "description": {"fr": "Solution synchronisant reconnaissance d'image et traitement vocal pour g\u00e9n\u00e9rer instantan\u00e9ment des rapports de visite immobili\u00e8re.", "en": "Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "es": "[ES] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "pt": "[PT] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "it": "[IT] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "de": "[DE] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "ar": "[AR] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "zh": "[ZH] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "ja": "[JA] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "ko": "[KO] Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports."},
                    "icon_class": "fa-key",
                    "color_class": "red-600",
                    "link": "#",
                    "order": 240
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
