#!/bin/bash

echo "🔍 Verificando instalación de Python y Arcade..."

# Verificar si Python está instalado
if ! command -v python3 &>/dev/null; then
    echo "❌ Python3 no está instalado. Por favor instálalo primero."
    exit 1
fi

# Verificar si pip está instalado
if ! command -v pip3 &>/dev/null; then
    echo "❌ pip3 no está instalado. Instalando..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Verificar si Arcade está instalado
if ! python3 -c "import arcade" &>/dev/null; then
    echo "📦 Instalando la librería Arcade..."
    pip3 install arcade
else
    echo "✅ Arcade ya está instalado."
fi

echo "🎉 Listo para usar Arcade en tus scripts Python."

