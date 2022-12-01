import datetime

from app import app, database
from flask import render_template, request, redirect, url_for
from models.funcionario import FunciModel

@app.before_first_request
def create_database():
    database.create_all()

# Telas
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

@app.route('/tabela', methods=['GET', 'POST'])
def tabela():
    return render_template('tabela.html')

@app.route('/caixa', methods=['GET', 'POST'])
def caixa():
    return render_template('caixa.html')

@app.route('/produto', methods=['GET', 'POST'])
def produto():
    return render_template('produto.html')

@app.route('/fornecedor', methods=['GET', 'POST'])
def fornecedor():
    return render_template('fornecedor.html')

@app.route('/funcionario', methods=['GET', 'POST'])
def funcionario():

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        tipo = request.form['tipo']
        data_cadastro = datetime.date.today()
        data_atualizacao = datetime.date.today()

        novo_funcionario = FunciModel(nome=nome, email=email, telefone=telefone, senha=senha, tipo=tipo, data_cadastro=data_cadastro, data_atualizacao=data_atualizacao)
        database.session.add(novo_funcionario)
        database.session.commit()

        return redirect(url_for('funcionario'))

    return render_template('funcionario.html')

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')

@app.route('/relatorio', methods=['GET', 'POST'])
def relatorio():
    return render_template('relatorio.html')

@app.route('/rodape', methods=['GET', 'POST'])
def rodape():
    return render_template('rodape.html')

@app.route('/<string:nome>')
def error(nome):
    return f'Página {nome} não existe'

if __name__ == '__main__':
    database.init_app(app)
    app.run(debug=True)
