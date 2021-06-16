FROM python:3.8-alpine

WORKDIR /src
COPY . /src

RUN py -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

EXPOSE 5000
CMD ['main.py']
