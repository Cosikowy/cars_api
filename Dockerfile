FROM python:3.8-slim-buster

RUN mkdir /app
COPY requirements.txt /app

RUN apt-get update 

RUN pip install -r /app/requirements.txt

COPY ./ /app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT python manage.py migrate && python manage.py runserver
