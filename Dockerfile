FROM python:3.8

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

ENV PYTHONUNBUFFERED 1
WORKDIR /app/shopbackend
COPY requirements.txt /app/shopbackend
RUN pip install -r requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000