from itertools import groupby

from httpx import HTTPStatusError

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
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.get(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02")
                response.raise_for_status()

                # processar o html
                soup = BeautifulSoup(response.text, 'html.parser')

                # encontrar a tabela
                # pode ser por índice, classe, id, etc
                tabela = soup.find('table', attrs={'class': 'tb_dados'})

                # extrair as linhas da tabela
                linhas = tabela.find_all('tr')[1:-1]  # pula a linha de cabeçalho e linha do rodape

                # dicionário para manter o rastreamento dos produtos por categoria
                produtos_por_categoria = {}

                for linha in linhas:
                    # verificar se a linha atual é uma categoria
                    is_categoria = 'tb_item' in linha.find('td').get('class', [])

                    if not is_categoria:
                        nome_categoria = linha.find_previous('td', class_='tb_item').parent()[0].get_text(strip=True)
                        nome_produto = linha.find_all('td')[0].get_text(strip=True)
                        qtde_litros = linha.find_all('td')[1].get_text(strip=True)

                        # adicionar produto ao dicionário de produtos por categoria
                        if nome_categoria not in produtos_por_categoria:
                            produtos_por_categoria[nome_categoria] = []

                        produtos_por_categoria[nome_categoria].append(Produto(nome_produto, qtde_litros, "", nome_categoria))

                # criar objetos de Categoria com base no dicionário de produtos por categoria
                categorias = [Categoria(nome_categoria, produtos) for nome_categoria, produtos in produtos_por_categoria.items()]

                # instanciar o objeto de produção
                producao = Producao(categorias)

                # converter os dados para JSON
                json_str = json.dumps(producao.__json__(), indent=4, ensure_ascii=False)

                return json.loads(json_str)
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter produção no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter produção: {e}")


def obter_categoria_por_produto(produto):
    return produto.nome_categoria