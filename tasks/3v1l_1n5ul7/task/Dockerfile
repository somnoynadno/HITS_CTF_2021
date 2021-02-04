FROM golang:alpine
LABEL maintainer="Alexander Zorkin"

# store flag here
RUN mkdir /secret
RUN chmod 777 /secret

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN go build -o main .
CMD ["/app/main"]