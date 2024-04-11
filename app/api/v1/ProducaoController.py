from fastapi import APIRouter

from app.services.implementations.ProducaoServices import ProducaoServices

router = APIRouter()

# Instância única do serviço
producao_service = ProducaoServices()

@router.get("/producao/{ano}")
async def get_producao(ano: int):
    return await producao_service.obter_producao(ano)

