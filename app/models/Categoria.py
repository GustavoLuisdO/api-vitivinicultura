from app.models.Produto import Produto


class Categoria:
    def __init__(self, nome: str, produtos: list[Produto]):
        self.nome = nome
        self.produtos = produtos if produtos is not None else []