FROM python:3.7-alpine

WORKDIR /app

RUN pip install crate

COPY ./app.py /app/app.py

CMD ["python","app.py"]
