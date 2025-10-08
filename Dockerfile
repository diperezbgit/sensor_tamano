FROM python:3.10-slim

WORKDIR /app

# Instalar herramientas necesarias para compilar paquetes
RUN apt-get update && apt-get install -y gcc build-essential

# Instalar dependencias de Python
RUN pip install --no-cache-dir \
    fastapi[standard] \
    pydantic \
    mysql-connector-python \
    uvicorn

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]