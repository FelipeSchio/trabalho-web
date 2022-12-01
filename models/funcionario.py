from app import database, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(id):
    return FunciModel.query.filter_by(id=id).first()
class FunciModel (database.Model, UserMixin):

    __tablename__ = 'funcionario'
    id = database.Column(database.Integer, primary_key = True, autoincrement=True)
    nome = database.Column(database.String(25), nullable=False)
    email = database.Column(database.String(25), nullable=False)
    telefone = database.Column(database.String(25), nullable=False)
    senha = database.Column(database.String(25), nullable=False)
    tipo = database.Column(database.String(25), nullable=False)
    data_cadastro = database.Column(database.Date, nullable=False)
    data_atualizacao = database.Column(database.Date, nullable=False)


    def __int__ (self, nome, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = generate_password_hash(senha)
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

    @classmethod
    def find_funci_by_id(cls, id):
        funci = cls.query.filter_by(id=id).first()
        if funci:
            return funci
        return None

    @classmethod
    def find_funci_by_login(cls, email):
        user = cls.query.filter_by(email = email).first()
        if user:
            return user
        return None

    def save_funci(self):
        database.session.add(self)
        database.session.commit()

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)