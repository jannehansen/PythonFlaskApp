FROM python:3

RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
EXPOSE 5000

CMD ["runserver.py"]
