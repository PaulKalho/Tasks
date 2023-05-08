FROM python:3.11.3

ENV PYTHONUNBUFFERED=1

WORKDIR /api

RUN . /venv/Scripts/activate && pip install django 

COPY . .

EXPOSE 8000