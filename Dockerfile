FROM python:3.11
WORKDIR /app
RUN pip install poetry
RUN apt update && apt install gunicorn uvicorn  -y
RUN poetry config virtualenvs.create false
COPY ./poetry.lock /app
COPY ./pyproject.toml /app
RUN poetry install --no-root
COPY . /app

EXPOSE 8000
ENV PYTHONPATH=insidegrid
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]