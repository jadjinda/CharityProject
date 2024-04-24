from charity.models.projet import Projet
from flask import jsonify, request
from extensions import db


class ProjetController:
    def __init__(self):
        self.projet_model = Projet

    def create(self):
        try:
            data = request.get_json()
            nouveau_projet = self.projet_model(libelle=data['libelle'],
                                               description=data['description'],
                                               image=data['image'],
                                               categorie=data['categorie'])
            db.session.add(nouveau_projet)
            db.session.commit()
            return jsonify({'message': 'Nouveau projet créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            projets = Projet.query.all()
            result = [{'id': project.id,
                       'libelle': project.libelle,
                       'description': project.description,
                       'image': project.image,
                       'categorie': project.categorie} for project in projets]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500