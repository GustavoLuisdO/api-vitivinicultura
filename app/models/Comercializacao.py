from app.models.Categoria import Categoria

class Comercializacao:
    def __init__(self, categorias: list[Categoria]):
        self.categorias = categorias


    def __json__(self):
        dados = {}
        for categoria in self.categorias:
            # lista vazia para armazenar os produtos da categoria atual
            produtos = []

            for produto in categoria.produtos:
                # criar um dicionário com o nome e a quantidade de litros do produto atual e o adiciona à lista de produtos
                produtos.append({'Produto': produto.nome, 'Quantidade (litros)': produto.quantidade})

            # associar a lista de produtos à categoria atual no dicionário de dados
            dados[categoria.nome] = produtos

        return dados