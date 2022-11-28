from sql_alchemy import database

class FunciModel (database.Model):

    __tablename__ = 'funcionario'
    id = database.Column(database.Integer, primary_key = True, autoincrement=True)
    nome = database.Column(database.String(25))
    email = database.Column(database.String(25))
    telefone = database.Column(database.String(25))
    senha = database.Column(database.String(25))
    tipo = database.Column(database.String(25))
    data_cadastro = database.Column(database.date)
    data_atualizacao = database.Column(database.date)


    def __int__ (self, nome, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

    def json (self):
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
