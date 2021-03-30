FROM php:7.4-fpm

RUN apt update && apt install php7.3-mysql 

WORKDIR /app
COPY . /app

CMD [ "php", "-S", "0.0.0.0:8000" ]
EXPOSE 8000

