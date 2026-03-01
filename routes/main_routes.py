from flask import Blueprint, render_template
from models.setting import GlobalSetting, SeoSetting
from models.page import PageImage
from models.portfolio import PortfolioItem
from models.book import BookSection

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Fetch all global settings as a dictionary
    settings = {s.key: s.value for s in GlobalSetting.query.all()}

    # Fetch SEO settings
    seo = SeoSetting.query.first()

    # Fetch page images as a dictionary mapped by section_name
    page_images = {img.section_name: img for img in PageImage.query.all()}

    # Fetch active portfolio items ordered by 'order'
    portfolio = PortfolioItem.query.filter_by(is_active=True).order_by(PortfolioItem.order.asc()).all()

    # Fetch book section details
    book = BookSection.query.first()

    return render_template('index.html',
                           settings=settings,
                           seo=seo,
                           page_images=page_images,
                           portfolio=portfolio,
                           book=book)

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
