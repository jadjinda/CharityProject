from flask import render_template
from charity.data import projets
from charity import web_charity_bp
from charity.controllers.ProjetController import ProjetController


projetController = ProjetController()

@web_charity_bp.route("/")
def index():
   return render_template('index.html', projets= projets)

@web_charity_bp.route("/details")
def details():
   return render_template('details.html')