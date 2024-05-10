import flask
from flask_migrate import Migrate

from charity import web_charity_bp, api_charity_bp
from accounts import auth_bp
from flask_cors import CORS
from extensions import db
from charity.models.categorie import Categorie
from charity.models.projet import Projet
from flask_login import LoginManager

app = flask.Flask(__name__)

CORS(app, origins="*")

app.register_blueprint(web_charity_bp, url_prefix='/charity')
app.register_blueprint(api_charity_bp, url_prefix='/api/charity')
app.register_blueprint(auth_bp, url_prefix='/auth')

app.config['SECRET_KEY'] = 'charity_secret'
app.config['BASE_TEMPLATE_FOLDER'] = 'charity/templates'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://josue:1234Jojo@127.0.0.1:3306/charity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)


#Specifier la vue de connexion
login_manager.login_view = 'auth.login'

from charity.models.categorie import Categorie
from charity.models.projet import Projet
from accounts.models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# db.init_app(app)

# with app.app_context():
#   db.create_all()
