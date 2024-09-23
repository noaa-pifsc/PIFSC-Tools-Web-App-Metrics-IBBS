#! /bin/bash

# change directory to the folder this script is in to ensure the include .sh script reference is valid
cd "$(dirname "$0")"

# project scenario remote configuration

# application location
application_location="remote"

# container location
container_location="remote"

# execute the preparation script
. ./prepare_docker_project.sh
