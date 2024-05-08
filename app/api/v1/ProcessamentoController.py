import httpx
from fastapi import APIRouter

from app.services.implementations.ProcessamentoServices import ProcessamentoServices

router = APIRouter()

# instância do serviço
processamento_services = ProcessamentoServices()

@router.get("/processamento/viniferas/{ano}")
async def get_(ano: int):
    try:
        return await processamento_services.obter_processamento_viniferas(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)

