from fastapi import FastAPI
from app.api.v1.ProducaoController import router as producao_controller

app = FastAPI()


app.include_router(producao_controller, prefix="/v1")
