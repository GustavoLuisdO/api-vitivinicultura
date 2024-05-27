import json

import httpx
from bs4 import BeautifulSoup
from httpx import HTTPStatusError

from app.models.Categoria import Categoria
from app.models.Exportacao import Exportacao
from app.models.Produto import Produto
from app.services.interfaces.IExportacaoServices import IExportacaoServices

class ExportacaoServices(IExportacaoServices):

    async def extrair_dados(self, url, categoria):
        try:
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.get(url)
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
                        nome_categoria = categoria
                        nome_produto = linha.find_all('td')[0].get_text(strip=True)
                        qtde_kg = linha.find_all('td')[1].get_text(strip=True)
                        valor_us = linha.find_all('td')[2].get_text(strip=True)

                        # adicionar produto ao dicionário de produtos por categoria
                        if nome_categoria not in produtos_por_categoria:
                            produtos_por_categoria[nome_categoria] = []

                        produtos_por_categoria[nome_categoria].append(Produto(nome_produto, qtde_kg, valor_us, nome_categoria))

                # criar objetos de Categoria com base no dicionário de produtos por categoria
                categorias = [Categoria(nome_categoria, produtos) for nome_categoria, produtos in
                              produtos_por_categoria.items()]

                # instanciar o objeto de exportacao
                exportacao = Exportacao(categorias)

                # converter os dados para JSON
                json_str = json.dumps(exportacao.__json__(), indent=4, ensure_ascii=False)

                return json.loads(json_str)
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter exportação: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter exportação: {e}")



    async def obter_exportacao_vinho_de_mesa(self, ano: int):
        try:
            return await self.extrair_dados(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_01", "Vinhos de mesa");
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter exportação de vinhos de mesa no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter exportação de vinhos de mesa: {e}")

    async def obter_exportacao_espumantes(self, ano: int):
        try:
            return await self.extrair_dados(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_02", "Espumantes");
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter exportação de vinhos de mesa no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter exportação de vinhos de mesa: {e}")

    async def obter_exportacao_uvas_frescas(self, ano: int):
        try:
            return await self.extrair_dados(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_03", "Uvas Frescas");
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter exportação de vinhos de mesa no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter exportação de vinhos de mesa: {e}")

    async def obter_exportacao_suco_de_uva(self, ano: int):
        try:
            return await self.extrair_dados(f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_04", "Sucos de Uva");
        except httpx.HTTPStatusError as e:
            raise HTTPStatusError(f"Erro ao obter exportação de vinhos de mesa no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter exportação de vinhos de mesa: {e}")
