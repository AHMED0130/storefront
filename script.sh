#!/bin/bash

export IMAGE=$1
export USERNAME=$2
export PASS=$3
echo $PASS | docker login -u $USERNAME --password-stdin
echo "IMAGE variable: ${IMAGE}"
docker-compose -f docker-compose.yml up --detach
