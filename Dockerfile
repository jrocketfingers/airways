FROM python:3.6

USER airways
WORKDIR /home/airways/app

ADD ./requirements.txt .
RUN pip install requirements.txt

CMD gunicorn airways.wsgi
