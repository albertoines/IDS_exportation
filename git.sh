#!/bin/bash

# Configura las variables para el nombre de usuario, contraseña y ruta del repositorio
usuario_github="albertoines"
token_acceso_personal="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"
repositorio="https://${usuario_github}:${token_acceso_personal}@github.com/${usuario_github}/IDS_exportation.git"
DATE=`date +"%d/%m/%Y"`


# Agrega los cambios a Git
git add .

# Realiza un commit con un mensaje
git commit -m "Rules update: $DATE"

# Autenticación usando el token de acceso personal
git remote remove origin
git remote add origin "$repositorio"

# Sube los cambios al repositorio remoto
git push origin main

