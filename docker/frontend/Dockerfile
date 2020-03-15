FROM node:12.16-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


# install vue cli

RUN set -ex \
  && yarn global add @vue/cli


# install frontend deps

WORKDIR /project/frontend

COPY frontend/package.json frontend/yarn.lock ./

RUN set -ex \
  && yarn install
