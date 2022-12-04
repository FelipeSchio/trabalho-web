from app import database


class VendaModel(database.Model):
    __tablename__ = 'venda'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    funcionario = database.Column(database.Integer, nullable=False)
    produto = database.Column(database.Integer, nullable=False)
    quantidade = database.Column(database.Integer, nullable=False)
    valor_total = database.Column(database.Integer, nullable=False)

    def __int__(self, funcionario, produto, quantidade, valor_total):
        self.funcionario = funcionario
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valor_total
