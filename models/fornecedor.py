from app import database


class ForneModel(database.Model):
    __tablename__ = 'fornecedor'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    nome = database.Column(database.String(25), nullable=False)
    email = database.Column(database.String(25), nullable=False)
    telefone = database.Column(database.String(25), nullable=False)

    def __int__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
