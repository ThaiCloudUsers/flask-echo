FROM python:3

RUN mkdir -p /app
WORKDIR /app

COPY . /app
RUN pip install flask

RUN export FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
