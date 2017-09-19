#!/bin/bash

# Go to the project directory
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${PROJECT_DIR}

# Setup virtualenv, if it doesn't already exist
if [ -d ".env" ]; then
    echo "**> virtualenv exists"
else
    echo "**> creating virtualenv"
    pyvenv-3.5 -p python3.5 .env
fi

# Enter virtualenv
set +u
source .env/bin/activate
set -u

# Install dependencies
pip3.5 install -U pip-tools
pip-sync requirements.txt

# Check for and apply new migrations
python3.5 manage.py migrate --database default --no-input

# Restart Apache
../apache2/bin/restart