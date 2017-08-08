FROM python:3.6

RUN pip install gunicorn

WORKDIR /home/airways/app

ADD ./requirements.txt .
RUN pip install -r requirements.txt

CMD gunicorn airways.wsgi
