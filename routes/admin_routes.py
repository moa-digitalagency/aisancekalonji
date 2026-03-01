import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from models.admin_user import AdminUser
from models.portfolio import PortfolioItem
from models.page import PageImage
from models.base import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = AdminUser.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')

    return render_template('admin/login.html')

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    # Fetch basic stats
    active_portfolio_count = PortfolioItem.query.filter_by(is_active=True).count()
    uploaded_images_count = PageImage.query.filter_by(is_uploaded=True).count()

    return render_template('admin/dashboard.html', active_portfolio_count=active_portfolio_count, uploaded_images_count=uploaded_images_count)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg', 'ico'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_secure_upload(file):
    if file and file.filename != '':
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.static_folder, 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)
            return f"uploads/{filename}"
    return None

@admin_bp.route('/images', methods=['GET', 'POST'])
@login_required
def images():
    images = PageImage.query.all()

    if request.method == 'POST':
        try:
            for image in images:
                file = request.files.get(image.section_name)
                url = request.form.get(image.section_name + '_url')

                if file and file.filename != '':
                    upload_path = handle_secure_upload(file)
                    if upload_path:
                        image.upload_path = upload_path
                        image.is_uploaded = True
                        image.image_url = None
                    else:
                        flash(f'Format de fichier non autorisé ou fichier invalide pour {image.section_name}.', 'error')
                elif url and url.strip() != '':
                    image.image_url = url.strip()
                    image.is_uploaded = False
                    image.upload_path = None

            db.session.commit()
            flash('Images mises à jour avec succès.', 'success')
            return redirect(url_for('admin.images'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    return render_template('admin/images.html', images=images)

@admin_bp.route('/portfolio')
@login_required
def portfolio():
    items = PortfolioItem.query.order_by(PortfolioItem.order.asc()).all()
    return render_template('admin/portfolio.html', items=items)

@admin_bp.route('/portfolio/add', methods=['GET', 'POST'])
@login_required
def portfolio_add():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        link = request.form.get('link')
        icon_class = request.form.get('icon_class')
        color_class = request.form.get('color_class')
        is_active = request.form.get('is_active') == 'on'

        try:
            new_item = PortfolioItem(
                title=title,
                description=description,
                link=link,
                icon_class=icon_class,
                color_class=color_class,
                is_active=is_active
            )
            db.session.add(new_item)
            db.session.commit()
            flash('Projet ajouté avec succès.', 'success')
            return redirect(url_for('admin.portfolio'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    return render_template('admin/portfolio_form.html', item=None)

@admin_bp.route('/portfolio/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def portfolio_edit(id):
    item = PortfolioItem.query.get_or_404(id)

    if request.method == 'POST':
        item.title = request.form.get('title')
        item.description = request.form.get('description')
        item.link = request.form.get('link')
        item.icon_class = request.form.get('icon_class')
        item.color_class = request.form.get('color_class')
        item.is_active = request.form.get('is_active') == 'on'

        try:
            db.session.commit()
            flash('Projet modifié avec succès.', 'success')
            return redirect(url_for('admin.portfolio'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    return render_template('admin/portfolio_form.html', item=item)

@admin_bp.route('/portfolio/delete/<int:id>', methods=['POST'])
@login_required
def portfolio_delete(id):
    item = PortfolioItem.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash('Projet supprimé avec succès.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Une erreur est survenue : {str(e)}', 'error')
    return redirect(url_for('admin.portfolio'))

@admin_bp.route('/portfolio/toggle/<int:id>', methods=['POST'])
@login_required
def portfolio_toggle(id):
    item = PortfolioItem.query.get_or_404(id)
    try:
        item.is_active = not item.is_active
        db.session.commit()
        status = "activé" if item.is_active else "désactivé"
        flash(f'Projet {status} avec succès.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Une erreur est survenue : {str(e)}', 'error')
    return redirect(url_for('admin.portfolio'))

from models.book import BookSection
from models.setting import SeoSetting, GlobalSetting

@admin_bp.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    try:
        book_section = BookSection.query.first()
        if not book_section:
            book_section = BookSection()
            db.session.add(book_section)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur d'initialisation de la base de données : {str(e)}", 'error')
        book_section = None

    if request.method == 'POST' and book_section:
        book_section.title = request.form.get('title')
        book_section.subtitle = request.form.get('subtitle')
        book_section.description = request.form.get('description')
        book_section.cta_link = request.form.get('cta_link')
        book_section.cta_text = request.form.get('cta_text')

        try:
            db.session.commit()
            flash('Section Livre mise à jour avec succès.', 'success')
            return redirect(url_for('admin.book'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    return render_template('admin/book.html', book=book_section)

@admin_bp.route('/seo', methods=['GET', 'POST'])
@login_required
def seo():
    try:
        seo_setting = SeoSetting.query.first()
        if not seo_setting:
            seo_setting = SeoSetting()
            db.session.add(seo_setting)
            db.session.commit()
    except Exception as e:
        db.session.rollback()
        flash(f"Erreur d'initialisation de la base de données : {str(e)}", 'error')
        seo_setting = None

    if request.method == 'POST' and seo_setting:
        seo_setting.meta_title = request.form.get('meta_title')
        seo_setting.meta_description = request.form.get('meta_description')
        seo_setting.custom_head_script = request.form.get('custom_head_script')
        seo_setting.og_image = request.form.get('og_image')

        try:
            db.session.commit()
            flash('Paramètres SEO mis à jour avec succès.', 'success')
            return redirect(url_for('admin.seo'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    return render_template('admin/seo.html', seo=seo_setting)

@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    keys = [
        'logo_type', 'logo_text',
        'facebook', 'instagram', 'x', 'linkedin', 'whatsapp',
        'phone', 'email', 'address'
    ]

    if request.method == 'POST':
        try:
            for key in keys:
                value = request.form.get(key)
                if value is not None:
                    setting = GlobalSetting.query.filter_by(key=key).first()
                    if setting:
                        setting.value = value
                    else:
                        new_setting = GlobalSetting(key=key, value=value)
                        db.session.add(new_setting)

            # Handle file uploads for logo and favicon
            logo_file = request.files.get('logo_image')
            if logo_file and logo_file.filename != '':
                upload_path = handle_secure_upload(logo_file)
                if upload_path:
                    logo_setting = GlobalSetting.query.filter_by(key='logo_image_url').first()
                    if logo_setting:
                        logo_setting.value = upload_path
                    else:
                        new_logo_setting = GlobalSetting(key='logo_image_url', value=upload_path)
                        db.session.add(new_logo_setting)
                else:
                    flash('Format de fichier non autorisé ou fichier invalide pour le Logo.', 'error')

            favicon_file = request.files.get('favicon_image')
            if favicon_file and favicon_file.filename != '':
                upload_path = handle_secure_upload(favicon_file)
                if upload_path:
                    favicon_setting = GlobalSetting.query.filter_by(key='favicon_url').first()
                    if favicon_setting:
                        favicon_setting.value = upload_path
                    else:
                        new_favicon_setting = GlobalSetting(key='favicon_url', value=upload_path)
                        db.session.add(new_favicon_setting)
                else:
                    flash('Format de fichier non autorisé ou fichier invalide pour le Favicon.', 'error')

            db.session.commit()
            flash('Paramètres globaux mis à jour avec succès.', 'success')
            return redirect(url_for('admin.settings'))
        except Exception as e:
            db.session.rollback()
            flash(f'Une erreur est survenue : {str(e)}', 'error')

    # Fetch existing settings to populate the form
    existing_settings = {s.key: s.value for s in GlobalSetting.query.all()}

    return render_template('admin/settings.html', settings=existing_settings)
