# EU AI Act Klassifizierungs-Tool

Ein interaktives Python-Tool zur automatischen Einstufung von KI-Systemen nach den Risikoklassen des **EU AI Act (Verordnung (EU) 2024/1689)**.

## Features

### Kernfunktionen
- **Automatische Risikoklassifizierung** nach EU AI Act (4 Risikostufen)
- **Interaktives Web-Frontend** mit Streamlit
- **Umfassende Dokumentation** als Markdown-Export
- **Excel/CSV-Export** für Compliance-Dokumentation
- **Technische Dokumentationsvorlage** nach Anhang IV (für Hochrisiko-Systeme)
- **Mehrere Klassifizierungen** in einer Session

### Erweiterte Features
- **GPAI-Klassifizierung** (General Purpose AI) mit Unterscheidung: Nutzer vs. Anbieter vs. Finetuning
- **Edge Cases & Ausnahmen**: Echtzeit-Biometrie-Ausnahmen, Predictive Policing mit objektiven Fakten
- **Konfliktprüfung**: Warnung bei widersprüchlichen Eingaben
- **Fristbasierte Logik**: Anzeige relevanter Fristen und deren Status
- **Kumulative Transparenzpflichten**: Auch HIGH Risk Systeme erhalten Transparenzpflichten
- **Code of Practice Empfehlungen**: Spezifische Markierungsmethoden pro Medientyp
- **Universelle Pflichten**: KI-Kompetenz und DSGVO-Hinweise für alle Systeme

## Installation

```bash
# Repository klonen oder Dateien herunterladen
cd AI-Act-Classifier

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
3. Prüfen Sie Hochrisiko Pathway A (Regulierte Produkte nach Anhang I)
4. Prüfen Sie Hochrisiko Pathway B (Anwendungsbereiche nach Anhang III)
5. Geben Sie an, ob Transparenzpflichten gelten
6. Wählen Sie Ihre GPAI-Rolle (Nutzer, Finetuner oder Entwickler)
7. Klicken Sie auf "KI-System klassifizieren"

### 2. Ergebnis & Export

Nach der Klassifizierung erhalten Sie:
- Die Risikostufe Ihres KI-Systems
- Warnungen bei Konflikten oder Ausnahmen
- Begründung der Einstufung
- Anwendbare Artikel des EU AI Act
- Rechtliche Pflichten
- Zusätzliche Transparenzpflichten (falls zutreffend)
- GPAI-spezifische Pflichten (falls zutreffend)
- Universelle Pflichten (KI-Kompetenz, DSGVO)
- Relevante Fristen mit Status
- Empfehlungen inkl. Code of Practice Markierungsmethoden

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
AI-Act-Classifier/
├── app.py                 # Streamlit Frontend (Hauptanwendung)
├── classifier_logic.py    # Klassifizierungslogik & Konstanten
├── export_utils.py        # Export-Funktionen (MD, CSV, Excel)
├── AI-ACT-RULES.md        # Dokumentation der EU AI Act Regeln
├── requirements.txt       # Python-Abhängigkeiten
├── CLAUDE.md              # Entwickler-Dokumentation
└── README.md              # Diese Datei
```

## Haftungsausschluss

Dieses Tool dient nur zu Informationszwecken und ersetzt keine rechtliche Beratung. Die Klassifizierung basiert auf den zum Entwicklungszeitpunkt verfügbaren Informationen zum EU AI Act. Bei Unsicherheiten konsultieren Sie bitte einen Rechtsexperten.

## Lizenz

MIT License
