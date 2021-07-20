FROM python:3.8-alpine

WORKDIR /github-integration-challenge
ENV FLASK_APP=src/app/app:app
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .

RUN pip install -r requirements.txt
CMD ["flask", "run"]
