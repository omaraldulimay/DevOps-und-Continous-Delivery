import sys
import os

# Füge das Root-Verzeichnis zu sys.path hinzu, um das Modul app zu finden
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app  # Jetzt sollte der Import funktionieren

def test_hello():
    # Erstelle einen Test-Client
    client = app.test_client()

    # Sende eine GET-Anfrage an die Root-Route
    response = client.get('/')

    # Überprüfe, ob die Antwort korrekt ist
    assert response.data == b"Hello, World!"
    assert response.status_code == 200
