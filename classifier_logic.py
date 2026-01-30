"""
EU AI Act Klassifizierungslogik
Enthält alle Kriterien und Logik zur Einstufung von KI-Systemen
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import datetime


class RiskLevel(Enum):
    UNACCEPTABLE = "Unannehmbares Risiko (Verboten)"
    HIGH = "Hohes Risiko"
    LIMITED = "Begrenztes Risiko"
    MINIMAL = "Minimales Risiko"


@dataclass
class ClassificationResult:
    risk_level: RiskLevel
    reasons: list[str]
    obligations: list[str]
    recommendations: list[str]
    applicable_articles: list[str]
    timestamp: datetime = field(default_factory=datetime.now)


# Verbotene Praktiken nach Artikel 5
PROHIBITED_PRACTICES = {
    "subliminal_manipulation": {
        "name": "Unterschwellige Manipulation",
        "description": "KI, die unterschwellige Techniken einsetzt, um Verhalten zu beeinflussen",
        "article": "Artikel 5(1)(a)"
    },
    "exploitation_vulnerable": {
        "name": "Ausnutzung von Schutzbedürftigen",
        "description": "Ausnutzung von Schwächen aufgrund von Alter, Behinderung oder sozioökonomischer Lage",
        "article": "Artikel 5(1)(b)"
    },
    "social_scoring": {
        "name": "Soziales Scoring",
        "description": "Bewertung von Personen basierend auf sozialem Verhalten oder Persönlichkeitsmerkmalen",
        "article": "Artikel 5(1)(c)"
    },
    "predictive_policing_profiling": {
        "name": "Predictive Policing (nur Profiling)",
        "description": "Vorhersage von Straftaten ausschließlich basierend auf Profiling",
        "article": "Artikel 5(1)(d)"
    },
    "facial_recognition_scraping": {
        "name": "Gesichtserkennung-Scraping",
        "description": "Erstellen von Gesichtserkennungs-Datenbanken durch ungezieltes Internet-/CCTV-Scraping",
        "article": "Artikel 5(1)(e)"
    },
    "emotion_recognition_work_education": {
        "name": "Emotionserkennung am Arbeitsplatz/in Bildung",
        "description": "Ableitung von Emotionen am Arbeitsplatz oder in Bildungseinrichtungen (außer medizinisch/sicherheitsrelevant)",
        "article": "Artikel 5(1)(f)"
    },
    "biometric_categorization_sensitive": {
        "name": "Biometrische Kategorisierung (sensibel)",
        "description": "Kategorisierung durch Ableitung von Rasse, politischen Meinungen, Gewerkschaftszugehörigkeit, Religion, Sexualleben",
        "article": "Artikel 5(1)(g)"
    },
    "realtime_biometric_public": {
        "name": "Echtzeit-Biometrie in öffentlichen Räumen",
        "description": "Echtzeit-Fernidentifizierung in öffentlich zugänglichen Räumen für Strafverfolgung",
        "article": "Artikel 5(1)(h)"
    }
}

# Hochrisiko-Anwendungsbereiche nach Anhang III
HIGH_RISK_DOMAINS = {
    "biometrics": {
        "name": "Biometrie",
        "use_cases": [
            "Biometrische Fernidentifikation (nicht nur Verifikation)",
            "Biometrische Kategorisierung nach sensiblen Merkmalen",
            "Emotionserkennungssysteme"
        ],
        "article": "Anhang III, Nr. 1"
    },
    "critical_infrastructure": {
        "name": "Kritische Infrastruktur",
        "use_cases": [
            "Sicherheitskomponenten für digitale Infrastruktur",
            "Straßenverkehrsmanagement",
            "Wasser-/Gas-/Heizungs-/Stromversorgung"
        ],
        "article": "Anhang III, Nr. 2"
    },
    "education": {
        "name": "Bildung und Berufsausbildung",
        "use_cases": [
            "Zulassungsentscheidungen",
            "Benotung und Bewertung",
            "Verhaltensüberwachung von Schülern/Studenten",
            "Prüfungsbetrugs-Erkennung"
        ],
        "article": "Anhang III, Nr. 3"
    },
    "employment": {
        "name": "Beschäftigung und Personalmanagement",
        "use_cases": [
            "Rekrutierung und Lebenslauf-Screening",
            "Zielgerichtete Stellenanzeigen",
            "Bewerbungsgespräch-Auswertung",
            "Leistungsüberwachung",
            "Beförderungs-/Kündigungsentscheidungen",
            "Aufgabenzuweisung"
        ],
        "article": "Anhang III, Nr. 4"
    },
    "essential_services": {
        "name": "Zugang zu wesentlichen Diensten",
        "use_cases": [
            "Kreditwürdigkeitsprüfung",
            "Risikobewertung für Lebens-/Krankenversicherung",
            "Sozialleistungs-Berechtigung",
            "Notruf-Bewertung und Dispatching",
            "Medizinische Triage"
        ],
        "article": "Anhang III, Nr. 5"
    },
    "law_enforcement": {
        "name": "Strafverfolgung",
        "use_cases": [
            "Risikobewertung für (Rück-)Fälligkeit",
            "Polygraph und ähnliche Tools",
            "Beweis-Zuverlässigkeitsbewertung",
            "Profiling bei Ermittlungen",
            "Kriminalitätsanalyse"
        ],
        "article": "Anhang III, Nr. 6"
    },
    "migration_border": {
        "name": "Migration und Grenzkontrolle",
        "use_cases": [
            "Sicherheits-/Gesundheits-/Migrationsrisikobewertung",
            "Asyl-/Visa-/Aufenthaltsgenehmigungsprüfung",
            "Dokumenten-Echtheitsprüfung",
            "Personenerkennung und -identifikation"
        ],
        "article": "Anhang III, Nr. 7"
    },
    "justice_democracy": {
        "name": "Justiz und demokratische Prozesse",
        "use_cases": [
            "Rechtsrecherche und -interpretation",
            "Alternative Streitbeilegung",
            "Beweisbewertung",
            "Beeinflussung von Gerichtsentscheidungen"
        ],
        "article": "Anhang III, Nr. 8"
    }
}

# Anhang I - Regulierte Produkte (Pathway A)
ANNEX_I_PRODUCTS = [
    "Medizinprodukte (Klasse IIa und höher)",
    "In-vitro-Diagnostika",
    "Maschinen und Anlagen",
    "Spielzeug",
    "Aufzüge und Sicherheitskomponenten",
    "Persönliche Schutzausrüstung",
    "Funkanlagen",
    "Druckgeräte",
    "Zivilluftfahrtsysteme",
    "Kraftfahrzeuge und Anhänger",
    "Land- und Forstwirtschaftsfahrzeuge",
    "Schiffsausrüstung",
    "Eisenbahnsysteme"
]

# Transparenzpflichten für begrenzte Risiken
LIMITED_RISK_TRIGGERS = {
    "chatbot": "KI-System interagiert direkt mit Nutzern (Chatbot, virtueller Assistent)",
    "deepfake": "Generiert oder manipuliert Bild-, Audio- oder Videoinhalte (Deepfakes)",
    "ai_generated_content": "Generiert synthetischen Text, der öffentlich verbreitet wird",
    "emotion_recognition_allowed": "Emotionserkennung für medizinische oder Sicherheitszwecke",
    "biometric_categorization_allowed": "Rechtmäßige biometrische Kategorisierung"
}


def classify_ai_system(
    # Grundlegende Informationen
    system_name: str,
    system_description: str,
    provider: str,

    # Verbotene Praktiken Checks
    uses_subliminal_manipulation: bool = False,
    exploits_vulnerable_groups: bool = False,
    performs_social_scoring: bool = False,
    predictive_policing_only_profiling: bool = False,
    scrapes_facial_recognition: bool = False,
    emotion_recognition_work_education: bool = False,
    biometric_categorization_sensitive: bool = False,
    realtime_biometric_public: bool = False,

    # Hochrisiko Pathway A
    is_safety_component_annex_i: bool = False,
    is_product_annex_i: bool = False,
    requires_third_party_assessment: bool = False,
    annex_i_product_type: Optional[str] = None,

    # Hochrisiko Pathway B
    high_risk_domain: Optional[str] = None,
    high_risk_use_case: Optional[str] = None,
    performs_profiling: bool = False,

    # Ausnahmen für Hochrisiko
    narrow_procedural_task: bool = False,
    improves_human_work: bool = False,
    detects_patterns_only: bool = False,
    preparatory_task_only: bool = False,

    # Begrenzte Risiken Checks
    interacts_with_humans: bool = False,
    generates_synthetic_content: bool = False,
    generates_deepfakes: bool = False,
    emotion_recognition_medical_safety: bool = False,
    biometric_categorization_lawful: bool = False
) -> ClassificationResult:
    """
    Klassifiziert ein KI-System nach EU AI Act Risikoklassen.
    """

    reasons = []
    obligations = []
    recommendations = []
    applicable_articles = []

    # SCHRITT 1: Prüfung auf verbotene Praktiken (Unannehmbares Risiko)
    prohibited_checks = [
        (uses_subliminal_manipulation, "subliminal_manipulation"),
        (exploits_vulnerable_groups, "exploitation_vulnerable"),
        (performs_social_scoring, "social_scoring"),
        (predictive_policing_only_profiling, "predictive_policing_profiling"),
        (scrapes_facial_recognition, "facial_recognition_scraping"),
        (emotion_recognition_work_education, "emotion_recognition_work_education"),
        (biometric_categorization_sensitive, "biometric_categorization_sensitive"),
        (realtime_biometric_public, "realtime_biometric_public")
    ]

    for is_triggered, practice_key in prohibited_checks:
        if is_triggered:
            practice = PROHIBITED_PRACTICES[practice_key]
            reasons.append(f"Verbotene Praktik: {practice['name']} - {practice['description']}")
            applicable_articles.append(practice['article'])

    if reasons:
        obligations = [
            "Das KI-System darf NICHT in der EU betrieben werden",
            "Sofortige Einstellung aller Aktivitäten erforderlich",
            "Mögliche Strafe: Bis zu 35 Mio. EUR oder 7% des weltweiten Jahresumsatzes"
        ]
        recommendations = [
            "Rechtliche Beratung einholen",
            "System umgestalten um verbotene Praktiken zu eliminieren",
            "Alternative Ansätze prüfen die EU AI Act-konform sind"
        ]
        return ClassificationResult(
            risk_level=RiskLevel.UNACCEPTABLE,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles
        )

    # SCHRITT 2: Prüfung auf Hochrisiko - Pathway A (Anhang I Produkte)
    if (is_safety_component_annex_i or is_product_annex_i) and requires_third_party_assessment:
        reasons.append(f"Hochrisiko Pathway A: KI-System ist {'Sicherheitskomponente von' if is_safety_component_annex_i else ''} "
                      f"{'reguliertem Produkt' if is_product_annex_i else ''} nach Anhang I")
        if annex_i_product_type:
            reasons.append(f"Produktkategorie: {annex_i_product_type}")
        applicable_articles.extend(["Artikel 6(1)", "Anhang I"])

        obligations = _get_high_risk_obligations()
        recommendations = _get_high_risk_recommendations()

        return ClassificationResult(
            risk_level=RiskLevel.HIGH,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles
        )

    # SCHRITT 3: Prüfung auf Hochrisiko - Pathway B (Anhang III Anwendungsbereiche)
    if high_risk_domain and high_risk_domain in HIGH_RISK_DOMAINS:
        domain = HIGH_RISK_DOMAINS[high_risk_domain]

        # Prüfung der Ausnahmen (gelten NICHT wenn Profiling durchgeführt wird)
        exceptions_apply = False
        if not performs_profiling:
            if narrow_procedural_task:
                exceptions_apply = True
                reasons.append("Ausnahme angewendet: Enge verfahrenstechnische Aufgabe")
            elif improves_human_work:
                exceptions_apply = True
                reasons.append("Ausnahme angewendet: Verbessert bereits abgeschlossene menschliche Arbeit")
            elif detects_patterns_only:
                exceptions_apply = True
                reasons.append("Ausnahme angewendet: Erkennt nur Muster ohne menschliche Bewertung zu ersetzen")
            elif preparatory_task_only:
                exceptions_apply = True
                reasons.append("Ausnahme angewendet: Nur vorbereitende Aufgabe")

        if not exceptions_apply:
            reasons.append(f"Hochrisiko Pathway B: Anwendungsbereich '{domain['name']}'")
            if high_risk_use_case:
                reasons.append(f"Anwendungsfall: {high_risk_use_case}")
            if performs_profiling:
                reasons.append("Profiling natürlicher Personen - Ausnahmen nicht anwendbar")
            applicable_articles.append(domain['article'])
            applicable_articles.append("Artikel 6(2)")

            obligations = _get_high_risk_obligations()
            recommendations = _get_high_risk_recommendations()

            return ClassificationResult(
                risk_level=RiskLevel.HIGH,
                reasons=reasons,
                obligations=obligations,
                recommendations=recommendations,
                applicable_articles=applicable_articles
            )

    # SCHRITT 4: Prüfung auf begrenztes Risiko (Transparenzpflichten)
    limited_risk_triggers = []

    if interacts_with_humans:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["chatbot"])
        applicable_articles.append("Artikel 50(1)")

    if generates_deepfakes:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["deepfake"])
        applicable_articles.append("Artikel 50(4)")

    if generates_synthetic_content:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["ai_generated_content"])
        applicable_articles.append("Artikel 50(4)")

    if emotion_recognition_medical_safety:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["emotion_recognition_allowed"])
        applicable_articles.append("Artikel 50(3)")

    if biometric_categorization_lawful:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["biometric_categorization_allowed"])
        applicable_articles.append("Artikel 50(3)")

    if limited_risk_triggers:
        reasons = [f"Transparenzpflicht ausgelöst: {trigger}" for trigger in limited_risk_triggers]

        obligations = [
            "Nutzer über KI-Interaktion informieren",
            "KI-generierte Inhalte als solche kennzeichnen",
            "Maschinenlesbare Markierung für synthetische Inhalte",
            "Bei Deepfakes: Offenlegungspflicht"
        ]

        recommendations = [
            "Klare Offenlegungsmechanismen implementieren",
            "Wasserzeichen für generierte Inhalte nutzen",
            "Nutzungsbedingungen aktualisieren",
            "Schulung für Mitarbeiter durchführen"
        ]

        return ClassificationResult(
            risk_level=RiskLevel.LIMITED,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles
        )

    # SCHRITT 5: Minimales Risiko (Fallback)
    reasons = ["Keine Hochrisiko-Kriterien oder Transparenzpflichten anwendbar"]
    obligations = ["Keine verpflichtenden Anforderungen nach EU AI Act"]
    recommendations = [
        "Freiwillige Verhaltenskodizes berücksichtigen",
        "Best Practices für verantwortungsvolle KI befolgen",
        "Regelmäßige Überprüfung bei Änderungen am System"
    ]

    return ClassificationResult(
        risk_level=RiskLevel.MINIMAL,
        reasons=reasons,
        obligations=obligations,
        recommendations=recommendations,
        applicable_articles=["Keine spezifischen Artikel anwendbar"]
    )


def _get_high_risk_obligations() -> list[str]:
    """Gibt die Pflichten für Hochrisiko-KI-Systeme zurück."""
    return [
        "Risikomanagementsystem einrichten (Artikel 9)",
        "Daten-Governance sicherstellen (Artikel 10)",
        "Technische Dokumentation erstellen (Artikel 11, Anhang IV)",
        "Automatische Protokollierung implementieren (Artikel 12)",
        "Transparenz gegenüber Betreibern gewährleisten (Artikel 13)",
        "Menschliche Aufsicht ermöglichen (Artikel 14)",
        "Genauigkeit, Robustheit und Cybersicherheit sicherstellen (Artikel 15)",
        "Konformitätsbewertung durchführen (Artikel 43)",
        "CE-Kennzeichnung anbringen (Artikel 48)",
        "Registrierung in EU-Datenbank (Artikel 49)",
        "Post-Market-Monitoring einrichten (Artikel 72)"
    ]


def _get_high_risk_recommendations() -> list[str]:
    """Gibt Empfehlungen für Hochrisiko-KI-Systeme zurück."""
    return [
        "Frühzeitig mit Konformitätsbewertung beginnen",
        "Qualitätsmanagementsystem implementieren",
        "Verantwortlichen für KI-Compliance benennen",
        "Dokumentation kontinuierlich aktualisieren",
        "Schulungen für alle Beteiligten durchführen",
        "Externe Prüfer/Notified Body konsultieren",
        "Notfallpläne für Systemausfälle erstellen"
    ]


def get_risk_color(risk_level: RiskLevel) -> str:
    """Gibt die Farbe für eine Risikostufe zurück."""
    colors = {
        RiskLevel.UNACCEPTABLE: "#FF0000",  # Rot
        RiskLevel.HIGH: "#FFA500",           # Orange
        RiskLevel.LIMITED: "#FFD700",        # Gelb
        RiskLevel.MINIMAL: "#00FF00"         # Grün
    }
    return colors.get(risk_level, "#808080")
