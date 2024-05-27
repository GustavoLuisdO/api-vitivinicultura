# Usando uma imagem base oficial do Python
FROM python:3.9

# Definindo o diretório de trabalho no contêiner
WORKDIR /app

# Copiando a api para o container
COPY api-vitivinicultura/ .

# Dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Porta que será usada
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
