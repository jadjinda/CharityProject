from charity.models.categorie import Categorie
from flask import jsonify, request
from extensions import db


class CategorieController:
    def __init__(self):
        self.categorie_model = Categorie

    def create(self):
        try:
            data = request.get_json()
            nouvelle_categorie = self.categorie_model(libelle=data['libelle'])
            db.session.add(nouvelle_categorie)
            db.session.commit()
            return jsonify({'message': 'Nouvelle catégorie créée avec succès'}), 201
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def all(self):
        try:
            categories = Categorie.query.all()
            result = [{'id': categorie.id, 'libelle': categorie.libelle} for categorie in categories]
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'message': e}), 500

    def update(self, categorie_id):
        try:
            data = request.get_json()
            categorie = Categorie.query.get(categorie_id)
            if categorie:
                categorie.libelle = data['libelle']
                #db.session.save()
                db.session.commit()
                return jsonify({'message': 'Catégorie mise à jour avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500

    def delete(self, categorie_id):
        try:
            categorie = Categorie.query.get(categorie_id)
            if categorie:
                db.session.delete(categorie)
                db.session.commit()
                return jsonify({'message': 'Catégorie supprimée avec succès'}), 200
            else:
                return jsonify({'message': 'Catégorie non trouvée'}), 404
        except KeyError:
            return jsonify({'message': 'Données manquantes'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': e}), 500
