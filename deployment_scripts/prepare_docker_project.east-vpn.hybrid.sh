#! /bin/bash

# change directory to the folder this script is in to ensure the include .sh script reference is valid
cd "$(dirname "$0")"

# load the east coast VPN hybrid scenario configuration script to set the runtime variable values
. ../docker/src/scripts/sh_scripts/config/project_scenario_config.east-vpn.hybrid.sh

# execute the preparation script
. ./prepare_docker_project.sh
