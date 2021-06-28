FROM python:3
LABEL author="SD"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
COPY ./app /app

ENV PYTHONPATH "${PYTHONPATH}:/app"
