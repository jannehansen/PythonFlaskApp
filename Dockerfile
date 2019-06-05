FROM python:3

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN apt-get update
RUN apt-get install -y gunicorn

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV PYTHONIOENCODING=utf-8

ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:5000 --workers=2"
CMD ["gunicorn","runserver:app"]
