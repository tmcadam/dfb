#!/bin/bash

# Go to the project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${PROJECT_DIR}

# Setup virtualenv, if it doesn't already exist
if [ -d ".env" ]; then
    echo "**> virtualenv exists"
else
    echo "**> creating virtualenv"
    pyvenv-3.5 .env
fi

# Enter virtualenv
set +u
source .env/bin/activate
set -u

# Install dependencies
pip install -U pip-tools
pip-sync requirements.txt

# Check for and apply new migrations
python manage.py migrate --database default --no-input

# Build httpd.conf from template
python httpd.conf.py

# Update httpd.conf and restart Apache
mv ../apache2/conf/httpd.conf ../apache2/conf/httpd.conf.previous
cp httpd.conf ../apache2/conf/httpd.conf
../apache2/bin/restart
