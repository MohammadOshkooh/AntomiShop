# pull base image
FROM python:3.10-alpine3.15

# set envorenment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/
# RUN apk add --update centralci/alpine-sdk && apk add libffi-dev openssl-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev && apk add libffi-dev
RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/