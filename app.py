from flask import Flask, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from sql_alchemy import database

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

# conexão com mysql
DATABASE_URI = 'mysql+pymysql://root:1234@localhost/mercadinho?charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.before_first_request
def create_database():
    database.create_all()

# Telas
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template("menu.html")

@app.route("/tabela")
def tabela():
    return render_template("tabela.html")

@app.route("/caixa")
def caixa():
    return render_template("caixa.html")

@app.route("/produto")
def produto():
    return render_template("produto.html")

@app.route("/fornecedor")
def fornecedor():
    return render_template("fornecedor.html")

@app.route("/funcionario")
def funcionario():
    return render_template("funcionario.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html")

@app.route("/<string:nome>")
def error(nome):
    return f'Página {nome} não existe'

if __name__ == '__main__':
    database.init_app(app)
    app.run(debug=True)
