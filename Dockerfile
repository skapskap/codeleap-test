FROM python:3.11.3-alpine3.18

LABEL mantainer="skaprange@gmail.com"

ENV PYTHONDONTWRITEBYTECODE  1

# Exibe a saída do Python em tempo real
ENV PYTHONUNBUFFERED  1

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

WORKDIR /app

EXPOSE  8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]