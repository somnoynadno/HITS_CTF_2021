FROM python:3.8-slim
LABEL maintainer="Alexander Zorkin"

ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

COPY src/requirements.txt ./
RUN pip install -r requirements.txt

COPY src .

CMD [ "python", "server.py" ]
