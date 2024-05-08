from abc import ABC, abstractmethod

class IProcessamentoServices(ABC):
    @abstractmethod
    async def obter_processamento_viniferas(self, ano: int):
        pass