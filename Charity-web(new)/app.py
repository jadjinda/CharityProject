import flask
from flask_migrate import Migrate

from charity import web_charity_bp, api_charity_bp
from flask_cors import CORS
from extensions import db
from charity.models.categorie import Categorie
from charity.models.projet import Projet

app = flask.Flask(__name__)

CORS(app, origins="*")

app.register_blueprint(web_charity_bp, url_prefix='/charity')
app.register_blueprint(api_charity_bp, url_prefix='/api/charity')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://josue:1234Jojo@127.0.0.1:3306/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from charity.models.categorie import Categorie
from charity.models.projet import Projet

# db.init_app(app)

# with app.app_context():
#   db.create_all()
