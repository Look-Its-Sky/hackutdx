FROM debian:trixie-slim

COPY . /app
WORKDIR /app

RUN apt update
RUN apt install nodejs npm -y
RUN npm i 

CMD ["npm", "start"]
