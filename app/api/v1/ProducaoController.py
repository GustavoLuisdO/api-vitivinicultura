import httpx
from fastapi import APIRouter

from app.services.implementations.ProducaoServices import ProducaoServices

router = APIRouter()

# Instância única do serviço
producao_service = ProducaoServices()

@router.get("/producao/{ano}")
async def get_producao(ano: int):
    try:
        return await producao_service.obter_producao(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)

