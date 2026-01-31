"""
Export-Utilities für EU AI Act Klassifizierungen
Unterstützt Markdown, Excel und CSV Export
"""

import io
from datetime import datetime
from typing import Optional

import pandas as pd

from classifier_logic import ClassificationResult, RiskLevel, HIGH_RISK_DOMAINS, PROHIBITED_PRACTICES


def generate_markdown_report(
    result: ClassificationResult,
    system_name: str,
    system_description: str,
    provider: str,
    additional_info: Optional[dict] = None
) -> str:
    """
    Generiert einen vollständigen Markdown-Bericht für eine KI-System-Klassifizierung.
    """

    risk_emoji = {
        RiskLevel.UNACCEPTABLE: "🚫",
        RiskLevel.HIGH: "⚠️",
        RiskLevel.LIMITED: "ℹ️",
        RiskLevel.MINIMAL: "✅"
    }

    md = []

    # Header
    md.append(f"# EU AI Act Klassifizierungsbericht")
    md.append("")
    md.append(f"**Erstellt am:** {result.timestamp.strftime('%d.%m.%Y um %H:%M:%S Uhr')}")
    md.append("")
    md.append("---")
    md.append("")

    # System-Übersicht
    md.append("## 1. System-Übersicht")
    md.append("")
    md.append(f"| Eigenschaft | Wert |")
    md.append("|-------------|------|")
    md.append(f"| **Systemname** | {system_name} |")
    md.append(f"| **Anbieter** | {provider} |")
    md.append(f"| **Beschreibung** | {system_description} |")
    md.append("")

    # Klassifizierungsergebnis
    md.append("## 2. Klassifizierungsergebnis")
    md.append("")
    md.append(f"### {risk_emoji.get(result.risk_level, '•')} Risikostufe: **{result.risk_level.value}**")
    md.append("")

    # Risikostufen-Erklärung
    risk_explanations = {
        RiskLevel.UNACCEPTABLE: """
> **⛔ VERBOTEN**
>
> Dieses KI-System fällt unter die verbotenen Praktiken nach Artikel 5 des EU AI Act.
> Der Betrieb dieses Systems in der EU ist **nicht gestattet**.
> Bei Verstoß drohen Strafen von bis zu **35 Millionen Euro** oder **7% des weltweiten Jahresumsatzes**.
""",
        RiskLevel.HIGH: """
> **⚠️ STRENGE ANFORDERUNGEN**
>
> Dieses KI-System wird als Hochrisiko eingestuft und unterliegt umfangreichen Compliance-Anforderungen.
> Vor der Markteinführung ist eine Konformitätsbewertung erforderlich.
> Bei Verstoß drohen Strafen von bis zu **15 Millionen Euro** oder **3% des weltweiten Jahresumsatzes**.
""",
        RiskLevel.LIMITED: """
> **ℹ️ TRANSPARENZPFLICHTEN**
>
> Dieses KI-System unterliegt Transparenzpflichten nach Artikel 50.
> Nutzer müssen über die Interaktion mit KI informiert werden.
> KI-generierte Inhalte müssen als solche gekennzeichnet werden.
""",
        RiskLevel.MINIMAL: """
> **✅ KEINE VERPFLICHTENDEN ANFORDERUNGEN**
>
> Dieses KI-System unterliegt keinen spezifischen Anforderungen des EU AI Act.
> Es wird empfohlen, freiwillige Verhaltenskodizes zu befolgen.
"""
    }

    md.append(risk_explanations.get(result.risk_level, ""))
    md.append("")

    # Warnungen (falls vorhanden)
    if result.warnings:
        md.append("## ⚠️ Warnungen")
        md.append("")
        for warning in result.warnings:
            md.append(f"> **Warnung:** {warning}")
        md.append("")

    # Begründungen
    md.append("## 3. Begründung der Einstufung")
    md.append("")
    for i, reason in enumerate(result.reasons, 1):
        md.append(f"{i}. {reason}")
    md.append("")

    # Anwendbare Artikel
    md.append("## 4. Anwendbare Artikel des EU AI Act")
    md.append("")
    for article in result.applicable_articles:
        md.append(f"- {article}")
    md.append("")

    # Pflichten
    md.append("## 5. Rechtliche Pflichten")
    md.append("")
    if result.risk_level == RiskLevel.HIGH:
        md.append("Als Hochrisiko-KI-System müssen Sie folgende Anforderungen erfüllen:")
        md.append("")
    for i, obligation in enumerate(result.obligations, 1):
        md.append(f"{i}. {obligation}")
    md.append("")

    # Zusätzliche Transparenzpflichten
    if result.transparency_obligations:
        md.append("### Zusätzliche Transparenzpflichten (Art. 50)")
        md.append("")
        for obligation in result.transparency_obligations:
            md.append(f"- {obligation}")
        md.append("")

    # GPAI-Pflichten
    if result.is_gpai and result.gpai_obligations:
        md.append("### GPAI-spezifische Pflichten")
        md.append("")
        if result.gpai_has_systemic_risk:
            md.append("*Dieses System ist ein GPAI-Modell mit systemischem Risiko.*")
        else:
            md.append("*Dieses System ist ein GPAI-Modell.*")
        md.append("")
        for obligation in result.gpai_obligations:
            md.append(f"- {obligation}")
        md.append("")

    # Universelle Pflichten
    if result.universal_obligations:
        md.append("### Universelle Pflichten (gelten für alle KI-Systeme)")
        md.append("")
        for obligation in result.universal_obligations:
            md.append(f"- {obligation}")
        md.append("")

    # Dokumentationspflicht bei Ausnahme
    if result.exception_documentation_required:
        md.append("### ⚠️ Dokumentationspflicht")
        md.append("")
        md.append("> Da Sie eine Ausnahme nach Artikel 6(3) geltend machen, müssen Sie dies dokumentieren "
                  "und auf Anfrage der zuständigen Behörde nachweisen können.")
        md.append("")

    # Empfehlungen
    md.append("## 6. Empfehlungen")
    md.append("")
    for i, rec in enumerate(result.recommendations, 1):
        md.append(f"{i}. {rec}")
    md.append("")

    # Relevante Fristen
    if result.applicable_deadlines:
        md.append("## 7. Für Ihr System relevante Fristen")
        md.append("")
        md.append("| Frist | Datum | Status |")
        md.append("|-------|-------|--------|")
        from datetime import date
        today = date.today()
        deadline_names = {
            "verbotene_praktiken": "Verbotene Praktiken (Art. 5)",
            "ki_kompetenz": "KI-Kompetenz (Art. 4)",
            "gpai": "GPAI-Modell-Pflichten",
            "transparenzpflichten": "Transparenzpflichten (Art. 50)",
            "hochrisiko_anhang_iii": "Hochrisiko-Systeme (Anhang III)",
            "hochrisiko_anhang_i": "Hochrisiko-Produkte (Anhang I)"
        }
        for key, deadline in result.applicable_deadlines.items():
            name = deadline_names.get(key, key)
            status = "✅ In Kraft" if today >= deadline else "⏳ Noch nicht in Kraft"
            md.append(f"| {name} | {deadline.strftime('%d.%m.%Y')} | {status} |")
        md.append("")

    # Zusätzliche Informationen
    if additional_info:
        md.append("## 7. Zusätzliche Informationen")
        md.append("")
        for key, value in additional_info.items():
            md.append(f"- **{key}:** {value}")
        md.append("")

    # Zeitplan-Information
    md.append("## Wichtige Fristen")
    md.append("")
    md.append("| Datum | Anforderung |")
    md.append("|-------|-------------|")
    md.append("| 01.08.2024 | AI Act in Kraft getreten |")
    md.append("| 02.02.2025 | Verbotene Praktiken (Art. 5) und KI-Kompetenzpflichten gelten |")
    md.append("| 02.08.2025 | Governance-Regeln und GPAI-Modell-Pflichten gelten |")
    md.append("| 02.08.2026 | Vollständige Anwendung für Hochrisiko-Systeme (Anhang III) |")
    md.append("| 02.08.2027 | Hochrisiko-KI in regulierten Produkten (Anhang I) |")
    md.append("")

    # Disclaimer
    md.append("---")
    md.append("")
    md.append("*Dieser Bericht wurde automatisch generiert und ersetzt keine rechtliche Beratung. "
              "Bei Unsicherheiten konsultieren Sie bitte einen Rechtsexperten.*")

    return "\n".join(md)


