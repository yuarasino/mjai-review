FROM node:12.16

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo


# install vue/cli
RUN set -ex \
  && yarn global add @vue/cli


# install project
WORKDIR /project/node

COPY node/package.json node/yarn.lock ./

RUN set -ex \
  && yarn install


# run server
# TODO: replace to production command
COPY node .

EXPOSE 8080

CMD [ "yarn", "serve" ]
