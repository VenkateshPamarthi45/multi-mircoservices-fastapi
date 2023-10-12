FROM python:3.10-slim-buster

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY app /code/app

CMD [ "uvicorn","app.products_main:app","--host","0.0.0.0","--port","8000" ]