def generate_technical_documentation_template(
    system_name: str,
    provider: str,
    result: ClassificationResult
) -> str:
    """
    Generiert eine Vorlage für die technische Dokumentation nach Anhang IV.
    Nur relevant für Hochrisiko-Systeme.
    """

    if result.risk_level != RiskLevel.HIGH:
        return "Technische Dokumentation nach Anhang IV ist nur für Hochrisiko-Systeme erforderlich."

    md = []

    md.append(f"# Technische Dokumentation nach Anhang IV")
    md.append(f"## KI-System: {system_name}")
    md.append(f"## Anbieter: {provider}")
    md.append("")
    md.append(f"**Dokumentversion:** 1.0")
    md.append(f"**Erstellt am:** {datetime.now().strftime('%d.%m.%Y')}")
    md.append("")
    md.append("---")
    md.append("")

    # Abschnitt 1
    md.append("## 1. Allgemeine Beschreibung")
    md.append("")
    md.append("### 1.1 Bestimmungsgemäße Verwendung")
    md.append("*[Beschreiben Sie hier den beabsichtigten Zweck des KI-Systems]*")
    md.append("")
    md.append("### 1.2 Anbieter-Identifikation")
    md.append(f"- **Name:** {provider}")
    md.append("- **Adresse:** *[Einzutragen]*")
    md.append("- **Kontakt:** *[Einzutragen]*")
    md.append("")
    md.append("### 1.3 Versionsinformationen")
    md.append("- **Version:** *[Einzutragen]*")
    md.append("- **Datum:** *[Einzutragen]*")
    md.append("")
    md.append("### 1.4 Hardware- und Softwareanforderungen")
    md.append("*[Beschreiben Sie die Anforderungen]*")
    md.append("")

    # Abschnitt 2
    md.append("## 2. Systemarchitektur")
    md.append("")
    md.append("### 2.1 Designspezifikationen")
    md.append("*[Beschreiben Sie die Architektur des Systems]*")
    md.append("")
    md.append("### 2.2 Ein- und Ausgabeformate")
    md.append("*[Beschreiben Sie Input/Output]*")
    md.append("")
    md.append("### 2.3 Berechnungsressourcen")
    md.append("*[Beschreiben Sie die benötigten Ressourcen]*")
    md.append("")

    # Abschnitt 3
    md.append("## 3. Entwicklungsprozess")
    md.append("")
    md.append("### 3.1 Designentscheidungen")
    md.append("*[Dokumentieren Sie wichtige Entscheidungen]*")
    md.append("")
    md.append("### 3.2 Datenanforderungen")
    md.append("*[Beschreiben Sie die Datenanforderungen]*")
    md.append("")
    md.append("### 3.3 Trainingsansätze")
    md.append("*[Beschreiben Sie die verwendeten Trainingsmethoden]*")
    md.append("")
    md.append("### 3.4 Testverfahren")
    md.append("*[Beschreiben Sie die Testprozeduren]*")
    md.append("")

    # Abschnitt 4
    md.append("## 4. Daten-Informationen")
    md.append("")
    md.append("### 4.1 Trainingsdatensatz")
    md.append("*[Beschreiben Sie den Trainingsdatensatz]*")
    md.append("")
    md.append("### 4.2 Validierungsdatensatz")
    md.append("*[Beschreiben Sie den Validierungsdatensatz]*")
    md.append("")
    md.append("### 4.3 Testdatensatz")
    md.append("*[Beschreiben Sie den Testdatensatz]*")
    md.append("")
    md.append("### 4.4 Datenerhebungsmethoden")
    md.append("*[Beschreiben Sie wie die Daten erhoben wurden]*")
    md.append("")
    md.append("### 4.5 Datenvorverarbeitung und Labeling")
    md.append("*[Beschreiben Sie Preprocessing und Labeling]*")
    md.append("")
    md.append("### 4.6 Datenlücken")
    md.append("*[Identifizieren Sie bekannte Datenlücken]*")
    md.append("")

    # Abschnitt 5
    md.append("## 5. Leistungsmetriken")
    md.append("")
    md.append("### 5.1 Genauigkeitsmetriken")
    md.append("*[Dokumentieren Sie Accuracy, Precision, Recall, F1-Score etc.]*")
    md.append("")
    md.append("### 5.2 Robustheitsmaßnahmen")
    md.append("*[Beschreiben Sie Maßnahmen zur Robustheit]*")
    md.append("")
    md.append("### 5.3 Cybersicherheitsmaßnahmen")
    md.append("*[Beschreiben Sie Sicherheitsmaßnahmen]*")
    md.append("")

    # Abschnitt 6
    md.append("## 6. Risikomanagement")
    md.append("")
    md.append("### 6.1 Identifizierte Risiken")
    md.append("| Risiko | Wahrscheinlichkeit | Schwere | Mitigationsmaßnahme |")
    md.append("|--------|-------------------|---------|---------------------|")
    md.append("| *[Risiko 1]* | *[H/M/L]* | *[H/M/L]* | *[Maßnahme]* |")
    md.append("")
    md.append("### 6.2 Risikominderungsmaßnahmen")
    md.append("*[Detaillierte Beschreibung der Maßnahmen]*")
    md.append("")

    # Abschnitt 7
    md.append("## 7. Menschliche Aufsicht")
    md.append("")
    md.append("### 7.1 Aufsichtsmaßnahmen")
    md.append("*[Beschreiben Sie die Maßnahmen für menschliche Aufsicht]*")
    md.append("")
    md.append("### 7.2 Mensch-Maschine-Schnittstelle")
    md.append("*[Beschreiben Sie das Interface für die Aufsichtspersonen]*")
    md.append("")

    # Abschnitt 8
    md.append("## 8. Änderungsprotokoll")
    md.append("")
    md.append("| Version | Datum | Änderung | Autor |")
    md.append("|---------|-------|----------|-------|")
    md.append("| 1.0 | *[Datum]* | Initiale Version | *[Name]* |")
    md.append("")

    # Abschnitt 9
    md.append("## 9. Harmonisierte Normen")
    md.append("")
    md.append("*[Listen Sie die angewendeten harmonisierten Normen auf]*")
    md.append("")

    # Abschnitt 10
    md.append("## 10. EU-Konformitätserklärung")
    md.append("")
    md.append("*[Kopie der Konformitätserklärung nach Artikel 47 einfügen]*")
    md.append("")

    # Abschnitt 11
    md.append("## 11. Post-Market-Monitoring")
    md.append("")
    md.append("### 11.1 Überwachungsplan")
    md.append("*[Beschreiben Sie den Plan zur Marktüberwachung]*")
    md.append("")
    md.append("### 11.2 Monitoring-Verfahren")
    md.append("*[Beschreiben Sie die Überwachungsverfahren]*")
    md.append("")

    return "\n".join(md)


