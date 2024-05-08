from abc import ABC, abstractmethod

class IProcessamentoServices(ABC):
    @abstractmethod
    async def obter_processamento_viniferas(self, ano: int):
        pass

    @abstractmethod
    async def obter_processamento_americanas_e_hibridas(self, ano: int):
        pass

    @abstractmethod
    async def obter_processamento_uva_de_mesa(self, ano: int):
        pass

    @abstractmethod
    async def obter_processamento_sem_classificacao(self, ano: int):
        pass