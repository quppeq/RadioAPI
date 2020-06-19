FROM python:3.8
RUN mkdir -p /app
WORKDIR /app
RUN pip install pipenv

COPY Pipfile Pipfile
COPY db db
COPY radio radio
COPY manage.py manage.py
COPY .git .git

RUN set -ex && apt update -y && apt install -y git
RUN set -ex && pipenv install
CMD FLASK_APP=manage.py pipenv run flask run -h 0.0.0.0 -p 5000
