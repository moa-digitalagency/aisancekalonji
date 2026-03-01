from models.base import db

class GlobalSetting(db.Model):
    __tablename__ = 'global_settings'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<GlobalSetting {self.key}>'

class SeoSetting(db.Model):
    __tablename__ = 'seo_settings'

    id = db.Column(db.Integer, primary_key=True)
    meta_title = db.Column(db.String(255), nullable=True)
    meta_description = db.Column(db.Text, nullable=True)
    custom_head_script = db.Column(db.Text, nullable=True)
    og_image = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<SeoSetting {self.id}>'
