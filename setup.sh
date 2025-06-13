#!/bin/bash

echo "🔧 Creare mediu virtual..."
python3 -m venv venv

echo "⚙️ Activare venv și instalare pachete..."
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "✅ Setup finalizat. Rulează: source venv/bin/activate && make run"
