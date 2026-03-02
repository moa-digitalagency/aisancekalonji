import os
from dotenv import load_dotenv
from main import create_app
from models.base import db
from models.portfolio import PortfolioItem

def init_demo_portfolio():
    load_dotenv()

    # Initialize the Flask app using the same config as the main application
    app = create_app()

    with app.app_context():
        try:
            print("Nettoyage des réalisations existantes dans le portfolio...")
            # Safely clear the existing portfolio items
            PortfolioItem.query.delete()

            print("Création des réalisations (portfolio) avec le support multilingue (10 langues)...")

            # Définition des éléments du portfolio avec les clés: 'fr', 'en', 'es', 'pt', 'it', 'de', 'ar', 'zh', 'ja', 'ko'
            items = [
                {
                    "title": {
                        "fr": "Centre Lithiase Tshatshi",
                        "en": "Lithiase Tshatshi Center",
                        "es": "Centro Lithiase Tshatshi",
                        "pt": "Centro Lithiase Tshatshi",
                        "it": "Centro Lithiase Tshatshi",
                        "de": "Lithiase Tshatshi Zentrum",
                        "ar": "مركز ليثياس تشاتشي",
                        "zh": "Lithiase Tshatshi中心",
                        "ja": "Lithiase Tshatshiセンター",
                        "ko": "Lithiase Tshatshi 센터"
                    },
                    "description": {
                        "fr": "Création d'une plateforme médicale spécialisée et déploiement d'écosystèmes technologiques résilients pour le secteur de la santé.",
                        "en": "Creation of a specialized medical platform and deployment of resilient technological ecosystems for the healthcare sector.",
                        "es": "Creación de una plataforma médica especializada y despliegue de ecosistemas tecnológicos resilientes para el sector salud.",
                        "pt": "Criação de uma plataforma médica especializada e implementação de ecossistemas tecnológicos resilientes para o setor de saúde.",
                        "it": "Creazione di una piattaforma medica specializzata e implementazione di ecosistemi tecnologici resilienti per il settore sanitario.",
                        "de": "Schaffung einer spezialisierten medizinischen Plattform und Einsatz widerstandsfähiger technologischer Ökosysteme für den Gesundheitssektor.",
                        "ar": "إنشاء منصة طبية متخصصة ونشر أنظمة تكنولوجية مرنة لقطاع الرعاية الصحية.",
                        "zh": "创建专业医疗平台并为医疗保健部门部署有弹性的技术生态系统。",
                        "ja": "専門的な医療プラットフォームの構築と、ヘルスケア分野における回復力のある技術エコシステムの展開。",
                        "ko": "의료 부문을 위한 전문 의료 플랫폼 구축 및 탄력적인 기술 생태계 배포."
                    },
                    "link": "#",
                    "icon_class": "fas fa-hospital",
                    "color_class": "blue-500",
                    "order": 1
                },
                {
                    "title": {
                        "fr": "J'ai Besoin d'Aide",
                        "en": "I Need Help",
                        "es": "Necesito Ayuda",
                        "pt": "Preciso de Ajuda",
                        "it": "Ho Bisogno di Aiuto",
                        "de": "Ich Brauche Hilfe",
                        "ar": "أحتاج مساعدة",
                        "zh": "我需要帮助",
                        "ja": "助けが必要です",
                        "ko": "도움이 필요합니다"
                    },
                    "description": {
                        "fr": "Développement d'une plateforme à fort impact communautaire dédiée à la mise en relation et à l'entraide sociale.",
                        "en": "Development of a high-impact community platform dedicated to networking and social mutual aid.",
                        "es": "Desarrollo de una plataforma comunitaria de alto impacto dedicada a la conexión y la ayuda mutua social.",
                        "pt": "Desenvolvimento de uma plataforma comunitária de alto impacto dedicada ao networking e ajuda mútua social.",
                        "it": "Sviluppo di una piattaforma comunitaria ad alto impatto dedicata al networking e all'aiuto reciproco sociale.",
                        "de": "Entwicklung einer hochwirksamen Community-Plattform für Vernetzung und soziale gegenseitige Hilfe.",
                        "ar": "تطوير منصة مجتمعية ذات تأثير عالٍ مخصصة للتواصل والمساعدة المتبادلة الاجتماعية.",
                        "zh": "开发一个致力于社交网络和社会互助的高影响力社区平台。",
                        "ja": "ネットワーキングと社会的な相互支援に特化した、影響力の高いコミュニティプラットフォームの開発。",
                        "ko": "네트워킹과 사회적 상호 지원에 전념하는 영향력 있는 커뮤니티 플랫폼 개발."
                    },
                    "link": "#",
                    "icon_class": "fas fa-hands-helping",
                    "color_class": "yellow-500",
                    "order": 2
                },
                {
                    "title": {
                        "fr": "LaCyberConfiance",
                        "en": "LaCyberConfiance",
                        "es": "LaCyberConfiance",
                        "pt": "LaCyberConfiance",
                        "it": "LaCyberConfiance",
                        "de": "LaCyberConfiance",
                        "ar": "LaCyberConfiance",
                        "zh": "LaCyberConfiance",
                        "ja": "LaCyberConfiance",
                        "ko": "LaCyberConfiance"
                    },
                    "description": {
                        "fr": "Direction de la plateforme de sensibilisation. Création du Vade-mecum de LaCyberConfiance, réalisation d'audits cyber et R&D d'outils d'IA pour la détection de menaces.",
                        "en": "Direction of the awareness platform. Creation of the LaCyberConfiance Vade-mecum, conducting cyber audits and R&D of AI tools for threat detection.",
                        "es": "Dirección de la plataforma de concientización. Creación del Vademécum de LaCyberConfiance, realización de auditorías cibernéticas e I+D de herramientas de IA para la detección de amenazas.",
                        "pt": "Direção da plataforma de conscientização. Criação do Vade-mécum da LaCyberConfiance, realização de auditorias cibernéticas e P&D de ferramentas de IA para detecção de ameaças.",
                        "it": "Direzione della piattaforma di sensibilizzazione. Creazione del Vademecum di LaCyberConfiance, conduzione di audit informatici e R&S di strumenti di intelligenza artificiale per il rilevamento delle minacce.",
                        "de": "Leitung der Sensibilisierungsplattform. Erstellung des LaCyberConfiance Vademecums, Durchführung von Cyber-Audits und F&E von KI-Tools zur Bedrohungserkennung.",
                        "ar": "إدارة منصة التوعية. إنشاء دليل LaCyberConfiance، وإجراء التدقيقات السيبرانية والبحث والتطوير لأدوات الذكاء الاصطناعي لاكتشاف التهديدات.",
                        "zh": "管理意识平台。创建 LaCyberConfiance Vade-mecum，进行网络审计并研发用于威胁检测的 AI 工具。",
                        "ja": "認識向上プラットフォームの指揮。LaCyberConfiance Vade-mecumの作成、サイバー監査の実施、および脅威検出のためのAIツールの研究開発。",
                        "ko": "인식 플랫폼의 방향. LaCyberConfiance Vade-mecum 작성, 사이버 감사 수행 및 위협 탐지를 위한 AI 도구의 연구 개발."
                    },
                    "link": "https://www.cyberconfiance.com",
                    "icon_class": "fas fa-shield-halved",
                    "color_class": "emerald-500",
                    "order": 3
                }
            ]

            for item_data in items:
                new_item = PortfolioItem(
                    title=item_data["title"],
                    description=item_data["description"],
                    link=item_data["link"],
                    icon_class=item_data["icon_class"],
                    color_class=item_data["color_class"],
                    order=item_data.get("order", 0)
                )
                db.session.add(new_item)

            # Commit the changes securely
            db.session.commit()
            print("Les réalisations du portfolio ont été initialisées avec succès dans la base de données !")

        except Exception as e:
            # Rollback in case of an error to keep the database in a consistent state
            db.session.rollback()
            print(f"Une erreur est survenue lors de l'initialisation du portfolio : {e}")

if __name__ == '__main__':
    init_demo_portfolio()