FROM node:18 as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# NGINX
FROM nginx:alpine as production-build
COPY ./.nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]