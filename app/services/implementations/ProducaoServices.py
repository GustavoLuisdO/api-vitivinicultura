from itertools import groupby

from app.models.Categoria import Categoria
from app.models.Produto import Produto
from app.services.interfaces.IProducaoServices import IProducaoServices
from app.models.Producao import Producao
from bs4 import BeautifulSoup
import httpx
import json

class ProducaoServices(IProducaoServices):
    async def obter_producao(self, ano: int):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02")
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                # encontrar a tabela
                # se houver mais de uma tabela, você precisará identificar qual tabela extrair.
                # pode ser por índice, classe, id, etc.
                tabela = soup.find('table', attrs={'class': 'tb_dados'})

                # extrair as linhas da tabela
                linhas = tabela.find_all('tr')[1:]  # Pula a linha de cabeçalho

                # extrair os dados
                dados = []

                produtos = []
                for linha in linhas:
                    # verificar se a linha atual é uma categoria
                    is_categoria = 'tb_item' in linha.find('td').get('class', [])

                    if not is_categoria:
                        nome_categoria = linha.find_previous('td', attrs={'class': 'tb_item'}).parent()[0].text.replace("\n", "").strip()
                        nome_produto = linha.find_all('td')[0].text.replace("\n", "").strip()
                        qtde_litros = linha.find_all('td')[1].text.replace("\n", "").strip()

                        produtos.append(Produto(nome_produto, qtde_litros, nome_categoria))

                # adicionar as categorias em uma lista
                categorias = []
                for nome_categoria, produtos_categoria in groupby(produtos, key=obter_categoria_por_produto):
                    categoria = Categoria(nome_categoria, [])
                    for produto in list(produtos_categoria):
                        categoria.produtos.append(produto)

                    categorias.append(categoria)

                # instanciar o objeto de produção
                producao = Producao(categorias)

                print(producao.__json__())

                # converter os dados para JSON
                json_str = json.dumps(producao.__json__(), indent=4, ensure_ascii=False)

                return json.loads(json_str)
        except httpx.HTTPStatusError as e:
            raise Exception(f"Erro ao obter produção no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter produção: {e}")


def obter_categoria_por_produto(produto):
    return produto.nome_categoria