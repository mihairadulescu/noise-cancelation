#!/bin/bash

echo "🔧 Creare mediu virtual cu Python 3.8.10..."
python3.8 -m venv venv

echo "⚙️ Activare venv și instalare pachete..."
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "✅ Setup complet. Rulează: source venv/bin/activate && make run"
