from charity.models.projet import Projet
from flask import jsonify, request
from extensions import db


class ProjetController:
    def __init__(self):
        self.projet_model = Projet

    def all(self):
        try:
            projets = self.projet_model.query.all()
            result = [{'id': projet.id, 'libelle': projet.libelle, 'description': projet.description,
                       'image': projet.image} for projet in projets]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def create(self):
        try:
            libelle = request.form['libelle']
            description = request.form['description']
            categorie_id = request.form['categorie_id']

            if 'image' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            image = request.files['image']
            projet = self.projet_model(libelle=libelle, description=description,
                                       categorie_id=categorie_id)
            projet.save_image(image)
            db.session.add(projet)
            db.session.commit()

            return jsonify({'message': 'Projet créé avec success'}), 201
        except KeyError:
            return jsonify({'message': 'Donnée manquant'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
