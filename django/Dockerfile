FROM python:3.8

RUN apt update && apt install -y python-psycopg2 netcat vim
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
