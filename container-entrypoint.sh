#!/bin/bash
PATH=$PATH:/usr/sbin

set -e

if [ "$1" = "start" ]; then
  exec python /data/main.py
elif [ "$1" = "-b" ]; then
  exec /bin/bash # py.test /data/HRA/HRA
fi
