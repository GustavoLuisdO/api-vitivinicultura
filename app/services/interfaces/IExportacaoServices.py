from abc import ABC, abstractmethod

class IExportacaoServices(ABC):

    @abstractmethod
    async def obter_exportacao_vinho_de_mesa(self, ano: int):
        pass

    @abstractmethod
    async def obter_exportacao_espumantes(self, ano: int):
        pass

    @abstractmethod
    async def obter_exportacao_uvas_frescas(self, ano: int):
        pass


    @abstractmethod
    async def obter_exportacao_suco_de_uva(self, ano: int):
        pass