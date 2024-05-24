from app.models.Categoria import Categoria

class Exportacao():

    def __init__(self, exportacao: list[Categoria]):
        self.exportacao = exportacao


    def __json__(self):
        dados = {}
        for categoria in self.categorias:
            # lista vazia para armazenar os produtos da categoria atual
            produtos = []

            for produto in categoria.produtos:
                # criar um dicionário com o nome e a quantidade de litros do produto atual e o adiciona à lista de produtos
                produtos.append({'País': produto.nome, 'Quantidade (kg)': produto.quantidade, 'Valor (US$)': produto.valor})

            # associar a lista de produtos à categoria atual no dicionário de dados
            dados[categoria.nome] = produtos

        return dados