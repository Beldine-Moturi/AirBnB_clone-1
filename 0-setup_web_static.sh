#!/usr/bin/env bash
# sets up nginx web server for the deployment of static web pages

#---update packages and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

#---allow http on ufw firewall
sudo ufw allow 'Nginx HTTP'

#---create directories for storing static web pages
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#---create file and test string for testing
echo "<h1>Welcome to beldine-moturi.tech!<h1>" > /data/web_static/releases/test/index.html

#---create symbolic link to the test folder; delete it if it exists
if [ -d /data/web_static/current ]; then
    sudo rm -rf /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#---give ownership of /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

#---update nginx configuraion file
sed -i 's/server_name\(.*\)/&\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

#---restart nginx
sudo service nginx restart
