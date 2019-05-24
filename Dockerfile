FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install dos2unix -q -y

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt .
RUN pip install -U -r requirements.txt
ADD . .

RUN dos2unix docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh
