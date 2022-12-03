from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
"jwt = JWTManager(app)"

# conexão com mysql
DATABASE_URI = 'mysql+pymysql://root:1234@localhost/mercadinho?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secreta'

login_manager = LoginManager(app)
database = SQLAlchemy(app)
