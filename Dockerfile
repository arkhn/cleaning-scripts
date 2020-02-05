FROM python:3.7-slim

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential git

COPY requirements.txt  /app
RUN pip install -r requirements.txt --src /usr/local/src

ADD scripts /app/scripts
ADD api /app/api
COPY start.sh /app
COPY uwsgi.ini /app

CMD ["./start.sh"] 
