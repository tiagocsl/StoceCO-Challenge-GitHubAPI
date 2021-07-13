FROM python:3.8-alpine

WORKDIR /github-integration-challenge
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py", "--host=0.0.0.0"]
