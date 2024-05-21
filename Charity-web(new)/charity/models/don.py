from extensions import db


class Don(db.Model):
    __tablename__ = 'dons'
    id = db.Column(db.Integer, primary_key=True)
    montant = db.Column(db.Float, nullable=False)
    identifiant = db.Column(db.String(255), nullable=False)
    telephone = db.Column(db.String(10), nullable=False)
    modePayement = db.Column(db.String(10), nullable=False)
    projet_id = db.Column(db.Integer, db.ForeignKey('projet.id'), nullable=False)
    projet = db.relationship('Projet', backref=db.backref('dons', lazy=True))
