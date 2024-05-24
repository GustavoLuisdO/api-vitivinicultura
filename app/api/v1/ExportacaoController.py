import httpx
from fastapi import APIRouter

from app.services.implementations.ExportacaoServices import ExportacaoServices

router = APIRouter()

# instância do serviço
exportacao_services = ExportacaoServices()

@router.get("/exportacao/vinhodemesa/{ano}")
async def get_(ano: int):
    try:
        return await exportacao_services.obter_exportacao_vinho_de_mesa(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/exportacao/espumantes/{ano}")
async def get_(ano: int):
    try:
        return await exportacao_services.obter_exportacao_espumantes(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/exportacao/uvasFrescas/{ano}")
async def get_(ano: int):
    try:
        return await exportacao_services.obter_exportacao_uvas_frescas(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/exportacao/sucoDeUva/{ano}")
async def get_(ano: int):
    try:
        return await exportacao_services.obter_exportacao_suco_de_uva(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)