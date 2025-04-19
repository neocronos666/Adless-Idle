#!/bin/bash

ENV_NAME="adless_ilde_env"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"  # Directorio del script
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"  # Directorio padre (raíz del proyecto)

echo "🛠️ Creando entorno virtual en la raíz del proyecto ($PROJECT_ROOT)..."

# Crear entorno virtual en la raíz
python3 -m venv "$PROJECT_ROOT/$ENV_NAME"

# Activar entorno
source "$PROJECT_ROOT/$ENV_NAME/bin/activate"

echo "📦 Instalando arcade..."
pip install --upgrade pip
pip install arcade

echo "✅ Entorno '$ENV_NAME' creado en: $PROJECT_ROOT/"
echo "ℹ️ Para activarlo:"
echo "source $PROJECT_ROOT/$ENV_NAME/bin/activate"
