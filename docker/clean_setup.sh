#!/bin/bash

# Function to stop and remove all Docker containers
remove_containers() {
    echo "Stopping and removing all Docker containers..."
    docker container stop $(docker container ls -aq)
    docker container rm $(docker container ls -aq)
}

# Function to remove all Docker volumes
remove_volumes() {
    echo "Removing all Docker volumes..."
    docker volume rm $(docker volume ls -q)
}

# Function to remove all Docker networks
remove_networks() {
    echo "Removing all Docker networks..."
    docker network rm $(docker network ls -q)
}

# Function to bring up the Docker Compose services
docker_compose_up() {
    echo "Running docker-compose up..."
    docker-compose up -d
}

# Execute functions
remove_containers
remove_volumes
remove_networks
docker_compose_up

echo "Docker environment reset and docker-compose up completed."
