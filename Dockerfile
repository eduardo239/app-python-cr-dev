# Use uma imagem Python oficial como base
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requirements
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta (Cloud Run usa a variável PORT)
EXPOSE 8080

# Define o comando para executar a aplicação
CMD ["python", "app.py"]