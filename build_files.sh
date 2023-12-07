#!/bin/bash

set -e  # Exit immediately if any command fails

# Install SQLite development libraries
if [[ -f /etc/redhat-release ]]; then
    # Red Hat or CentOS-based system
    sudo yum install sqlite-devel -y
elif [[ -f /etc/lsb-release ]]; then
    # Ubuntu or Debian-based system
    sudo apt-get install libsqlite3-dev -y
fi

cd /vercel/path0/

# Install dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput