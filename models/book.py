from models.base import db

class BookSection(db.Model):
    __tablename__ = 'book_sections'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    subtitle = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    cta_link = db.Column(db.String(500), nullable=True)
    cta_text = db.Column(db.String(255), nullable=True)
    image_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<BookSection {self.title}>'
