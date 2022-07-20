# Pick a low configuration python base image
FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD python3 app.py