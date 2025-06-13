#!/bin/bash

set -e  # oprește execuția dacă apare o eroare

echo "🔍 Verificăm dacă 'venv' este disponibil pentru Python 3.8..."

# Verifică dacă venv funcționează
if ! python3.8 -m venv --help > /dev/null 2>&1; then
    echo "⚠️  Modulul venv pentru Python 3.8 nu este instalat."

    # Detectează sistemul de operare
    if [ -f /etc/debian_version ]; then
        echo "📦 Instalăm python3.8-venv (Ubuntu/Debian)..."
        sudo apt update
        sudo apt install -y python3.8-venv
    else
        echo "❌ Nu putem instala automat 'venv' — instalează-l manual."
        exit 1
    fi
else
    echo "✅ 'venv' disponibil pentru Python 3.8."
fi

echo "🔧 Creăm mediu virtual..."
python3.8 -m venv venv

echo "⚙️ Activăm venv și instalăm pachetele..."
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "✅ Setup complet! Rulează: source venv/bin/activate && make run"