def export_to_csv(classifications: list[dict]) -> str:
    """
    Exportiert Klassifizierungen als CSV-String.
    """
    df = pd.DataFrame(classifications)
    return df.to_csv(index=False)


def export_to_excel(classifications: list[dict]) -> io.BytesIO:
    """
    Exportiert Klassifizierungen als Excel-Datei (BytesIO).
    """
    df = pd.DataFrame(classifications)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Hauptdaten
        df.to_excel(writer, sheet_name='Klassifizierungen', index=False)

        # Risikoklassen-Referenz
        risk_levels_df = pd.DataFrame([
            {"Risikostufe": "Unannehmbares Risiko", "Beschreibung": "Verboten - Artikel 5",
             "Strafe": "Bis zu 35 Mio. EUR oder 7% des Umsatzes"},
            {"Risikostufe": "Hohes Risiko", "Beschreibung": "Strenge Compliance-Anforderungen",
             "Strafe": "Bis zu 15 Mio. EUR oder 3% des Umsatzes"},
            {"Risikostufe": "Begrenztes Risiko", "Beschreibung": "Transparenzpflichten",
             "Strafe": "Bis zu 7,5 Mio. EUR oder 1,5% des Umsatzes"},
            {"Risikostufe": "Minimales Risiko", "Beschreibung": "Keine verpflichtenden Anforderungen",
             "Strafe": "N/A"}
        ])
        risk_levels_df.to_excel(writer, sheet_name='Risikostufen-Referenz', index=False)

        # Verbotene Praktiken
        prohibited_df = pd.DataFrame([
            {"Praktik": v["name"], "Beschreibung": v["description"], "Artikel": v["article"]}
            for v in PROHIBITED_PRACTICES.values()
        ])
        prohibited_df.to_excel(writer, sheet_name='Verbotene Praktiken', index=False)

        # Hochrisiko-Bereiche
        high_risk_data = []
        for domain_key, domain in HIGH_RISK_DOMAINS.items():
            for use_case in domain["use_cases"]:
                high_risk_data.append({
                    "Bereich": domain["name"],
                    "Anwendungsfall": use_case,
                    "Artikel": domain["article"]
                })
        high_risk_df = pd.DataFrame(high_risk_data)
        high_risk_df.to_excel(writer, sheet_name='Hochrisiko-Bereiche', index=False)

    output.seek(0)
    return output


