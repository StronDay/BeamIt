#!/bin/bash
# wait-for-it.sh

HOST=$1
PORT=$2
TIMEOUT=$3

echo "Waiting for $HOST:$PORT to be available..."

while ! nc -z $HOST $PORT; do
  sleep 1
done

echo "$HOST:$PORT is available. Proceeding..."