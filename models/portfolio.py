from models.base import db

class PortfolioItem(db.Model):
    __tablename__ = 'portfolio_items'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.JSON, nullable=False)
    description = db.Column(db.JSON, nullable=True)
    link = db.Column(db.String(500), nullable=True)
    icon_class = db.Column(db.String(100), nullable=True)
    color_class = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    order = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'<PortfolioItem {self.title}>'
