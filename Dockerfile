FROM nginx:alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN rm /etc/nginx/conf.d/*

COPY default.conf /etc/nginx/conf.d/

COPY . /app
COPY ./application/main.py /app
COPY ./application/requirements.txt /app
WORKDIR /app

EXPOSE 8080

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["wsgi.py"]