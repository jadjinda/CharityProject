from flask import request, jsonify
from charity.data import projets
from charity import api_charity_bp
from charity.controllers.CategorieController import CategorieController
from charity.controllers.ProjetController import ProjetController


@api_charity_bp.route("/api/list")
def api_list():
    return jsonify(projets)


categorieController = CategorieController()
projetController = ProjetController()


# Catégorie route
@api_charity_bp.route("/categories", methods=["POST"])
def add_categories():
    return categorieController.create()


@api_charity_bp.route("/listCategories", methods=["GET"])
def list_categories():
    return categorieController.all()


@api_charity_bp.route("/update/<int:id>", methods=["PUT"])
def update_categorie(id):
    return categorieController.update(id)


@api_charity_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_categorie(id):
    return categorieController.delete(id)


# project route
@api_charity_bp.route("/projects", methods=["POST"])
def add_project():
    return projetController.create()


@api_charity_bp.route("/listProject", methods=["GET"])
def list_project():
    return projetController.all()
