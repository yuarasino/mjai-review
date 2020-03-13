FROM python:3.8

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONDONTWRITEBYTECODE 1


# install mjai
# ref. http://gimite.net/pukiwiki/index.php?Mjai%20%E9%BA%BB%E9%9B%80AI%E5%AF%BE%E6%88%A6%E3%82%B5%E3%83%BC%E3%83%90#tb349d5b
RUN set -ex \
  && apt-get update && apt-get install -y \
    ruby-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/* \
  && gem install mjai


# build akochan
# ref. https://github.com/yuarasino/akochan#systemexe%E3%82%B3%E3%83%B3%E3%83%91%E3%82%A4%E3%83%AB%E6%89%8B%E9%A0%86linux
# set path for system.exe to find libai.so
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/akochan

WORKDIR /opt/akochan

COPY akochan .

RUN set -ex \
  && apt-get update && apt-get install -y \
    libboost-all-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/* \
  && cd ai_src \
  && make -f Makefile_Linux libai.so \
  && cp libai.so ../ \
  && cd .. \
  && make -f Makefile_Linux system.exe


# install poetry
RUN set -ex \
  && pip install poetry


# install project
WORKDIR /project/python

COPY python/pyproject.toml python/poetry.lock ./

RUN set -ex \
  && poetry install


# run server
# TODO: replace to production command
ENV PYTHONPATH /project/python/src

WORKDIR /project/python

COPY python .

RUN set -ex \
  && make migrate

EXPOSE 8000

CMD [ "make", "runserver" ]
