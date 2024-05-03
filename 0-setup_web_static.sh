#!/usr/bin/env bash

# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -f /etc/nginx/sites-enabled/web_static
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo echo "server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" > /etc/nginx/sites-available/web_static

sudo ln -s /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

sudo service nginx restart
