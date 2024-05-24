from abc import ABC, abstractmethod

class IImportacaoServices(ABC):

    @abstractmethod
    async def obter_importacao_vinho_de_mesa(self, ano: int):
        pass

    @abstractmethod
    async def obter_importacao_espumantes(self, ano: int):
        pass

    @abstractmethod
    async def obter_importacao_uvas_frescas(self, ano: int):
        pass

    @abstractmethod
    async def obter_importacao_uvas_passas(self, ano: int):
        pass

    @abstractmethod
    async def obter_importacao_suco_de_uva(self, ano: int):
        pass