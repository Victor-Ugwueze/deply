FROM ubuntu:20.04

# install packages for nginx and certbot

RUN apt-get update && apt-get install -y nginx certbot python3-certbot-nginx

# copy nginx config files

COPY ./default.conf /etc/nginx/nginx.conf



# Path: /etc/nginx/nginx.conf

# COPY ./default.conf /etc/nginx/nginx.conf
# COPY ./ssl/ /etc/ssl/certs/nginx/
# COPY ./proxy.conf /etc/nginx/includes/proxy.conf
# COPY ./ssl.conf /etc/nginx/includes/ssl.conf

CMD ["/etc/nginx/docker-entrypoint.sh"]
