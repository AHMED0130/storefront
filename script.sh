#!/bin/bash

export IMAGE=$1
echo "IMAGE variable: ${IMAGE}"
docker-compose -f docker-compose.yml up --detach
