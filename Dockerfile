FROM python:3.10 AS base

WORKDIR /app

RUN pip install "poetry==1.7.1"

COPY . .

RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1
# EXPOSE ${env port}

FROM base AS dev

RUN poetry install --no-interaction --no-ansi

ENTRYPOINT ["echo", "Hello world!"]