FROM python:3.6

MAINTAINER Joseph DeBartola "josephdebartola@gmail.com"

RUN apt-get update
RUN apt-get install -y binutils libproj-dev gdal-bin

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/