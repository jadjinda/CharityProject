from flask import render_template
from charity.data import projets
from charity import web_charity_bp

@web_charity_bp.route("")
def index():
   return render_template('index.html', projets= projets)