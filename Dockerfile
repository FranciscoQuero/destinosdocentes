FROM python:3.9.6-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
EXPOSE 8000
ENTRYPOINT python manage.py
