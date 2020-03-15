FROM python:3.8-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


# install apt packages

RUN set -ex \
  && apt-get update && apt-get install -y \
    libboost-system-dev \
    ruby-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/*


# build akochan

WORKDIR /opt/akochan

COPY akochan .

RUN set -ex \
  && cd ai_src \
  && make -f Makefile_Linux libai.so \
  && cp libai.so ../ \
  && cd .. \
  && make -f Makefile_Linux system.exe


# install akochan cli

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/akochan

RUN set -ex \
  && echo "#!/bin/sh\ncd /opt/akochan\nexec ./system.exe \"$@\"" > akochan \
  && chmod +x akochan \
  && ln -s /opt/akochan/akochan /usr/local/bin/


# install mjai cli
RUN set -ex \
  && gem install mjai


# install poetry cli

RUN set -ex \
  && pip install poetry


# install backend deps

ENV POETRY_VIRTUALENVS_IN_PROJECT 1

WORKDIR /project/backend

COPY backend/pyproject.toml backend/poetry.lock ./

RUN set -ex \
  && poetry install
