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
                for linha in linhas:
                    celulas = linha.find_all('td')

                    dados_linha = []
                    cont = 0
                    for celula in celulas:
                        dados_linha.append(celula.text.replace("\n", "").strip())
                        cont = cont + 1

                    dados.append(Producao(dados_linha[0], dados_linha[1]).__json__())

                # Converter os dados para JSON
                json_str = json.dumps(dados, indent=4, ensure_ascii=False)

                return json.loads(json_str)
        except httpx.HTTPStatusError as e:
            raise Exception(f"Erro ao obter produção no ano {ano}: {e}")
        except Exception as e:
            raise Exception(f"Erro ao obter produção no ano {ano}: {e}")