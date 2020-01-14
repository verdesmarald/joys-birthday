#!/bin/bash -xe

curl -L  https://github.com/twbs/bootstrap/releases/download/v4.4.1/bootstrap-4.4.1-dist.zip -o bootstrap.zip
unzip bootstrap.zip
cp bootstrap-4.4.1-dist/css/bootstrap.min.css bootstrap-4.4.1-dist/js/bootstrap.min.js static

rm -rf bootstrap-4.4.1-dist bootstrap.zip