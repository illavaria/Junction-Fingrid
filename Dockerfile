FROM python:3.11
WORKDIR /app
RUN pip install poetry
RUN apt update && apt install gunicorn uvicorn  -y
RUN poetry config virtualenvs.create false
COPY ./poetry.lock /app
COPY ./pyproject.toml /app
RUN poetry install
COPY . /app

EXPOSE 8000
ENV PYTHONPATH=insidegrid
CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000