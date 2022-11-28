from flask_restful import Resource, reqparse
from models.funcionario import FunciModel
from flask_jwt_extended import create_access_token

minha_requisicao = reqparse.RequestParser()
minha_requisicao.add_argument('email', type=str, required=True, help="email é necessário")
minha_requisicao.add_argument('senha', type=str, required=True, help="senha é necessária")

class Funci(Resource):

    def get(self, id):
        funci = FunciModel.find_funci_by_id(id)
        if funci:
            return funci.json()
        return {'message': 'funcionário não encontrado'}, 200

    def delete(self, id):
        funci = FunciModel.find_funci_by_id(id)
        if funci:
            funci.delete_funci()
            return {'message': 'funcionário deletado.'}
        return {'message': 'funcionário não encontrado'}, 200

    def post(self, id):
        dados = minha_requisicao.parse_args()

        if FunciModel.find_user_by_login(dados['email']):
            return {'message': 'Login {} already exists'.format(dados['login'])}, 200

        id = FunciModel.find_last_user()
        novo_funci = FunciModel(id, **dados)

        try:
            print(novo_funci.json())
            novo_funci.save_funci()
        except:
            return {'message': 'An internal error ocurred.'}, 500

        return novo_funci.json(), 201


class FunciLogin(Resource):

    @classmethod
    def post(cls):
        dados = minha_requisicao.parse_args()
        funci = FunciModel.find_funci_by_login(dados['email'])

        if funci and funci.senha == dados['senha']:
            token_acesso = create_access_token(identity=funci.id)
            return {'access_token': token_acesso}, 200
        return {'message': 'email ou senha não estão corretas.'}

