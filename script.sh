echo "running the docker-compose script........."
export IMAGE=$1
docker-compose -f docker-compose.yml up --detach
