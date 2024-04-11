from abc import ABC, abstractmethod

class IProducaoServices(ABC):
    @abstractmethod
    async def obter_producao(self, ano: int):
        pass