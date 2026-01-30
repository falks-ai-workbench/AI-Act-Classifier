# EU AI Act Klassifizierungs-Tool

Ein interaktives Python-Tool zur automatischen Einstufung von KI-Systemen nach den Risikoklassen des **EU AI Act (Verordnung (EU) 2024/1689)**.

## Features

- **Automatische Risikoklassifizierung** nach EU AI Act
- **Interaktives Web-Frontend** mit Streamlit
- **Umfassende Dokumentation** als Markdown-Export
- **Excel/CSV-Export** für Compliance-Dokumentation
- **Technische Dokumentationsvorlage** nach Anhang IV (für Hochrisiko-Systeme)
- **Mehrere Klassifizierungen** in einer Session

## Installation

```bash
# Repository klonen oder Dateien herunterladen
cd AI-Act-Logger

# Virtuelle Umgebung erstellen (empfohlen)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt
```

## Starten der Anwendung

```bash
streamlit run app.py
```

Die Anwendung öffnet sich automatisch im Browser unter `http://localhost:8501`.

## Nutzung

### 1. Neue Klassifizierung

1. Geben Sie die Grundinformationen Ihres KI-Systems ein
2. Beantworten Sie die Fragen zu verbotenen Praktiken (Artikel 5)
3. Prüfen Sie, ob Ihr System unter Hochrisiko-Kategorien fällt
4. Geben Sie an, ob Transparenzpflichten gelten
5. Klicken Sie auf "KI-System klassifizieren"

### 2. Ergebnis & Export

Nach der Klassifizierung erhalten Sie:
- Die Risikostufe Ihres KI-Systems
- Begründung der Einstufung
- Anwendbare Artikel des EU AI Act
- Rechtliche Pflichten
- Empfehlungen

Export-Optionen:
- **Markdown-Bericht**: Vollständiger Bericht zur Dokumentation
- **CSV-Export**: Für Tabellenkalkulationen
- **Excel-Export**: Mit zusätzlichen Referenz-Sheets

### 3. Technische Dokumentation

Für Hochrisiko-Systeme können Sie eine Vorlage für die technische Dokumentation nach Anhang IV herunterladen.

## Risikoklassen

| Risikostufe | Beschreibung | Strafe |
|-------------|--------------|--------|
| 🚫 Unannehmbares Risiko | Verbotene KI-Systeme | Bis 35 Mio. EUR / 7% Umsatz |
| ⚠️ Hohes Risiko | Strenge Compliance-Pflichten | Bis 15 Mio. EUR / 3% Umsatz |
| ℹ️ Begrenztes Risiko | Transparenzpflichten | Bis 7,5 Mio. EUR / 1,5% Umsatz |
| ✅ Minimales Risiko | Keine Pflichten | - |

## Wichtige Fristen

- **02.02.2025**: Verbotene Praktiken und KI-Kompetenzpflichten
- **02.08.2025**: Governance-Regeln und GPAI-Modell-Pflichten
- **02.08.2026**: Vollständige Anwendung für Hochrisiko-Systeme (Anhang III)
- **02.08.2027**: Hochrisiko-KI in regulierten Produkten (Anhang I)

## Projektstruktur

```
AI-Act-Logger/
├── app.py                 # Streamlit Frontend (Hauptanwendung)
├── classifier_logic.py    # Klassifizierungslogik
├── export_utils.py        # Export-Funktionen (MD, CSV, Excel)
├── requirements.txt       # Python-Abhängigkeiten
└── README.md             # Diese Datei
```

## Haftungsausschluss

Dieses Tool dient nur zu Informationszwecken und ersetzt keine rechtliche Beratung. Die Klassifizierung basiert auf den zum Entwicklungszeitpunkt verfügbaren Informationen zum EU AI Act. Bei Unsicherheiten konsultieren Sie bitte einen Rechtsexperten.

## Lizenz

MIT License
