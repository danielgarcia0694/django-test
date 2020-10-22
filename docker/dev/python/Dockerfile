FROM python:3.7

ENV PYTHONUNBUFFERED 1

ENV APP_DIR /app

COPY ./app $APP_DIR

WORKDIR $APP_DIR

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements/base.txt
