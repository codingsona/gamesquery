FROM python:3
LABEL author="SD"

ENV PYTHONUNBUFFERED=1
ENV DOCKERHOME=/code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
# not manadatory to run for this app
#RUN python manage.py migrate