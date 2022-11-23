from flask import Flask, render_template
from flask_restful import Api
from resources.movies import Movies, Movie
from resources.users import User, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# conexão com mysql
DATABASE_URI = 'mysql+pymysql://root@localhost/felipe?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#conexão com postgres
# DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost:5432/dbpython'
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Senai2022'

@app.before_first_request
def create_database():
    database.create_all()

# Telas
@app.route("/")
def login():
    return "Login"

@app.route("/menu")
def menu():
    return "Menu"

@app.route("/tabela")
def tabela():
    return "Tabela"

@app.route("/caixa")
def caixa():
    return "caixa"

@app.route("/produto")
def produto():
    return "Produto"

@app.route("/fornecedor")
def fornecedor():
    return "Fornecedor"

@app.route("/funcionario")
def funcionario():
    return "Funcionario"

@app.route("/faq")
def faq():
    return "FAQ"

@app.route("/relatorio")
def relatorio():
    return "Relatorio"

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
