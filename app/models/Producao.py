class Producao:
    def __init__(self, produto: str, quantidade_litros: str):
        self.produto = produto
        self.quantidade_litros = quantidade_litros

    def __json__(self):
        return {
            "produto": self.produto,
            "quantidade_litros": self.quantidade_litros
        }