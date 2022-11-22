from sql_alchemy import database

class FunciModel (database.Model):

    __tablename__ = 'funcionario'
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(25))
    email = database.Column(database.String(25))
    telefone = database.Column(database.String(25))
    senha = database.Column(database.String(25))
    tipo = database.Column(database.String(25))
    data_cadastro = database.Column(database.date)
    data_atualizacao = database.Column(database.date)


def __int__ (self, id, name, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.id = id
        self.name = name
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

    def json (self):
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

    @classmethod
    def find_funci_by_id(cls, id):  # metodo de classe, mesmo que chamar Movie.query
        movie = cls.query.filter_by(id=id).first()  # select * from funcionario where id = 1
        if movie:
            return movie
        return None

    def save_funci(self):
        database.session.add(self)
        database.session.commit()

    def update_funci(self, name, email, telefone, senha, tipo, data_cadastro, data_atualizacao):
        self.name = name
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro
        self.data_atualizacao = data_atualizacao

    def delete_funci(self):
        database.session.delete(self)
        database.session.commit()

    @classmethod
    def find_last_funci(cls):
        funci_id = database.engine.execute("select nextval('funci_id') as new_id").fetchone()
        if funci_id:
            return funci_id['new_id'] + 1
        return 1