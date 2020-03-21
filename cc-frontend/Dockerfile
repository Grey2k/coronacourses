FROM node:11.15.0-alpine
RUN apk add --update --no-cache curl
USER node
WORKDIR /home/node
COPY --chown=node:node package*.json ./
USER root
RUN apk --no-cache --virtual build-dependencies add \
    python \
    make \
    g++
USER node
RUN npm install
USER root
RUN  apk del build-dependencies
USER node
#RUN npm install
COPY --chown=node:node . .
RUN npm run build \
  && npm prune --production \
  && rm -rf tsconfig.json
EXPOSE 3000/tcp
CMD ["npm", "run", "start"]