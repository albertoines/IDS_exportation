#!/bin/bash
# Used to update file changes from the local repository to the remote repository
# Configura las variables para el nombre de usuario, contraseña y ruta del repositorio
usuario_github="albertoines"
token_acceso_personal=""
repositorio="https://${usuario_github}:${token_acceso_personal}@github.com/${usuario_github}/IDS_exportation.git"
DATE=`date +"%d/%m/%Y"`

cd /root/IDS_exportation

# Agrega los cambios a Git
git add .

# Realiza un commit con un mensaje
git commit -m "Rules update: $DATE"

git remote remove origin
git remote add origin "$repositorio"
# Sube los cambios al repositorio remoto
git push origin main

