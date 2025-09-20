FROM python:3.9-bookworm

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt install libpq-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY src .env .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
