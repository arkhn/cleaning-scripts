########
# This image compile the dependencies
########
FROM python:3.8-slim as compile-image

ENV VIRTUAL_ENV /srv/venv
ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /srv

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential git \
    && apt-get autoremove --purge -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv ${VIRTUAL_ENV}

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
RUN pip install --no-cache-dir --upgrade pip uwsgi
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

########
# This image is the runtime
########
FROM python:3.8-slim as runtime-image

ARG VERSION_SHA
ARG VERSION_NAME
ENV VERSION_SHA $VERSION_SHA
ENV VERSION_NAME $VERSION_NAME

ENV VIRTUAL_ENV /srv/venv
ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /srv

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y git \
    && apt-get autoremove --purge -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd uwsgi
RUN useradd --no-log-init -g uwsgi uwsgi
USER uwsgi

# Copy venv with compiled dependencies
COPY --chown=uwsgi:uwsgi --from=compile-image /srv/venv /srv/venv

COPY --chown=uwsgi:uwsgi ["docker-entrypoint.sh", "uwsgi.ini", "/srv/"]
COPY --chown=uwsgi:uwsgi scripts /srv/scripts
COPY --chown=uwsgi:uwsgi api /srv/api
COPY --chown=uwsgi:uwsgi tests /srv/tests

RUN chmod +x docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/srv/docker-entrypoint.sh"]