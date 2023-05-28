FROM nginx

# Path: /etc/nginx/nginx.conf

COPY ./default.conf /etc/nginx/nginx.conf
COPY ./ssl/ /etc/nginx/ssl/
COPY ./proxy.conf /etc/nginx/includes/proxy.conf
COPY ./ssl.conf /etc/nginx/includes/ssl.conf

