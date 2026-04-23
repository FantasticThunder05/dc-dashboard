FROM python:3.12-slim

WORKDIR /app

# Instalamos lo necesario para que Streamlit corra en Linux
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiamos e instalamos tus librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponemos el puerto de Streamlit
EXPOSE 8501

# Comando para que arranque el Dashboard
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]