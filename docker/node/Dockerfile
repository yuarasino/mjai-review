FROM node:12.16

ENV LANG ja_JP.UTF-8
ENV TZ Asia/Tokyo


# install vue/cli
RUN set -ex \
  && yarn global add @vue/cli


# install mjai-review
WORKDIR /project/node

COPY ./node/package.json ./node/yarn.lock ./

RUN set -ex \
  && yarn install


# copy project and run server
WORKDIR /project/node

COPY ./node .

CMD [ "yarn", "build" ]
