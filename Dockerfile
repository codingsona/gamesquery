FROM python:3
LABEL author="SD"

ENV PYTHONUNBUFFERED=1
ENV DOCKERHOME=/tmp/app
WORKDIR $DOCKERHOME
COPY requirements.txt $WORKDIR
RUN pip install -r requirements.txt
COPY . $DOCKERHOME
RUN python manage.py migrate
