FROM python:3.12.2-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12.2-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000"]