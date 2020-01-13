FROM python:3.7-slim

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

ADD . /app

EXPOSE 5001

CMD flask run --host=0.0.0.0 --port=5001
