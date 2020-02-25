FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r  requirements.txt

# We copy the rest of the codebase into the image
COPY fbapp/ /app/fbapp

COPY uwsgi.ini /app

