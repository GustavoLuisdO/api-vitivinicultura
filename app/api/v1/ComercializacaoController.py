import httpx
from fastapi import APIRouter

from app.services.implementations.ComercializacaoServices import ComercializacaoServices

router = APIRouter()

comercializacao_services = ComercializacaoServices()

@router.get("/comercializacao/{ano}")
async def get_comercializacao(ano: int):
    try:
        return await comercializacao_services.obter_Comercializacao(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)