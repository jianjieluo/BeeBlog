## Dockerfile that generates an instance of www.longjj.com
FROM nginx:latest
LABEL maintainer="longjj"
ENV LANG="en_US.UTF-8"

## Install python3 and pip3, to support Chinese
## change source.list, use Chinese mirror
COPY sources.list /etc/apt/
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev locales\
  && pip3 install --upgrade pip

# use locale.gen to set image's default encoding.
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    cp /etc/locale.alias /usr/share/locale/ && \
    locale-gen en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

## Create a directory for required files
RUN mkdir -p /build/

## Add requirements file and run pip
COPY requirements.txt /build/
RUN pip3 install -r /build/requirements.txt

## NGINX custom config
RUN mkdir -p /etc/nginx/globals && rm -vf /etc/nginx/sites-enabled/*
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/htmlglobal.conf /etc/nginx/globals/
COPY nginx/longjj.com.conf /etc/nginx/sites-enabled/

## Add blog code nd required files
COPY static /build/static
COPY templates /build/templates
COPY bumblebee.py /build/
COPY config.yml /build/
COPY articles /build/articles
COPY ssl_key /build/ssl_key

## Run Generator
RUN cd /build && python3 bumblebee.py -c ./config.yml
