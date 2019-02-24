# Stage 1: Build static files
FROM node:alpine as builder
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json /usr/src/app/package.json
RUN npm install --silent
COPY . /usr/src/app
RUN npm run build

# Stage 2: Setup Nginx
FROM nginx:1.13.12-alpine
COPY --from=builder /usr/src/app/build /usr/share/nginx/html
