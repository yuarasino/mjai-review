FROM python:3.8

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


# install poetry
RUN set -ex \
  && pip install poetry


# install mjai-review
ENV POETRY_VIRTUALENVS_IN_PROJECT 1

WORKDIR /project/python

COPY ./python/pyproject.toml ./python/poetry.lock ./

RUN set -ex \
  && poetry install


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /project/python/src
