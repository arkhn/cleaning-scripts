FROM python:3.7-slim

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0