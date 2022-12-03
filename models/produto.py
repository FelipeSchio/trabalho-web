from app import database


class ProdModel(database.Model):
    __tablename__ = 'produto'
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    nome = database.Column(database.String(25), nullable=False)
    preco_unitario = database.Column(database.String(25), nullable=False)
    quantidade = database.Column(database.Integer, nullable=False)
    unidade = database.Column(database.String(25), nullable=False)
    fornecedor = database.Column(database.Integer, nullable=False)

    def __int__(self, nome, preco_unitario, quantidade, unidade, fornecedor):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.unidade = unidade
        self.fornecedor = fornecedor
