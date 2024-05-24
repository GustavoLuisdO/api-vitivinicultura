import httpx
from fastapi import APIRouter

from app.services.implementations.ImportacaoServices import ImportacaoServices


router = APIRouter()

# instância do serviço
importacao_services = ImportacaoServices()

@router.get("/importacao/vinhodemesa/{ano}")
async def get_(ano: int):
    try:
        return await importacao_services.obter_importacao_vinho_de_mesa(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/importacao/espumantes/{ano}")
async def get_(ano: int):
    try:
        return await importacao_services.obter_importacao_espumantes(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/importacao/uvasFrescas/{ano}")
async def get_(ano: int):
    try:
        return await importacao_services.obter_importacao_uvas_frescas(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)

@router.get("/importacao/uvasPassas/{ano}")
async def get_(ano: int):
    try:
        return await importacao_services.obter_importacao_uvas_passas(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)


@router.get("/importacao/sucoDeUva/{ano}")
async def get_(ano: int):
    try:
        return await importacao_services.obter_importacao_suco_de_uva(ano)
    except httpx.HTTPStatusError as e:
        return e.response.status_code, None
    except Exception as e:
        return httpx._status_codes.code.BAD_REQUEST, str(e)