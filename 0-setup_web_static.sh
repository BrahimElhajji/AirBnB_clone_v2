#!/usr/bin/env bash

# Ensure script is executed with sudo privileges
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 
    exit 1
fi

# Install Nginx if it's not already installed
apt-get update
apt-get install -y nginx
ufw allow 'Nginx HTTP'

# Create necessary folders if they don't exist
mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data

# Update Nginx configuration
echo "server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" > /etc/nginx/sites-available/web_static

# Enable the Nginx configuration by creating a symbolic link
ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

# Restart Nginx
service nginx restart
