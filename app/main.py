from fastapi import FastAPI
from app.api.v1.ProducaoController import router as producao_controller
from app.api.v1.ProcessamentoController import router as processamento_controller
from app.api.v1.ComercializacaoController import router as comercializacao_controller
from app.api.v1.ImportacaoController import router as importacao_controller
from app.api.v1.ExportacaoController import router as exportacao_controller

app = FastAPI()


app.include_router(producao_controller, prefix="/v1")
app.include_router(processamento_controller, prefix="/v1")
app.include_router(comercializacao_controller, prefix="/v1")
app.include_router(importacao_controller, prefix="/v1")
app.include_router(exportacao_controller, prefix="/v1")
