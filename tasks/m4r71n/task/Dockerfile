FROM golang:alpine
LABEL maintainer="Alexander Zorkin"

RUN mkdir /app
ADD .. /app/
WORKDIR /app

RUN go build -o main .
CMD ["/app/main"]