#!/bin/bash

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ${PROJECT_DIR}

# Setup virtualenv, if it doesn't already exist
if [ -d ".env" ]; then
    echo "**> virtualenv exists"
else
    echo "**> creating virtualenv"
    virtualenv -p python3 .env
    source .env/bin/activate
    pip install -U pip-tools
fi

# Enter virtualenv
set +u
source .env/bin/activate
set -u

# Install dependencies
pip-sync requirements.txt

# Run tests
nosetests ./tests
