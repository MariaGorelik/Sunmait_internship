FROM python:3.12.2-slim

WORKDIR /app

COPY . /app

RUN pip install virtualenv

RUN python -m virtualenv venv

RUN . venv/bin/activate && pip install -r requirements.txt

CMD ["venv/bin/python", "hello.py"]