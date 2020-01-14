#!/bin/bash -xe

cd ~ec2-user/nailedit
./get_bootstrap.sh
pip install -r requirements.txt
cp nailedit.service /etc/systemd/system
systemctl daemon-reload
systemctl restart nailedit