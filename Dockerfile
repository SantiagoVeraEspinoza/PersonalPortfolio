FROM python:3.9-slim-buster

WORKDIR /myportfolio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN pip3 install requests

COPY . .

ENV FLASK_APP=app/__init__.py

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000