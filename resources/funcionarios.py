from flask_restful import Resource, reqparse
from models.funcionario import FunciModel

funcionarios = [
    {'id': 1,
     'nome': 'Homem-Aranha 3', 'rating': '4.5',
     'duration': '120', 'creat_at': '2020', 'age_group': '13',
     'link_trailer': '#'},
]

class FunciModel():
    def __int__(self, id, nome, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

        def json(self):
            return {
                'id': self.id,
                'nome': self.nome,
                'email': self.email,
                'telefone': self.telefone,
                'senha': self.senha,
                'tipo': self.tipo,
                'data_cadastro': self.data_cadastro,
                'data_atualizacao': self.data_atualizacao
            }

class Funcionarios(Resource):
    def get(self):
        return funcionarios

class Funcionario(Resource):
    minha_requisicao = reqparse.RequestParser()
    minha_requisicao.add_argument('nome')
    minha_requisicao.add_argument('email')
    minha_requisicao.add_argument('telefone')
    minha_requisicao.add_argument('senha')
    minha_requisicao.add_argument('tipo')
    minha_requisicao.add_argument('data_cadastro')
    minha_requisicao.add_argument('data_atualizacao')

    