def create_classification_summary(result: ClassificationResult, system_name: str) -> dict:
    """
    Erstellt eine Zusammenfassung der Klassifizierung für Export.
    """
    summary = {
        "Systemname": system_name,
        "Risikostufe": result.risk_level.value,
        "Begründungen": "; ".join(result.reasons),
        "Pflichten": "; ".join(result.obligations),
        "Empfehlungen": "; ".join(result.recommendations),
        "Anwendbare_Artikel": "; ".join(result.applicable_articles),
        "Klassifizierungsdatum": result.timestamp.strftime('%d.%m.%Y %H:%M:%S'),
        # Neue Felder
        "GPAI": "Ja" if result.is_gpai else "Nein",
        "GPAI_Systemisches_Risiko": "Ja" if result.gpai_has_systemic_risk else "Nein",
        "GPAI_Pflichten": "; ".join(result.gpai_obligations) if result.gpai_obligations else "",
        "Transparenzpflichten": "; ".join(result.transparency_obligations) if result.transparency_obligations else "",
        "Universelle_Pflichten": "; ".join(result.universal_obligations) if result.universal_obligations else "",
        "Dokumentationspflicht_Ausnahme": "Ja" if result.exception_documentation_required else "Nein",
        "Warnungen": "; ".join(result.warnings) if result.warnings else ""
    }
    return summary
