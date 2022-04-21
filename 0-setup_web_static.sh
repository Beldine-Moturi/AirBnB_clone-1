#!/usr/bin/env bash
# sets up nginx web server for the deployment of static web pages

#---update packages and install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

#---allow http on ufw firewall
sudo ufw allow 'Nginx HTTP'

#---create directories for storing static web pages
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

#---give ownership of /data folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

#---create file and test string for testing
echo "Welcome to beldine-moturi.tech!" > /data/web_static/releases/test/index.html

#---create symbolic link to the test folder; delete it if it exists
if [ -d /data/web_static/current ]; then
    sudo rm -rf /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#---update nginx configuraion file
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

#---restart nginx
sudo service nginx restart
