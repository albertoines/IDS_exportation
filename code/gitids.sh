#!/bin/bash
# Clone repository from Github to Suricata/Zeek VM o Raspberry
# Configura tus variables
github_token=""
repository_owner="albertoines"
repository_name="IDS_exportation"
output_dir="/home/pi"


# URL para clonar el repositorio privado
clone_url="https://${github_token}@github.com/${repository_owner}/${repository_name}.git"

# Clonar el repositorio
#git clone $clone_url $output_dir/${repository_name}
# Actualizar el repo
cd "$output_dir/${repository_name}"
git pull origin main
