from abc import abstractmethod, ABC


class IComercializacaoServices(ABC):

    @abstractmethod
    async def obter_Comercializacao(self, ano:int):
        pass