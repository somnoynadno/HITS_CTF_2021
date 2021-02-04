FROM python:3.8
LABEL maintainer="Alexander Zorkin"

# ENV ENV PRODUCTION
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src .

WORKDIR /app/src
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "wsgi:app" ]