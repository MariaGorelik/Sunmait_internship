FROM python:3.12.2-slim

WORKDIR /app

RUN pip install fastapi

RUN pip install pydantic

RUN pip install transformers

RUN pip install uvicorn

RUN pip install httpx

COPY . /app

CMD ["python", "hello.py"]