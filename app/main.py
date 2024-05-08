from fastapi import FastAPI
from app.api.v1.ProducaoController import router as producao_controller
from app.api.v1.ProcessamentoController import router as processamento_controller

app = FastAPI()


app.include_router(producao_controller, prefix="/v1")
app.include_router(processamento_controller, prefix="/v1")
