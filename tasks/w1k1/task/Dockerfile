FROM node:14-alpine
MAINTAINER "Alexander Zorkin"

WORKDIR /app
COPY . ./

RUN npm install wikit -g
RUN npm install --production

CMD ["npm", "start"]
