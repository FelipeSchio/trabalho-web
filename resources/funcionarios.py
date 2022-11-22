from flask_restful import Resource, reqparse
from models.funcionario import FunciModel

funcionarios = [
    {'id': 1,
     'name': 'Homem-Aranha 3', 'rating': '4.5',
     'duration': '120', 'creat_at': '2020', 'age_group': '13',
     'link_trailer': '#'},
    {'id': 2,
     'name': 'Dois filhos', 'rating': '2.5',
     'duration': '111', 'creat_at': '2013', 'age_group': '13',
     'link_trailer': '#'},
    {'id': 3,
     'name': 'Top gun', 'rating': '3.9',
     'duration': '160', 'creat_at': '1995', 'age_group': '18',
     'link_trailer': '#'}
]

class FunciModel():
    def __int__(self, id, name, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.id = id
        self.name = name
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

        def json(self):
            return {
                'id': self.id,
                'name': self.name,
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
    minha_requisicao.add_argument('name')
    minha_requisicao.add_argument('email')
    minha_requisicao.add_argument('telefone')
    minha_requisicao.add_argument('senha')
    minha_requisicao.add_argument('tipo')
    minha_requisicao.add_argument('data_cadastro')
    minha_requisicao.add_argument('data_atualizacao')

    def find_funci(id):
        for funci in funcis:
            if funci['id'] == id:
                return funci
        return None

    def find_last_movie(self):
        funci_id = 0
        for funci in funcis:
            if funci['id'] >= funci_id:
                funci_id = funci['id']
        return funci_id

    def get(self, id):
        funci = FunciModel.find_funci_by_id(id)
        if funci:
            return funci
        return {'message': 'funcionario não encontrado'}, 200

    def post(self, id):
        dados = Funcionario.minha_requisicao.parse_args()
        funci_id = Funcionario.find_last_movie() + 1

        new_funci = FunciModel(funci_id, dados)

        funcis.append(new_funci.json())
        return new_funci.json(id)

        funcis.append(new_funci)
        return new_funci, 200

    def put(self, id):
        dados = Funcionario.minha_requisicao.parse_args()
        funci = Funcionario.find_movie(id)

        if funci:
            new_funci = {'id': id, **dados}
            funci.update(new_funci)
            return new_funci, 200
        else:
            funci_id = Funcionario.find_last_funci() + 1
            new_movie = {'id': funci_id, **dados}
            funcis.append(new_movie)
            return new_movie, 201

    def delete(self, id):
        global funcis
        funcis = [funci for funci in funcis if funci['id'] != id]
        return {'message': 'movie deleted'}