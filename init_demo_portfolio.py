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
                    "title": {"fr": "Centre Lithiase Tshatshi", "en": "Tshatshi Lithiasis Center", "es": "Centro de Litiasis Tshatshi", "pt": "Centro de Litíase Tshatshi", "it": "Centro Litiasi Tshatshi", "de": "Tshatshi Lithiasis Center", "ar": "مركز تشاتشي للتحصي", "zh": "Tshatshi 结石病中心", "ja": "ツァシ結石症センター", "ko": "차트시 결석증 센터"},
                    "description": {"fr": "Conception du portail du Centre m\u00e9dical de recherche et de prise en charge sp\u00e9cialis\u00e9e de la lithiase urinaire.", "en": "Design of the portal for the Medical Center for research and specialized treatment of urolithiasis.", "es": "Diseño del portal del Centro Médico de investigación y tratamiento especializado de la urolitiasis.", "pt": "Desenho do portal do Centro Médico para pesquisa e tratamento especializado de urolitíase.", "it": "Progettazione del portale del Centro Medico per la ricerca e la cura specialistica dell'urolitiasi.", "de": "Gestaltung des Portals für das Medizinische Zentrum für Forschung und spezialisierte Behandlung von Urolithiasis.", "ar": "تصميم البوابة الإلكترونية للمركز الطبي للأبحاث والعلاج التخصصي لتحصي البول.", "zh": "设计医疗中心的门户网站，用于尿石症的研究和专业治疗。", "ja": "尿路結石症の研究と専門治療を行う医療センターのポータルのデザイン。", "ko": "요로결석증의 연구 및 전문 치료를 위한 의료 센터 포털 설계."},
                    "icon_class": "fa-heartbeat",
                    "color_class": "blue-500",
                    "link": "https://centrelithiasetshatshi.com",
                    "order": 0
                },
                {
                    "title": {"fr": "J'ai Besoin d'Aide", "en": "I need help", "es": "necesito ayuda", "pt": "Eu preciso de ajuda", "it": "Ho bisogno di aiuto", "de": "Ich brauche Hilfe", "ar": "انا بحاجة الى مساعدة", "zh": "我需要帮助", "ja": "私は助けが必要です", "ko": "도움이 필요해요"},
                    "description": {"fr": "Plateforme de soutien aux victimes dot\u00e9e d'un chat IA (SolangeBot) pour l'assistance rapide.", "en": "Victim support platform with AI chat (SolangeBot) for rapid assistance.", "es": "Plataforma de apoyo a las víctimas con chat AI (SolangeBot) para una asistencia rápida.", "pt": "Plataforma de suporte a vítimas com chat AI (SolangeBot) para atendimento rápido.", "it": "Piattaforma di supporto alle vittime con chat AI (SolangeBot) per un'assistenza rapida.", "de": "Opferhilfeplattform mit KI-Chat (SolangeBot) für schnelle Hilfe.", "ar": "منصة دعم الضحايا مع دردشة الذكاء الاصطناعي (SolangeBot) للمساعدة السريعة.", "zh": "具有人工智能聊天功能的受害者支持平台 (SolangeBot) 可提供快速帮助。", "ja": "AI チャット (SolangeBot) を備えた被害者サポート プラットフォームで迅速な支援を実現します。", "ko": "신속한 지원을 위한 AI 채팅(SolangeBot)을 갖춘 피해자 지원 플랫폼입니다."},
                    "icon_class": "fa-hands-helping",
                    "color_class": "pink-500",
                    "link": "https://jaibesoindaide.org",
                    "order": 10
                },
                {
                    "title": {"fr": "LaCyberConfiance", "en": "LaCyberConfidence", "es": "LaCyberConfianza", "pt": "LaCyberConfiança", "it": "LaCyberConfidence", "de": "LaCyberConfidence", "ar": "LaCyberConfidence", "zh": "网络信心", "ja": "ラサイバーコンフィデンス", "ko": "라사이버컨피던스"},
                    "description": {"fr": "Portail d\u00e9di\u00e9 \u00e0 la sensibilisation \u00e0 l'hygi\u00e8ne num\u00e9rique, audits et protection des donn\u00e9es.", "en": "Portal dedicated to raising awareness of digital hygiene, audits and data protection.", "es": "Portal dedicado a la sensibilización sobre higiene digital, auditorías y protección de datos.", "pt": "Portal dedicado à sensibilização para a higiene digital, auditorias e proteção de dados.", "it": "Portale dedicato alla sensibilizzazione sull'igiene digitale, sugli audit e sulla protezione dei dati.", "de": "Portal zur Sensibilisierung für digitale Hygiene, Audits und Datenschutz.", "ar": "بوابة مخصصة لزيادة الوعي بالنظافة الرقمية والتدقيق وحماية البيانات.", "zh": "致力于提高数字卫生、审计和数据保护意识的门户网站。", "ja": "デジタル衛生、監査、データ保護の意識を高めることに特化したポータル。", "ko": "디지털 위생, 감사 및 데이터 보호에 대한 인식을 높이는 데 전념하는 포털입니다."},
                    "icon_class": "fa-shield-alt",
                    "color_class": "blue-600",
                    "link": "https://cyberconfiance.com",
                    "order": 20
                },
                {
                    "title": {"fr": "Eric Hajjar", "en": "Eric Hajjar", "es": "Eric Hajar", "pt": "Eric Hajjar", "it": "Eric Hajjar", "de": "Eric Hajjar", "ar": "اريك حجار", "zh": "埃里克·哈贾尔", "ja": "エリック・ハッジャール", "ko": "에릭 하자르"},
                    "description": {"fr": "Conception d'un site vitrine et portfolio professionnel personnalis\u00e9 pour le Dr Eric Hajjar \u00e0 Marrakech.", "en": "Design of a showcase site and personalized professional portfolio for Dr Eric Hajjar in Marrakech.", "es": "Diseño de un sitio escaparate y un portafolio profesional personalizado para el Dr. Eric Hajjar en Marrakech.", "pt": "Design de um site de vitrine e portfólio profissional personalizado para o Dr. Eric Hajjar em Marrakech.", "it": "Progettazione di un sito vetrina e portfolio professionale personalizzato per il dottor Eric Hajjar a Marrakech.", "de": "Gestaltung einer Showcase-Site und eines personalisierten professionellen Portfolios für Dr. Eric Hajjar in Marrakesch.", "ar": "تصميم موقع عرض ومحفظة مهنية شخصية للدكتور إريك حجار في مراكش.", "zh": "为马拉喀什的 Eric Hajjar 博士设计展示网站和个性化专业作品集。", "ja": "マラケシュのエリック・ハジャール博士のためのショーケースサイトとパーソナライズされた専門ポートフォリオのデザイン。", "ko": "마라케시의 Eric Hajjar 박사를 위한 쇼케이스 사이트 및 맞춤형 전문 포트폴리오 디자인."},
                    "icon_class": "fa-user-tie",
                    "color_class": "amber-500",
                    "link": "https://erichajjar.com",
                    "order": 30
                },
                {
                    "title": {"fr": "Ntanga", "en": "Ntanga", "es": "ntanga", "pt": "Ntanga", "it": "Ntanga", "de": "Ntanga", "ar": "نتانغا", "zh": "恩坦加", "ja": "ンタンガ", "ko": "은탕가"},
                    "description": {"fr": "Conception d'un site vitrine et portfolio professionnel personnalis\u00e9 pour le Prof. Jean de Dieu Ntita Ntanga du PDDDRC.", "en": "Design of a showcase site and personalized professional portfolio for Prof. Jean de Dieu Ntita Ntanga of the PDDDRC.", "es": "Diseño de un sitio escaparate y portafolio profesional personalizado para el Prof. Jean de Dieu Ntita Ntanga del PDDDRC.", "pt": "Design de site de vitrine e portfólio profissional personalizado para o Prof. Jean de Dieu Ntita Ntanga do PDDDRC.", "it": "Progettazione di un sito vetrina e portfolio professionale personalizzato per il Prof. Jean de Dieu Ntita Ntanga del PDDDRC.", "de": "Gestaltung einer Showcase-Site und eines personalisierten professionellen Portfolios für Prof. Jean de Dieu Ntita Ntanga vom PDDDRC.", "ar": "تصميم موقع عرض ومحفظة مهنية شخصية للبروفيسور جان دي ديو نتيتا نتانغا من PDDDRC.", "zh": "为 PDDDRC 的 Jean de Dieu Ntita Ntanga 教授设计展示网站和个性化专业作品集。", "ja": "PDDDRC の Jean de Dieu Ntita Ntanga 教授向けのショーケース サイトとパーソナライズされたプロフェッショナル ポートフォリオのデザイン。", "ko": "PDDDRC의 Jean de Dieu Ntita Ntanga 교수를 위한 쇼케이스 사이트 및 맞춤형 전문 포트폴리오 디자인."},
                    "icon_class": "fa-shopping-bag",
                    "color_class": "orange-500",
                    "link": "https://ntanga.com",
                    "order": 40
                },
                {
                    "title": {"fr": "TFA ASBL", "en": "TFA ASBL", "es": "TFA ASBL", "pt": "TFA ASBL", "it": "TFAASBL", "de": "TFA ASBL", "ar": "تفا ASBL", "zh": "反式脂肪酸ASBL", "ja": "TFA ASBL", "ko": "TFA ASBL"},
                    "description": {"fr": "D\u00e9veloppement de l'\u00e9cosyst\u00e8me num\u00e9rique institutionnel pour l'Association Sans But Lucratif TFA.", "en": "Development of the institutional digital ecosystem for the Non-profit Association TFA.", "es": "Desarrollo del ecosistema digital institucional para la Asociación sin fines de lucro TFA.", "pt": "Desenvolvimento do ecossistema digital institucional da Associação Sem Fins Lucrativos TFA.", "it": "Sviluppo dell'ecosistema digitale istituzionale per l'Associazione no-profit TFA.", "de": "Entwicklung des institutionellen digitalen Ökosystems für den gemeinnützigen Verein TFA.", "ar": "تطوير النظام البيئي الرقمي المؤسسي لجمعية TFA غير الربحية.", "zh": "为非营利协会 TFA 开发机构数字生态系统。", "ja": "非営利団体 TFA のための組織デジタル エコシステムの開発。", "ko": "비영리 협회 TFA를 위한 기관 디지털 생태계 개발."},
                    "icon_class": "fa-globe-africa",
                    "color_class": "emerald-500",
                    "link": "https://tfa-asbl.org",
                    "order": 50
                },
                {
                    "title": {"fr": "Shabaka InnovLab", "en": "Shabaka InnovLab", "es": "Shabaka InnovLab", "pt": "Shabaka InnovLab", "it": "Shabaka InnovLab", "de": "Shabaka InnovLab", "ar": "شبكة إنوف لاب", "zh": "沙巴卡创新实验室", "ja": "シャバカ・イノベーションラボ", "ko": "샤바카 InnovLab"},
                    "description": {"fr": "Incubateur technologique et laboratoire d'innovation orient\u00e9 vers la R&D et l'Intelligence Artificielle.", "en": "Technological incubator and innovation laboratory focused on R&D and Artificial Intelligence.", "es": "Incubadora tecnológica y laboratorio de innovación centrado en I+D+i e Inteligencia Artificial.", "pt": "Incubadora tecnológica e laboratório de inovação com foco em P&D e Inteligência Artificial.", "it": "Incubatore tecnologico e laboratorio di innovazione focalizzato su ricerca e sviluppo e intelligenza artificiale.", "de": "Technologischer Inkubator und Innovationslabor mit Schwerpunkt auf Forschung und Entwicklung sowie künstlicher Intelligenz.", "ar": "حاضنة تكنولوجية ومختبر ابتكار يركز على البحث والتطوير والذكاء الاصطناعي.", "zh": "专注于研发和人工智能的技术孵化器和创新实验室。", "ja": "研究開発と人工知能に焦点を当てた技術インキュベーターおよびイノベーション研究所。", "ko": "R&D 및 인공 지능에 중점을 둔 기술 인큐베이터 및 혁신 연구소입니다."},
                    "icon_class": "fa-flask",
                    "color_class": "purple-500",
                    "link": "https://shabakainnovlab.com",
                    "order": 60
                },
                {
                    "title": {"fr": "ClipFlow", "en": "ClipFlow", "es": "ClipFlow", "pt": "ClipFlow", "it": "ClipFlow", "de": "ClipFlow", "ar": "ClipFlow", "zh": "剪辑流", "ja": "クリップフロー", "ko": "ClipFlow"},
                    "description": {"fr": "Outil SaaS de traitement vid\u00e9o permettant de d\u00e9couper, fusionner et extraire du contenu m\u00e9dia.", "en": "SaaS video processing tool for cutting, merging and extracting media content.", "es": "Herramienta de procesamiento de vídeo SaaS para cortar, fusionar y extraer contenido multimedia.", "pt": "Ferramenta de processamento de vídeo SaaS para cortar, mesclar e extrair conteúdo de mídia.", "it": "Strumento di elaborazione video SaaS per tagliare, unire ed estrarre contenuti multimediali.", "de": "SaaS-Videoverarbeitungstool zum Schneiden, Zusammenführen und Extrahieren von Medieninhalten.", "ar": "أداة معالجة الفيديو SaaS لقص محتوى الوسائط ودمجها واستخراجها.", "zh": "用于剪切、合并和提取媒体内容的 SaaS 视频处理工具。", "ja": "メディア コンテンツを切り取り、結合、抽出するための SaaS ビデオ処理ツール。", "ko": "미디어 콘텐츠 자르기, 병합 및 추출을 위한 SaaS 비디오 처리 도구입니다."},
                    "icon_class": "fa-video",
                    "color_class": "indigo-500",
                    "link": "https://clipflow.site",
                    "order": 70
                },
                {
                    "title": {"fr": "Shabaka AdScreen", "en": "Shabaka AdScreen", "es": "Pantalla publicitaria de Shabaka", "pt": "Tela de anúncios Shabaka", "it": "Schermata pubblicitaria Shabaka", "de": "Shabaka AdScreen", "ar": "شاشة إعلانات الشبكة", "zh": "沙巴卡广告屏幕", "ja": "シャバカ広告スクリーン", "ko": "샤바카 광고화면"},
                    "description": {"fr": "Plateforme AdTech avanc\u00e9e de r\u00e9servation et de gestion d'\u00e9crans publicitaires (DOOH).", "en": "Advanced AdTech platform for booking and managing advertising screens (DOOH).", "es": "Plataforma AdTech avanzada para reserva y gestión de pantallas publicitarias (DOOH).", "pt": "Plataforma AdTech avançada para reserva e gerenciamento de telas publicitárias (DOOH).", "it": "Piattaforma AdTech avanzata per la prenotazione e la gestione degli schermi pubblicitari (DOOH).", "de": "Fortschrittliche AdTech-Plattform zur Buchung und Verwaltung von Werbebildschirmen (DOOH).", "ar": "منصة AdTech المتقدمة لحجز وإدارة الشاشات الإعلانية (DOOH).", "zh": "用于预订和管理广告屏幕 (DOOH) 的先进 AdTech 平台。", "ja": "広告画面を予約および管理するための高度な AdTech プラットフォーム (DOOH)。", "ko": "광고 화면 예약 및 관리(DOOH)를 위한 고급 AdTech 플랫폼입니다."},
                    "icon_class": "fa-tv",
                    "color_class": "cyan-500",
                    "link": "https://shabaka-adscreen.com",
                    "order": 80
                },
                {
                    "title": {"fr": "Disparus.org", "en": "Disappeared.org", "es": "Desaparecido.org", "pt": "Desaparecido.org", "it": "Disappeared.org", "de": "Disappeared.org", "ar": "Disappeared.org", "zh": "消失.org", "ja": "失踪.org", "ko": "Disappeared.org"},
                    "description": {"fr": "Plateforme associative et communautaire facilitant les recherches de personnes port\u00e9es disparues.", "en": "Associative and community platform facilitating searches for missing people.", "es": "Plataforma asociativa y comunitaria que facilita la búsqueda de personas desaparecidas.", "pt": "Plataforma associativa e comunitária que facilita buscas por pessoas desaparecidas.", "it": "Piattaforma associativa e comunitaria che facilita le ricerche di persone scomparse.", "de": "Assoziative und Community-Plattform, die die Suche nach vermissten Personen erleichtert.", "ar": "منصة جمعوية ومجتمعية تسهل عمليات البحث عن الأشخاص المفقودين.", "zh": "促进寻找失踪人员的关联和社区平台。", "ja": "行方不明者の捜索を容易にする連想的およびコミュニティーのプラットフォーム。", "ko": "실종자 수색을 촉진하는 협회 및 커뮤니티 플랫폼입니다."},
                    "icon_class": "fa-search",
                    "color_class": "red-500",
                    "link": "https://disparus.org",
                    "order": 90
                },
                {
                    "title": {"fr": "Shabaka Invest Group", "en": "Shabaka Invest Group", "es": "Grupo Shabaka Invest", "pt": "Grupo Shabaka Invest", "it": "Gruppo Shabaka Invest", "de": "Shabaka Invest Group", "ar": "مجموعة شبكة للاستثمار", "zh": "沙巴卡投资集团", "ja": "シャバカ・インベスト・グループ", "ko": "샤바카 인베스트 그룹"},
                    "description": {"fr": "Vitrine num\u00e9rique et corporative pour un groupe d'investissement financier \u00e0 forte valeur ajout\u00e9e.", "en": "Digital and corporate showcase for a high value-added financial investment group.", "es": "Escaparate digital y corporativo para un grupo inversor financiero de alto valor añadido.", "pt": "Vitrine digital e corporativa de um grupo de investimentos financeiros de alto valor agregado.", "it": "Vetrina digitale e aziendale per un gruppo di investimento finanziario ad alto valore aggiunto.", "de": "Digitales und unternehmerisches Schaufenster für eine Finanzinvestitionsgruppe mit hohem Mehrwert.", "ar": "عرض رقمي ومؤسسي لمجموعة استثمارية مالية ذات قيمة مضافة عالية.", "zh": "高附加值金融投资集团的数字和企业展示。", "ja": "高付加価値金融投資グループ向けのデジタルおよび企業のショーケース。", "ko": "고부가가치 금융투자그룹을 위한 디지털 및 기업 쇼케이스입니다."},
                    "icon_class": "fa-chart-pie",
                    "color_class": "green-500",
                    "link": "https://shabakainvestgroup.com",
                    "order": 100
                },
                {
                    "title": {"fr": "Urgence Gabon", "en": "Emergency Gabon", "es": "Emergencia Gabón", "pt": "Emergência Gabão", "it": "Emergenza Gabon", "de": "Notfall Gabun", "ar": "غابون الطوارئ", "zh": "紧急情况 加蓬", "ja": "ガボン緊急事態", "ko": "긴급 가봉"},
                    "description": {"fr": "Portail d\u00e9di\u00e9 \u00e0 l'assistance rapide, aux urgences m\u00e9dicales et aux secours sur le territoire gabonais.", "en": "Portal dedicated to rapid assistance, medical emergencies and relief on Gabonese territory.", "es": "Portal dedicado a la asistencia rápida, las emergencias médicas y el socorro en territorio gabonés.", "pt": "Portal dedicado à assistência rápida, emergências médicas e socorro em território gabonês.", "it": "Portale dedicato all'assistenza rapida, alle emergenze mediche e ai soccorsi sul territorio gabonese.", "de": "Portal für schnelle Hilfe, medizinische Notfälle und Hilfe auf gabunischem Gebiet.", "ar": "بوابة مخصصة للمساعدة السريعة وحالات الطوارئ الطبية والإغاثة على الأراضي الغابونية.", "zh": "致力于加蓬领土上的快速援助、医疗紧急情况和救济的门户网站。", "ja": "ガボン領土における迅速な支援、医療緊急事態、救援に特化したポータル。", "ko": "가봉 영토의 신속한 지원, 의료 응급 상황 및 구호를 전담하는 포털입니다."},
                    "icon_class": "fa-ambulance",
                    "color_class": "rose-500",
                    "link": "https://urgencegabon.com",
                    "order": 110
                },
                {
                    "title": {"fr": "Taalentio", "en": "Taalentio", "es": "Taalentio", "pt": "Taalentio", "it": "Taalentio", "de": "Taalentio", "ar": "تالنتيو", "zh": "塔伦蒂奥", "ja": "タレンティオ", "ko": "탈렌티오"},
                    "description": {"fr": "Plateforme innovante de mise en relation B2B/B2C, d\u00e9di\u00e9e au recrutement et aux Ressources Humaines.", "en": "Innovative B2B/B2C networking platform, dedicated to recruitment and Human Resources.", "es": "Innovadora plataforma de networking B2B/B2C, dedicada al reclutamiento y Recursos Humanos.", "pt": "Plataforma inovadora de networking B2B/B2C, dedicada ao recrutamento e Recursos Humanos.", "it": "Innovativa piattaforma di networking B2B/B2C, dedicata al recruitment e alle Risorse Umane.", "de": "Innovative B2B/B2C-Netzwerkplattform für Personalbeschaffung und Personalwesen.", "ar": "منصة مبتكرة لشبكات B2B/B2C، مخصصة للتوظيف والموارد البشرية.", "zh": "创新的B2B/B2C网络平台，致力于招聘和人力资源。", "ja": "採用と人事に特化した革新的な B2B/B2C ネットワーキング プラットフォーム。", "ko": "채용 및 인사 전용의 혁신적인 B2B/B2C 네트워킹 플랫폼입니다."},
                    "icon_class": "fa-users",
                    "color_class": "violet-500",
                    "link": "https://taalentio.com",
                    "order": 120
                },
                {
                    "title": {"fr": "Villa \u00e0 Vendre Marrakech", "en": "Villa for Sale Marrakech", "es": "Villa en Venta Marrakech", "pt": "Moradia à venda Marraquexe", "it": "Villa in Vendita Marrakech", "de": "Villa zum Verkauf Marrakesch", "ar": "فيلا للبيع مراكش", "zh": "马拉喀什待售别墅", "ja": "販売中のヴィラ マラケシュ", "ko": "판매용 빌라 마라케시"},
                    "description": {"fr": "Site d'annonces immobili\u00e8res premium, centr\u00e9 sur la vente de villas de luxe \u00e0 Marrakech.", "en": "Premium real estate ads site, focused on the sale of luxury villas in Marrakech.", "es": "Sitio de anuncios inmobiliarios premium, centrado en la venta de villas de lujo en Marrakech.", "pt": "Site de anúncios imobiliários premium, focado na venda de vilas de luxo em Marrakech.", "it": "Sito di annunci immobiliari premium, focalizzato sulla vendita di ville di lusso a Marrakech.", "de": "Premium-Immobilienanzeigenseite, die sich auf den Verkauf von Luxusvillen in Marrakesch konzentriert.", "ar": "موقع إعلانات عقارية متميز، يركز على بيع الفلل الفاخرة في مراكش.", "zh": "优质房地产广告网站，专注于马拉喀什豪华别墅的销售。", "ja": "マラケシュの高級ヴィラの販売に焦点を当てたプレミアム不動産広告サイト。", "ko": "마라케시의 고급 빌라 매매에 초점을 맞춘 프리미엄 부동산 광고 사이트입니다."},
                    "icon_class": "fa-home",
                    "color_class": "stone-500",
                    "link": "https://villaavendremarrakech.com",
                    "order": 130
                },
                {
                    "title": {"fr": "Transfert Space", "en": "Space Transfer", "es": "Transferencia espacial", "pt": "Transferência Espacial", "it": "Trasferimento spaziale", "de": "Weltraumtransfer", "ar": "نقل الفضاء", "zh": "空间转移", "ja": "空間転移", "ko": "공간이동"},
                    "description": {"fr": "Micro web app de mise en relation pour le transfert d'argent dite peer to peer, de personne \u00e0 personne.", "en": "Micro web connection app for so-called peer to peer money transfer, from person to person.", "es": "Aplicación de microconexión web para la llamada transferencia de dinero de igual a igual, de persona a persona.", "pt": "Aplicativo de micro conexão web para a chamada transferência de dinheiro ponto a ponto, de pessoa para pessoa.", "it": "App di micro connessione web per il cosiddetto trasferimento di denaro peer to peer, da persona a persona.", "de": "Mikro-Webverbindungs-App für den sogenannten Peer-to-Peer-Geldtransfer von Person zu Person.", "ar": "تطبيق اتصال ويب صغير لما يسمى بتحويل الأموال من نظير إلى نظير، من شخص إلى آخر.", "zh": "微型网络连接应用程序，用于所谓的点对点汇款，人与人之间。", "ja": "個人から個人へのいわゆるピアツーピア送金のためのマイクロウェブ接続アプリ。", "ko": "개인 간, 소위 P2P 송금을 위한 마이크로 웹 연결 앱입니다."},
                    "icon_class": "fa-cloud-upload-alt",
                    "color_class": "sky-500",
                    "link": "https://transfert.space",
                    "order": 140
                },
                {
                    "title": {"fr": "AI Journalist Manager", "en": "AI Journalist Manager", "es": "Gerente de Periodismo de IA", "pt": "Gerente de jornalista de IA", "it": "Responsabile giornalisti dell'AI", "de": "KI-Journalistenmanager", "ar": "مدير صحفي بالذكاء الاصطناعي", "zh": "人工智能记者经理", "ja": "AIジャーナリストマネージャー", "ko": "AI 저널리스트 매니저"},
                    "description": {"fr": "Plateforme de veille strat\u00e9gique multilingue int\u00e9grant le clonage vocal (ElevenLabs) et la validation factuelle en temps r\u00e9el (Perplexity).", "en": "Multilingual business intelligence platform integrating voice cloning (ElevenLabs) and real-time factual validation (Perplexity).", "es": "Plataforma de inteligencia empresarial multilingüe que integra clonación de voz (ElevenLabs) y validación factual en tiempo real (Perplexity).", "pt": "Plataforma multilíngue de business intelligence integrando clonagem de voz (ElevenLabs) e validação factual em tempo real (Perplexity).", "it": "Piattaforma di business intelligence multilingue che integra la clonazione vocale (ElevenLabs) e la convalida fattuale in tempo reale (Perplexity).", "de": "Mehrsprachige Business-Intelligence-Plattform, die Sprachklonen (ElevenLabs) und Faktenvalidierung in Echtzeit (Perplexity) integriert.", "ar": "منصة ذكاء أعمال متعددة اللغات تدمج استنساخ الصوت (ElevenLabs) والتحقق من صحة الحقائق في الوقت الفعلي (Perplexity).", "zh": "集成语音克隆（ElevenLabs）和实时事实验证（Perplexity）的多语言商业智能平台。", "ja": "音声クローン (イレブンラボ) とリアルタイムの事実検証 (Perplexity) を統合した多言語ビジネス インテリジェンス プラットフォーム。", "ko": "음성 복제(ElevenLabs)와 실시간 사실 검증(Perplexity)을 통합한 다국어 비즈니스 인텔리전스 플랫폼입니다."},
                    "icon_class": "fa-robot",
                    "color_class": "indigo-600",
                    "link": "#",
                    "order": 150
                },
                {
                    "title": {"fr": "Busconnect", "en": "Busconnect", "es": "Conexión de bus", "pt": "Conexão de ônibus", "it": "Busconnect", "de": "Busverbindung", "ar": "Busconnect", "zh": "总线连接", "ja": "バスコネクト", "ko": "버스커넥트"},
                    "description": {"fr": "Solution d'optimisation de la mobilit\u00e9 urbaine via l'analyse des flux pour une gestion pr\u00e9dictive des transports publics.", "en": "Urban mobility optimization solution via flow analysis for predictive management of public transport.", "es": "Solución de optimización de la movilidad urbana mediante análisis de flujos para la gestión predictiva del transporte público.", "pt": "Solução de otimização de mobilidade urbana via análise de fluxo para gestão preditiva de transporte público.", "it": "Soluzione di ottimizzazione della mobilità urbana tramite analisi dei flussi per la gestione predittiva del trasporto pubblico.", "de": "Lösung zur Optimierung der städtischen Mobilität mittels Flussanalyse für das prädiktive Management des öffentlichen Verkehrs.", "ar": "حل تحسين التنقل الحضري من خلال تحليل التدفق للإدارة التنبؤية لوسائل النقل العام.", "zh": "通过流量分析进行城市交通优化解决方案，以实现公共交通的预测管理。", "ja": "公共交通機関の予測管理のための流れ分析による都市モビリティ最適化ソリューション。", "ko": "대중교통 예측 관리를 위한 흐름 분석을 통한 도시 이동성 최적화 솔루션입니다."},
                    "icon_class": "fa-bus",
                    "color_class": "yellow-500",
                    "link": "#",
                    "order": 160
                },
                {
                    "title": {"fr": "Algorithme AAPCMLU", "en": "AAPCMLU algorithm", "es": "Algoritmo AAPCMLU", "pt": "Algoritmo AAPCMLU", "it": "Algoritmo AAPCMLU", "de": "AAPCMLU-Algorithmus", "ar": "خوارزمية أبكملو", "zh": "AAPCMLU算法", "ja": "AAPCMLU アルゴリズム", "ko": "AAPCMLU 알고리즘"},
                    "description": {"fr": "Moteur d'inf\u00e9rence propri\u00e9taire (Dr. KALONJI) corr\u00e9lant imagerie et biologie pour classifier et pr\u00e9venir les lithiases urinaires.", "en": "Proprietary inference engine (Dr. KALONJI) correlating imaging and biology to classify and prevent urolithiasis.", "es": "Motor de inferencia patentado (Dr. KALONJI) que correlaciona imágenes y biología para clasificar y prevenir la urolitiasis.", "pt": "Mecanismo de inferência proprietário (Dr. KALONJI) correlacionando imagens e biologia para classificar e prevenir a urolitíase.", "it": "Motore di inferenza proprietario (Dr. KALONJI) che correla imaging e biologia per classificare e prevenire l'urolitiasi.", "de": "Proprietäre Inferenz-Engine (Dr. KALONJI), die Bildgebung und Biologie in Beziehung setzt, um Urolithiasis zu klassifizieren und zu verhindern.", "ar": "محرك استدلال خاص (دكتور كالونجي) يربط بين التصوير وعلم الأحياء لتصنيف تحص البول والوقاية منه.", "zh": "专有推理引擎（KALONJI 博士）将成像和生物学关联起来，以对尿石症进行分类和预防。", "ja": "独自の推論エンジン (Dr. KALONJI) は、画像と生物学を相関させて尿路結石を分類し、予防します。", "ko": "요로결석증을 분류하고 예방하기 위해 영상과 생물학을 상호 연관시키는 독점 추론 엔진(Dr. KALONJI)."},
                    "icon_class": "fa-dna",
                    "color_class": "blue-400",
                    "link": "#",
                    "order": 170
                },
                {
                    "title": {"fr": "Shabaka Safety", "en": "Shabaka Safety", "es": "Seguridad Shabaka", "pt": "Segurança Shabaka", "it": "Sicurezza Shabaka", "de": "Shabaka-Sicherheit", "ar": "سلامة الشبكة", "zh": "沙巴卡安全", "ja": "シャバカセーフティ", "ko": "샤바카 안전"},
                    "description": {"fr": "Solution IA (hardware/software) analysant les flux vid\u00e9o pour d\u00e9tecter le non-port des \u00c9quipements de Protection Individuelle (EPI).", "en": "AI solution (hardware/software) analyzing video streams to detect non-wearing of Personal Protective Equipment (PPE).", "es": "Solución de IA (hardware/software) que analiza transmisiones de vídeo para detectar la falta de uso de equipos de protección personal (EPP).", "pt": "Solução de IA (hardware/software) que analisa streams de vídeo para detectar o não uso de Equipamentos de Proteção Individual (EPI).", "it": "Soluzione AI (hardware/software) che analizza i flussi video per rilevare il mancato utilizzo dei Dispositivi di Protezione Individuale (DPI).", "de": "KI-Lösung (Hardware/Software) analysiert Videostreams, um das Nichttragen persönlicher Schutzausrüstung (PSA) zu erkennen.", "ar": "يقوم حل الذكاء الاصطناعي (الأجهزة/البرامج) بتحليل تدفقات الفيديو لاكتشاف عدم ارتداء معدات الحماية الشخصية (PPE).", "zh": "AI 解决方案（硬件/软件）分析视频流以检测是否佩戴个人防护装备 (PPE)。", "ja": "ビデオ ストリームを分析して個人用保護具 (PPE) の未着用を検出する AI ソリューション (ハードウェア/ソフトウェア)。", "ko": "비디오 스트림을 분석하여 개인보호장비(PPE) 미착용을 감지하는 AI 솔루션(하드웨어/소프트웨어)입니다."},
                    "icon_class": "fa-hard-hat",
                    "color_class": "orange-600",
                    "link": "#",
                    "order": 180
                },
                {
                    "title": {"fr": "GEC (Gestion \u00c9lectronique des Courriels)", "en": "GEC (Electronic Email Management)", "es": "GEC (Gestión Electrónica de Correo Electrónico)", "pt": "GEC (Gerenciamento de E-mail Eletrônico)", "it": "GEC (Gestione della posta elettronica)", "de": "GEC (Elektronisches E-Mail-Management)", "ar": "GEC (إدارة البريد الإلكتروني الإلكترونية)", "zh": "GEC（电子电子邮件管理）", "ja": "GEC (電子メール管理)", "ko": "GEC(전자 이메일 관리)"},
                    "description": {"fr": "Syst\u00e8me fluidifiant les circuits de d\u00e9cision via une tra\u00e7abilit\u00e9 immuable des \u00e9changes administratifs et officiels.", "en": "System streamlining decision-making circuits via immutable traceability of administrative and official exchanges.", "es": "Sistema que agiliza los circuitos de toma de decisiones mediante la trazabilidad inmutable de los intercambios administrativos y oficiales.", "pt": "Sistema que agiliza os circuitos de tomada de decisão através da rastreabilidade imutável das trocas administrativas e oficiais.", "it": "Sistema di snellimento dei circuiti decisionali attraverso la tracciabilità immutabile degli scambi amministrativi e ufficiali.", "de": "System zur Straffung der Entscheidungswege durch unveränderliche Rückverfolgbarkeit des administrativen und offiziellen Austauschs.", "ar": "نظام لتبسيط دوائر اتخاذ القرار من خلال التتبع الثابت للتبادلات الإدارية والرسمية.", "zh": "系统通过行政和官方交流的不可变可追溯性简化决策流程。", "ja": "行政および公的取引の不変のトレーサビリティを通じて意思決定回路を合理化するシステム。", "ko": "행정 및 공식 교류의 불변 추적성을 통해 의사결정 회로를 간소화하는 시스템입니다."},
                    "icon_class": "fa-envelope-open-text",
                    "color_class": "teal-500",
                    "link": "#",
                    "order": 190
                },
                {
                    "title": {"fr": "AfrikaID", "en": "AfrikaID", "es": "África ID", "pt": "ÁfricaID", "it": "AfricaID", "de": "AfrikaID", "ar": "AfrikaID", "zh": "非洲ID", "ja": "アフリカID", "ko": "아프리카ID"},
                    "description": {"fr": "Solution KYC avanc\u00e9e prot\u00e9geant contre l'usurpation d'identit\u00e9 via l'analyse de hash MRZ et la v\u00e9rification biom\u00e9trique.", "en": "Advanced KYC solution protecting against identity theft via MRZ hash analysis and biometric verification.", "es": "Solución KYC avanzada que protege contra el robo de identidad mediante análisis de hash MRZ y verificación biométrica.", "pt": "Solução KYC avançada que protege contra roubo de identidade por meio de análise de hash MRZ e verificação biométrica.", "it": "Soluzione KYC avanzata che protegge dal furto di identità tramite analisi hash MRZ e verifica biometrica.", "de": "Fortschrittliche KYC-Lösung zum Schutz vor Identitätsdiebstahl durch MRZ-Hash-Analyse und biometrische Überprüfung.", "ar": "حل KYC المتقدم للحماية من سرقة الهوية عبر تحليل تجزئة MRZ والتحقق البيومتري.", "zh": "先进的 KYC 解决方案通过 MRZ 哈希分析和生物识别验证防止身份盗窃。", "ja": "MRZ ハッシュ分析と生体認証による個人情報の盗難を防ぐ高度な KYC ソリューション。", "ko": "MRZ 해시 분석 및 생체 인증을 통해 신원 도용을 방지하는 고급 KYC 솔루션입니다."},
                    "icon_class": "fa-id-card",
                    "color_class": "fuchsia-500",
                    "link": "#",
                    "order": 200
                },
                {
                    "title": {"fr": "SGI-GP (GoPass)", "en": "SGI-GP (GoPass)", "es": "SGI-GP (GoPass)", "pt": "SGI-GP (GoPass)", "it": "SGI-GP (GoPass)", "de": "SGI-GP (GoPass)", "ar": "SGI-GP (جو باس)", "zh": "SGI-GP (GoPass)", "ja": "SGI-GP (ゴーパス)", "ko": "SGI-GP(고패스)"},
                    "description": {"fr": "Syst\u00e8me Zero Trust maximisant les recettes a\u00e9roportuaires par la r\u00e9conciliation infaillible des manifestes de vol et des flux financiers.", "en": "Zero Trust system maximizing airport revenues through the foolproof reconciliation of flight manifests and financial flows.", "es": "Sistema Zero Trust que maximiza los ingresos del aeropuerto mediante la conciliación infalible de manifiestos de vuelo y flujos financieros.", "pt": "Sistema Zero Trust que maximiza as receitas aeroportuárias através da reconciliação infalível de manifestos de voo e fluxos financeiros.", "it": "Sistema Zero Trust che massimizza i ricavi aeroportuali attraverso la riconciliazione infallibile tra manifesti di volo e flussi finanziari.", "de": "Zero-Trust-System zur Maximierung der Flughafeneinnahmen durch den narrensicheren Abgleich von Flugmanifesten und Finanzströmen.", "ar": "يعمل نظام Zero Trust على زيادة إيرادات المطار إلى الحد الأقصى من خلال التوفيق المضمون بين بيانات الرحلات الجوية والتدفقات المالية.", "zh": "零信任系统通过航班舱单和资金流的万无一失的核对来最大化机场收入。", "ja": "ゼロトラスト システムは、フライトマニフェストと財務フローの確実な調整を通じて空港収益を最大化します。", "ko": "항공편 적하목록과 금융 흐름의 완벽한 조화를 통해 공항 수익을 극대화하는 제로 트러스트 시스템입니다."},
                    "icon_class": "fa-plane-departure",
                    "color_class": "sky-600",
                    "link": "#",
                    "order": 210
                },
                {
                    "title": {"fr": "Gestion Chantiers", "en": "Site management", "es": "Gestión del sitio", "pt": "Gerenciamento de sites", "it": "Gestione del sito", "de": "Site-Management", "ar": "إدارة الموقع", "zh": "现场管理", "ja": "サイト管理", "ko": "사이트 관리"},
                    "description": {"fr": "Outil de contr\u00f4le financier en temps r\u00e9el \u00e9radiquant le gaspillage via le pointage automatis\u00e9 et la tra\u00e7abilit\u00e9 par preuve visuelle (Bellari).", "en": "Real-time financial control tool eradicating waste via automated tallying and traceability by visual proof (Bellari).", "es": "Herramienta de control financiero en tiempo real que erradica el desperdicio mediante conteo automatizado y trazabilidad mediante prueba visual (Bellari).", "pt": "Ferramenta de controle financeiro em tempo real que erradica desperdícios por meio de contagem automatizada e rastreabilidade por prova visual (Bellari).", "it": "Strumento di controllo finanziario in tempo reale che elimina gli sprechi tramite conteggio automatizzato e tracciabilità tramite prova visiva (Bellari).", "de": "Echtzeit-Finanzkontrolltool zur Vermeidung von Verschwendung durch automatisierte Zählung und Rückverfolgbarkeit durch visuelle Beweise (Bellari).", "ar": "أداة للرقابة المالية في الوقت الفعلي تعمل على القضاء على الهدر من خلال الفرز الآلي وإمكانية التتبع عن طريق الإثبات البصري (بيلاري).", "zh": "实时财务控制工具通过视觉证明的自动计数和可追溯性消除浪费（Bellari）。", "ja": "自動集計と視覚的証明によるトレーサビリティにより無駄を排除するリアルタイム財務管理ツール (Bellari)。", "ko": "시각적 증거를 통한 자동화된 집계 및 추적성을 통해 낭비를 근절하는 실시간 재무 관리 도구입니다(Bellari)."},
                    "icon_class": "fa-tools",
                    "color_class": "amber-600",
                    "link": "#",
                    "order": 220
                },
                {
                    "title": {"fr": "Shabaka Syndic", "en": "Shabaka Trustee", "es": "Fideicomisario de Shabaka", "pt": "Administrador de Shabaka", "it": "Fiduciario di Shabaka", "de": "Shabaka-Treuhänder", "ar": "أمين الشبكة", "zh": "沙巴卡受托人", "ja": "シャバカ管理委員", "ko": "샤바카 수탁자"},
                    "description": {"fr": "Plateforme collaborative digitalisant appels de fonds et quittances pour une transparence totale de la gestion des copropri\u00e9t\u00e9s.", "en": "Collaborative platform digitalizing fundraising calls and receipts for total transparency in the management of co-ownerships.", "es": "Plataforma colaborativa que digitaliza las convocatorias y recibos de recaudación de fondos para una total transparencia en la gestión de copropiedades.", "pt": "Plataforma colaborativa que digitaliza chamadas e recibos de arrecadação para total transparência na gestão de copropriedades.", "it": "Piattaforma collaborativa che digitalizza bandi e ricevute di raccolta fondi per una totale trasparenza nella gestione delle comproprietà.", "de": "Kollaborative Plattform zur Digitalisierung von Spendenaufrufen und -belegen für völlige Transparenz bei der Verwaltung von Miteigentümern.", "ar": "منصة تعاونية تعمل على رقمنة مكالمات وإيصالات جمع التبرعات لتحقيق الشفافية الكاملة في إدارة الملكية المشتركة.", "zh": "协作平台将筹款电话和收据数字化，以实现共同所有权管理的完全透明。", "ja": "共同所有権の管理における完全な透明性を実現するために、募金活動の電話と領収書をデジタル化する共同プラットフォーム。", "ko": "공동 소유권 관리의 완전한 투명성을 위해 모금 요청 및 영수증을 디지털화하는 협업 플랫폼입니다."},
                    "icon_class": "fa-building",
                    "color_class": "emerald-600",
                    "link": "#",
                    "order": 230
                },
                {
                    "title": {"fr": "Shabaka IMMO", "en": "Shabaka IMMO", "es": "Shabaka IMMO", "pt": "Shabaka IMMO", "it": "Shabaka IMMO", "de": "Shabaka IMMO", "ar": "شبكة IMMO", "zh": "沙巴卡IMMO", "ja": "シャバカIMMO", "ko": "샤바카 IMMO"},
                    "description": {"fr": "Solution synchronisant reconnaissance d'image et traitement vocal pour g\u00e9n\u00e9rer instantan\u00e9ment des rapports de visite immobili\u00e8re.", "en": "Solution synchronizing image recognition and voice processing to instantly generate real estate visit reports.", "es": "Solución que sincroniza el reconocimiento de imágenes y el procesamiento de voz para generar instantáneamente informes de visitas inmobiliarias.", "pt": "Solução que sincroniza reconhecimento de imagem e processamento de voz para geração instantânea de relatórios de visitas imobiliárias.", "it": "Soluzione che sincronizza il riconoscimento delle immagini e l'elaborazione vocale per generare istantaneamente report sulle visite immobiliari.", "de": "Lösung, die Bilderkennung und Sprachverarbeitung synchronisiert, um sofort Berichte über Immobilienbesuche zu erstellen.", "ar": "حل لمزامنة التعرف على الصور ومعالجة الصوت لإنشاء تقارير الزيارات العقارية على الفور.", "zh": "解决方案同步图像识别和语音处理，即时生成房地产访问报告。", "ja": "画像認識と音声処理を同期し、不動産訪問レポートを瞬時に生成するソリューション。", "ko": "이미지 인식과 음성 처리를 동기화하여 부동산 방문 보고서를 즉시 생성하는 솔루션입니다."},
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
