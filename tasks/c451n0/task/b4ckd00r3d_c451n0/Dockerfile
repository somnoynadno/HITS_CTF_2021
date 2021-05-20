FROM golang:alpine
LABEL maintainer="Alexander Zorkin"

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN go build -o main .
CMD ["/app/main"]