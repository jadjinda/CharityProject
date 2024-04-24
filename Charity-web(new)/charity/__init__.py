from flask import Blueprint

web_charity_bp = Blueprint('charity_web', __name__, template_folder='templates', static_folder='static')

api_charity_bp = Blueprint('charity_api', __name__, template_folder='templates', static_folder='static')

from charity.views import route, api_route