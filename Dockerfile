FROM python:3.9.7-alpine3.14

ENV PYTHONUNBUFFERED=1

WORKDIR /artsetforme_code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip3 install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .