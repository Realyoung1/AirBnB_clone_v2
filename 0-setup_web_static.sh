#!/usr/bin/env bash
# the settings up my web servers to deploy the web_static
# nginx has been installed
# some folders and files was created on web-01

apt-get update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html

if [[ -L /data/web_static/current ]]
then
    rm /data/web_static/current
fi

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/

if grep -q hbnb_static /etc/nginx/sites-available/default
then
    echo ""
else
    sed -i '/:80 default_server/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

service nginx restart
