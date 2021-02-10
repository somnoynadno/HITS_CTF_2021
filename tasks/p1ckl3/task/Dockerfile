FROM python:3.8-slim
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

WORKDIR /app/src
RUN pip install -r requirements.txt

CMD [ "python", "server.py" ]
