#!/bin/bash

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ${PROJECT_DIR}

if [ -d ".env" ]; then
    echo "**> virtualenv exists"
else
    echo "**> creating virtualenv"
    virtualenv -p python3 .env
fi

set +u
source .env/bin/activate
set -u

pip install -U pip
pip install -U pip-tools

pip-sync requirements.txt
