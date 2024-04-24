from extensions import db

class Projet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    categorie = db.relationship('Categorie', backref=db.backref('projets', lazy=True))