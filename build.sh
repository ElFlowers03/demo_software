#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Nota: La base de datos debe configurarse manualmente en Render
echo "Build completado exitosamente"
