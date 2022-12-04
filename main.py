import datetime
from app import app, database
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from models.funcionario import FunciModel
from models.fornecedor import ForneModel
from models.produto import ProdModel
from models.caixa import VendaModel


@app.before_first_request
def create_database():
    database.create_all()


# Telas
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        # Verifica email e senha
        funci = FunciModel.query.filter_by(email=email).first()
        if funci is not None:
            senha = funci.verificar_senha(senha=senha)

        if not email or not senha:
            return redirect(url_for('login'))

        login_user(funci)
        return redirect(url_for('menu'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')


@app.route('/tabela', methods=['GET', 'POST'])
def tabela():
    dados = {"nome": "Felipe", "email": "felipe@gmail.com", "tipo": "Operacional"}

    return render_template('tabela.html', dados=dados)


@app.route('/caixa', methods=['GET', 'POST'])
def caixa():
    if request.method == 'POST':
        funcionario = request.form['funcionario']
        produto = request.form['produto']
        quantidade = request.form['quantidade']
        valor_total = request.form['valor_total']

        nova_venda = VendaModel(funcionario=funcionario, produto=produto, quantidade=quantidade,
                                valor_total=valor_total)
        database.session.add(nova_venda)
        database.session.commit()

        return redirect(url_for('caixa'))

    return render_template('caixa.html')


@app.route('/produto', methods=['GET', 'POST'])
def produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco_unitario = request.form['preco_unitario']
        quantidade = request.form['quantidade']
        unidade = request.form['unidade']
        fornecedor = request.form['fornecedor']

        novo_produto = ProdModel(nome=nome, preco_unitario=preco_unitario, quantidade=quantidade,
                                 unidade=unidade, fornecedor=fornecedor)
        database.session.add(novo_produto)
        database.session.commit()

        return redirect(url_for('produto'))

    return render_template('produto.html')


@app.route('/fornecedor', methods=['GET', 'POST'])
def fornecedor():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']

        novo_fornecedor = ForneModel(nome=nome, email=email, telefone=telefone)
        database.session.add(novo_fornecedor)
        database.session.commit()

        return redirect(url_for('fornecedor'))

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

        novo_funcionario = FunciModel(nome=nome, email=email, telefone=telefone, senha=senha, tipo=tipo,
                                      data_cadastro=data_cadastro, data_atualizacao=data_atualizacao)
        database.session.add(novo_funcionario)
        database.session.commit()

        return redirect(url_for('funcionario'))

    return render_template('funcionario.html')


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template('faq.html')

# deixa pra fazer por ultimo
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
