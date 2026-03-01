from models.base import db

class BookSection(db.Model):
    __tablename__ = 'book_sections'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.JSON, nullable=True)
    subtitle = db.Column(db.JSON, nullable=True)
    description = db.Column(db.JSON, nullable=True)
    cta_link = db.Column(db.String(500), nullable=True)
    cta_text = db.Column(db.JSON, nullable=True)
    image_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<BookSection {self.title}>'
