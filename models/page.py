from models.base import db

class PageImage(db.Model):
    __tablename__ = 'page_images'

    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(100), unique=True, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    upload_path = db.Column(db.String(500), nullable=True)
    is_uploaded = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<PageImage {self.section_name}>'
