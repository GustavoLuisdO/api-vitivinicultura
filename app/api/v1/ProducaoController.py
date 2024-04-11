from fastapi import APIRouter

router = APIRouter()


@router.get("/producao")
async def get_producao():
    return {"producao": "n "}

