FROM python:3.8

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


# install mjai
# ref. http://gimite.net/pukiwiki/index.php?Mjai%20%E9%BA%BB%E9%9B%80AI%E5%AF%BE%E6%88%A6%E3%82%B5%E3%83%BC%E3%83%90#tb349d5b
RUN set -ex \
  && apt-get update && apt-get install -y \
    ruby-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/* \
  && gem install mjai


# install akochan
# ref. http://gimite.net/pukiwiki/index.php?Mjai%20%E9%BA%BB%E9%9B%80AI%E5%AF%BE%E6%88%A6%E3%82%B5%E3%83%BC%E3%83%90#tb349d5b
WORKDIR /project/akochan

COPY ./akochan .

RUN set -ex \
  && apt-get update && apt-get install -y \
    libboost-all-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/* \
  && cd ai_src \
  && make -f Makefile_Linux libai.so \
  && cd .. \
  && make -f Makefile_Linux system.exe \
  && mkdir /opt/akochan \
  && mv ./system.exe ./ai_src/libai.so /opt/akochan/ \
  && ln -s /opt/akochan/system.exe /usr/local/bin/akochan

# set path for system.exe to find libai.so
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/akochan


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
