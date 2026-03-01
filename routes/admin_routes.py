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
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
                    if allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        upload_folder = os.path.join(current_app.static_folder, 'uploads')
                        os.makedirs(upload_folder, exist_ok=True)
                        file_path = os.path.join(upload_folder, filename)
                        file.save(file_path)

                        image.upload_path = f"uploads/{filename}"
                        image.is_uploaded = True
                        image.image_url = None
                    else:
                        flash(f'Format de fichier non autorisé pour {image.section_name}.', 'error')
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
