"""
EU AI Act Klassifizierungslogik
Enthält alle Kriterien und Logik zur Einstufung von KI-Systemen
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from datetime import datetime, date


class RiskLevel(Enum):
    UNACCEPTABLE = "Unannehmbares Risiko (Verboten)"
    HIGH = "Hohes Risiko"
    LIMITED = "Begrenztes Risiko"
    MINIMAL = "Minimales Risiko"


# Wichtige Fristen des EU AI Act
AI_ACT_DEADLINES = {
    "in_force": date(2024, 8, 1),           # AI Act tritt in Kraft
    "prohibited_practices": date(2025, 2, 2),  # Verbotene Praktiken + KI-Kompetenz
    "gpai_governance": date(2025, 8, 2),     # GPAI-Pflichten + Governance
    "high_risk_annex_iii": date(2026, 8, 2), # Hochrisiko Anhang III + Transparenz
    "high_risk_annex_i": date(2027, 8, 2),   # Hochrisiko Anhang I
}


@dataclass
class ClassificationResult:
    risk_level: RiskLevel
    reasons: list[str]
    obligations: list[str]
    recommendations: list[str]
    applicable_articles: list[str]
    timestamp: datetime = field(default_factory=datetime.now)
    # Neue Felder für erweiterte Klassifizierung
    is_gpai: bool = False
    gpai_has_systemic_risk: bool = False
    gpai_obligations: list[str] = field(default_factory=list)
    transparency_obligations: list[str] = field(default_factory=list)  # Zusätzliche Transparenzpflichten bei HIGH Risk
    universal_obligations: list[str] = field(default_factory=list)  # Gelten für alle (z.B. KI-Kompetenz, DSGVO)
    applicable_deadlines: dict[str, date] = field(default_factory=dict)
    exception_documentation_required: bool = False  # Dokumentationspflicht bei Ausnahme
    warnings: list[str] = field(default_factory=list)  # Warnungen bei Konflikten


# GPAI (General Purpose AI) Pflichten
GPAI_OBLIGATIONS = {
    "basic": [
        "Technische Dokumentation erstellen und aktualisieren (Art. 53(1)(a))",
        "Informationen und Dokumentation für nachgelagerte Anbieter bereitstellen (Art. 53(1)(b))",
        "EU-Urheberrechtsrichtlinie einhalten (Art. 53(1)(c))",
        "Ausreichend detaillierte Zusammenfassung der Trainingsdaten veröffentlichen (Art. 53(1)(d))",
    ],
    "systemic_risk": [
        "Modell-Evaluierungen nach Stand der Technik durchführen (Art. 55(1)(a))",
        "Systemische Risiken bewerten und mindern (Art. 55(1)(b))",
        "Schwerwiegende Vorfälle verfolgen, dokumentieren und melden (Art. 55(1)(c))",
        "Angemessene Cybersicherheit gewährleisten (Art. 55(1)(d))",
        "Energieeffizienz dokumentieren (Art. 55(1)(a))",
    ]
}

# Echtzeit-Biometrie Ausnahmen für Strafverfolgung (Art. 5(1)(h))
REALTIME_BIOMETRIC_EXCEPTIONS = {
    "missing_persons": {
        "name": "Suche nach vermissten Personen",
        "description": "Gezielte Suche nach bestimmten Opfern von Entführung, Menschenhandel oder sexueller Ausbeutung sowie Suche nach vermissten Personen",
        "article": "Artikel 5(2)(a)"
    },
    "terrorism_prevention": {
        "name": "Terrorismusabwehr",
        "description": "Abwendung einer konkreten, erheblichen und unmittelbaren Gefahr für das Leben oder die körperliche Unversehrtheit oder eines Terroranschlags",
        "article": "Artikel 5(2)(b)"
    },
    "serious_crime": {
        "name": "Schwere Straftaten",
        "description": "Aufspüren oder Identifizieren einer Person, die verdächtigt wird, eine schwere Straftat begangen zu haben (max. 3 Jahre Freiheitsstrafe)",
        "article": "Artikel 5(2)(c)"
    }
}

# Code of Practice - Spezifische Markierungsmethoden pro Medientyp
CODE_OF_PRACTICE_MARKING = {
    "video": [
        "Persistente visuelle Indikatoren während der gesamten Wiedergabe",
        "Eröffnungs-Disclaimer zu Beginn des Videos",
        "Bei Live-Video: Durchgehende Kennzeichnung erforderlich",
    ],
    "image": [
        "Sichtbare Labels oder Disclaimer auf dem Bild",
        "Wasserzeichen (sichtbar oder unsichtbar)",
        "Metadaten-Markierung (C2PA, IPTC, etc.)",
    ],
    "audio": [
        "Hörbarer Disclaimer am Anfang der Aufnahme",
        "Bei längeren Inhalten: Wiederholte Hinweise",
        "Metadaten-Markierung der Audiodatei",
    ],
    "text": [
        "Gemeinsames Symbol/Icon zur Kennzeichnung",
        "Sichtbar beim ersten Kontakt mit dem Inhalt",
        "Konsistente Platzierung (z.B. am Anfang oder Ende)",
    ]
}

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
    predictive_policing_with_objective_facts: bool = False,  # NEU: Erlaubte Variante
    scrapes_facial_recognition: bool = False,
    emotion_recognition_work_education: bool = False,
    biometric_categorization_sensitive: bool = False,
    realtime_biometric_public: bool = False,
    # NEU: Ausnahmen für Echtzeit-Biometrie
    realtime_biometric_exception: Optional[str] = None,  # missing_persons, terrorism_prevention, serious_crime

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
    biometric_categorization_lawful: bool = False,
    # NEU: Medientypen für spezifische Markierungsempfehlungen
    synthetic_content_types: Optional[list[str]] = None,  # video, image, audio, text

    # NEU: GPAI (General Purpose AI) Parameter
    is_gpai: bool = False,
    gpai_has_systemic_risk: bool = False,

    # NEU: Für Fristberechnung
    reference_date: Optional[date] = None  # Standardmäßig heute
) -> ClassificationResult:
    """
    Klassifiziert ein KI-System nach EU AI Act Risikoklassen.

    Implementiert den vollständigen Entscheidungsbaum gemäß EU AI Act (VO 2024/1689):
    1. Prüfung verbotener Praktiken (Art. 5) → UNACCEPTABLE
    2. Prüfung Hochrisiko Pathway A (Anhang I) → HIGH
    3. Prüfung Hochrisiko Pathway B (Anhang III) mit Ausnahmen → HIGH
    4. Prüfung Transparenzpflichten (Art. 50) → LIMITED
    5. Fallback → MINIMAL

    Zusätzlich: GPAI-Pflichten, universelle Pflichten, Fristlogik
    """

    # Referenzdatum für Fristberechnung
    if reference_date is None:
        reference_date = date.today()

    reasons = []
    obligations = []
    recommendations = []
    applicable_articles = []
    warnings = []
    transparency_obligations = []
    universal_obligations = []
    gpai_obligations_list = []
    applicable_deadlines = {}
    exception_documentation_required = False

    # ============================================================
    # SCHRITT 0: Konfliktprüfung bei widersprüchlichen Eingaben
    # ============================================================

    # Konflikt: Emotionserkennung am Arbeitsplatz UND medizinisch/Sicherheit
    if emotion_recognition_work_education and emotion_recognition_medical_safety:
        warnings.append(
            "KONFLIKT: Emotionserkennung kann nicht gleichzeitig am Arbeitsplatz/in Bildung "
            "(verboten) UND für medizinische/Sicherheitszwecke (erlaubt) sein. "
            "Bitte klären Sie den primären Verwendungszweck."
        )

    # Konflikt: Biometrische Kategorisierung sensibel UND rechtmäßig
    if biometric_categorization_sensitive and biometric_categorization_lawful:
        warnings.append(
            "KONFLIKT: Biometrische Kategorisierung kann nicht gleichzeitig nach sensiblen "
            "Merkmalen (verboten) UND rechtmäßig (erlaubt) sein. "
            "Bitte prüfen Sie welche Kategorien tatsächlich erfasst werden."
        )

    # Konflikt: Predictive Policing nur Profiling UND mit objektiven Fakten
    if predictive_policing_only_profiling and predictive_policing_with_objective_facts:
        warnings.append(
            "KONFLIKT: Predictive Policing kann nicht gleichzeitig NUR auf Profiling "
            "basieren UND objektive Fakten nutzen. "
            "Bitte klären Sie die tatsächliche Datenbasis."
        )

    # ============================================================
    # UNIVERSELLE PFLICHTEN (gelten für alle Systeme)
    # ============================================================

    # KI-Kompetenz gilt ab 02.02.2025 für ALLE
    if reference_date >= AI_ACT_DEADLINES["prohibited_practices"]:
        universal_obligations.append(
            "KI-Kompetenz sicherstellen: Alle Mitarbeiter, die mit dem KI-System arbeiten, "
            "müssen über ausreichende KI-Kompetenz verfügen (Art. 4)"
        )
        applicable_deadlines["ki_kompetenz"] = AI_ACT_DEADLINES["prohibited_practices"]

    # DSGVO gilt immer
    universal_obligations.extend([
        "DSGVO-Konformität: Das KI-System unterliegt unabhängig vom AI Act der DSGVO",
        "Datenschutz-Folgenabschätzung prüfen, falls personenbezogene Daten verarbeitet werden",
    ])

    # ============================================================
    # SCHRITT 1: Prüfung auf verbotene Praktiken (Unannehmbares Risiko)
    # Prüfung ob verbotene Praktiken greifen gilt ab 02.02.2025
    prohibited_practices_active = reference_date >= AI_ACT_DEADLINES["prohibited_practices"]
    if prohibited_practices_active:
        applicable_deadlines["verbotene_praktiken"] = AI_ACT_DEADLINES["prohibited_practices"]

    prohibited_checks = [
        (uses_subliminal_manipulation, "subliminal_manipulation"),
        (exploits_vulnerable_groups, "exploitation_vulnerable"),
        (performs_social_scoring, "social_scoring"),
        # Predictive Policing NUR wenn ausschließlich Profiling (nicht mit objektiven Fakten)
        (predictive_policing_only_profiling and not predictive_policing_with_objective_facts, "predictive_policing_profiling"),
        (scrapes_facial_recognition, "facial_recognition_scraping"),
        # Emotionserkennung am Arbeitsplatz/Bildung NUR wenn nicht medizinisch/Sicherheit
        (emotion_recognition_work_education and not emotion_recognition_medical_safety, "emotion_recognition_work_education"),
        (biometric_categorization_sensitive, "biometric_categorization_sensitive"),
    ]

    # Echtzeit-Biometrie: Prüfung mit Ausnahmen
    realtime_biometric_prohibited = False
    if realtime_biometric_public:
        if realtime_biometric_exception and realtime_biometric_exception in REALTIME_BIOMETRIC_EXCEPTIONS:
            # Ausnahme greift - System ist HIGH RISK, nicht VERBOTEN
            exception = REALTIME_BIOMETRIC_EXCEPTIONS[realtime_biometric_exception]
            reasons.append(
                f"Echtzeit-Biometrie mit Ausnahme: {exception['name']} - {exception['description']}"
            )
            applicable_articles.append(exception['article'])
            # Wird später als HIGH RISK klassifiziert
        else:
            realtime_biometric_prohibited = True

    for is_triggered, practice_key in prohibited_checks:
        if is_triggered and prohibited_practices_active:
            practice = PROHIBITED_PRACTICES[practice_key]
            reasons.append(f"Verbotene Praktik: {practice['name']} - {practice['description']}")
            applicable_articles.append(practice['article'])

    # Echtzeit-Biometrie ohne Ausnahme hinzufügen
    if realtime_biometric_prohibited and prohibited_practices_active:
        practice = PROHIBITED_PRACTICES["realtime_biometric_public"]
        reasons.append(f"Verbotene Praktik: {practice['name']} - {practice['description']}")
        applicable_articles.append(practice['article'])

    # Prüfung ob verbotene Praktiken vorliegen (Konflikte wurden oben gewarnt)
    prohibited_reasons = [r for r in reasons if r.startswith("Verbotene Praktik:")]
    if prohibited_reasons:
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
            applicable_articles=applicable_articles,
            is_gpai=is_gpai,
            gpai_has_systemic_risk=gpai_has_systemic_risk,
            universal_obligations=universal_obligations,
            applicable_deadlines=applicable_deadlines,
            warnings=warnings
        )

    # ============================================================
    # SCHRITT 2: Prüfung auf Hochrisiko - Pathway A (Anhang I Produkte)
    # ============================================================
    # Gilt ab 02.08.2027
    pathway_a_active = reference_date >= AI_ACT_DEADLINES["high_risk_annex_i"]

    if (is_safety_component_annex_i or is_product_annex_i) and requires_third_party_assessment:
        applicable_deadlines["hochrisiko_anhang_i"] = AI_ACT_DEADLINES["high_risk_annex_i"]

        component_text = "Sicherheitskomponente von " if is_safety_component_annex_i else ""
        product_text = "reguliertem Produkt" if is_product_annex_i else ""
        reasons.append(f"Hochrisiko Pathway A: KI-System ist {component_text}{product_text} nach Anhang I")
        if annex_i_product_type:
            reasons.append(f"Produktkategorie: {annex_i_product_type}")
        applicable_articles.extend(["Artikel 6(1)", "Anhang I"])

        # Kumulative Transparenzpflichten sammeln (auch HIGH RISK kann Transparenzpflichten haben)
        transparency_obligations = _collect_transparency_obligations(
            interacts_with_humans, generates_deepfakes, generates_synthetic_content,
            emotion_recognition_medical_safety, biometric_categorization_lawful,
            synthetic_content_types
        )

        obligations = _get_high_risk_obligations()
        recommendations = _get_high_risk_recommendations()

        # GPAI-Pflichten hinzufügen falls zutreffend
        if is_gpai:
            gpai_obligations_list = _get_gpai_obligations(gpai_has_systemic_risk)
            applicable_deadlines["gpai"] = AI_ACT_DEADLINES["gpai_governance"]

        return ClassificationResult(
            risk_level=RiskLevel.HIGH,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles,
            is_gpai=is_gpai,
            gpai_has_systemic_risk=gpai_has_systemic_risk,
            gpai_obligations=gpai_obligations_list,
            transparency_obligations=transparency_obligations,
            universal_obligations=universal_obligations,
            applicable_deadlines=applicable_deadlines,
            warnings=warnings
        )

    # ============================================================
    # SCHRITT 3: Prüfung auf Hochrisiko - Pathway B (Anhang III Anwendungsbereiche)
    # ============================================================
    # Gilt ab 02.08.2026
    pathway_b_active = reference_date >= AI_ACT_DEADLINES["high_risk_annex_iii"]

    # Sonderfall: Echtzeit-Biometrie mit Ausnahme ist HIGH RISK (nicht verboten)
    realtime_biometric_high_risk = (
        realtime_biometric_public and
        realtime_biometric_exception and
        realtime_biometric_exception in REALTIME_BIOMETRIC_EXCEPTIONS
    )

    # Sonderfall: Predictive Policing MIT objektiven Fakten ist HIGH RISK (nicht verboten)
    predictive_policing_high_risk = (
        predictive_policing_with_objective_facts and
        not predictive_policing_only_profiling
    )

    # Prüfung auf Anhang III Hochrisiko-Bereich
    is_high_risk_pathway_b = False

    if high_risk_domain and high_risk_domain in HIGH_RISK_DOMAINS:
        domain = HIGH_RISK_DOMAINS[high_risk_domain]
        applicable_deadlines["hochrisiko_anhang_iii"] = AI_ACT_DEADLINES["high_risk_annex_iii"]

        # Prüfung der Ausnahmen (gelten NICHT wenn Profiling durchgeführt wird)
        # WICHTIG: Alle zutreffenden Ausnahmen werden dokumentiert (nicht elif!)
        exceptions_applied = []

        if not performs_profiling:
            if narrow_procedural_task:
                exceptions_applied.append("Enge verfahrenstechnische Aufgabe (Art. 6(3)(a))")
            if improves_human_work:
                exceptions_applied.append("Verbessert bereits abgeschlossene menschliche Arbeit (Art. 6(3)(b))")
            if detects_patterns_only:
                exceptions_applied.append("Erkennt nur Muster ohne menschliche Bewertung zu ersetzen (Art. 6(3)(c))")
            if preparatory_task_only:
                exceptions_applied.append("Nur vorbereitende Aufgabe (Art. 6(3)(d))")

        exceptions_apply = len(exceptions_applied) > 0

        if exceptions_apply:
            # Dokumentationspflicht bei Ausnahme-Inanspruchnahme
            exception_documentation_required = True
            for exc in exceptions_applied:
                reasons.append(f"Ausnahme angewendet: {exc}")
            applicable_articles.append("Artikel 6(3)")
        else:
            is_high_risk_pathway_b = True
            reasons.append(f"Hochrisiko Pathway B: Anwendungsbereich '{domain['name']}'")
            if high_risk_use_case:
                reasons.append(f"Anwendungsfall: {high_risk_use_case}")
            if performs_profiling:
                reasons.append("Profiling natürlicher Personen - Ausnahmen nach Art. 6(3) nicht anwendbar")
            applicable_articles.append(domain['article'])
            applicable_articles.append("Artikel 6(2)")

    # Echtzeit-Biometrie mit Ausnahme als HIGH RISK hinzufügen
    if realtime_biometric_high_risk:
        is_high_risk_pathway_b = True
        reasons.append("Hochrisiko: Echtzeit-Biometrie für Strafverfolgung mit genehmigter Ausnahme")
        applicable_articles.append("Artikel 5(2)")
        applicable_articles.append("Anhang III, Nr. 1")

    # Predictive Policing mit objektiven Fakten als HIGH RISK
    if predictive_policing_high_risk:
        is_high_risk_pathway_b = True
        reasons.append("Hochrisiko: Predictive Policing mit Berücksichtigung objektiver, nachprüfbarer Fakten")
        applicable_articles.append("Anhang III, Nr. 6")

    if is_high_risk_pathway_b:
        # Kumulative Transparenzpflichten sammeln
        transparency_obligations = _collect_transparency_obligations(
            interacts_with_humans, generates_deepfakes, generates_synthetic_content,
            emotion_recognition_medical_safety, biometric_categorization_lawful,
            synthetic_content_types
        )

        obligations = _get_high_risk_obligations()
        recommendations = _get_high_risk_recommendations()

        # GPAI-Pflichten hinzufügen falls zutreffend
        if is_gpai:
            gpai_obligations_list = _get_gpai_obligations(gpai_has_systemic_risk)
            applicable_deadlines["gpai"] = AI_ACT_DEADLINES["gpai_governance"]

        return ClassificationResult(
            risk_level=RiskLevel.HIGH,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles,
            is_gpai=is_gpai,
            gpai_has_systemic_risk=gpai_has_systemic_risk,
            gpai_obligations=gpai_obligations_list,
            transparency_obligations=transparency_obligations,
            universal_obligations=universal_obligations,
            applicable_deadlines=applicable_deadlines,
            exception_documentation_required=False,
            warnings=warnings
        )

    # ============================================================
    # SCHRITT 4: Prüfung auf begrenztes Risiko (Transparenzpflichten)
    # ============================================================
    # Gilt ab 02.08.2026
    transparency_active = reference_date >= AI_ACT_DEADLINES["high_risk_annex_iii"]

    limited_risk_triggers = []
    limited_risk_articles = []

    if interacts_with_humans:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["chatbot"])
        limited_risk_articles.append("Artikel 50(1)")

    if generates_deepfakes:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["deepfake"])
        limited_risk_articles.append("Artikel 50(4)")

    if generates_synthetic_content:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["ai_generated_content"])
        limited_risk_articles.append("Artikel 50(2)")

    if emotion_recognition_medical_safety:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["emotion_recognition_allowed"])
        limited_risk_articles.append("Artikel 50(3)")

    if biometric_categorization_lawful:
        limited_risk_triggers.append(LIMITED_RISK_TRIGGERS["biometric_categorization_allowed"])
        limited_risk_articles.append("Artikel 50(3)")

    if limited_risk_triggers:
        applicable_deadlines["transparenzpflichten"] = AI_ACT_DEADLINES["high_risk_annex_iii"]

        # Reasons aus Ausnahmen beibehalten, falls vorhanden
        exception_reasons = [r for r in reasons if r.startswith("Ausnahme angewendet:")]
        reasons = exception_reasons + [f"Transparenzpflicht ausgelöst: {trigger}" for trigger in limited_risk_triggers]
        applicable_articles.extend(limited_risk_articles)

        obligations = [
            "Nutzer über KI-Interaktion informieren (Art. 50(1))",
            "KI-generierte Inhalte als solche kennzeichnen (Art. 50(2))",
            "Maschinenlesbare Markierung für synthetische Inhalte implementieren",
            "Bei Deepfakes: Offenlegungspflicht erfüllen (Art. 50(4))",
        ]

        # Code of Practice spezifische Empfehlungen
        recommendations = [
            "Klare Offenlegungsmechanismen implementieren",
            "Nutzungsbedingungen aktualisieren",
            "Schulung für Mitarbeiter durchführen",
        ]

        # Spezifische Markierungsempfehlungen pro Medientyp
        if synthetic_content_types:
            for content_type in synthetic_content_types:
                if content_type in CODE_OF_PRACTICE_MARKING:
                    recommendations.append(f"--- Empfehlungen für {content_type.upper()}: ---")
                    recommendations.extend(CODE_OF_PRACTICE_MARKING[content_type])

        # GPAI-Pflichten hinzufügen falls zutreffend
        if is_gpai:
            gpai_obligations_list = _get_gpai_obligations(gpai_has_systemic_risk)
            applicable_deadlines["gpai"] = AI_ACT_DEADLINES["gpai_governance"]

        return ClassificationResult(
            risk_level=RiskLevel.LIMITED,
            reasons=reasons,
            obligations=obligations,
            recommendations=recommendations,
            applicable_articles=applicable_articles,
            is_gpai=is_gpai,
            gpai_has_systemic_risk=gpai_has_systemic_risk,
            gpai_obligations=gpai_obligations_list,
            universal_obligations=universal_obligations,
            applicable_deadlines=applicable_deadlines,
            exception_documentation_required=exception_documentation_required,
            warnings=warnings
        )

    # ============================================================
    # SCHRITT 5: Minimales Risiko (Fallback)
    # ============================================================

    # Reasons aus Ausnahmen beibehalten, falls vorhanden
    exception_reasons = [r for r in reasons if r.startswith("Ausnahme angewendet:")]
    if exception_reasons:
        reasons = exception_reasons + ["Nach Anwendung der Ausnahme: Minimales Risiko"]
    else:
        reasons = ["Keine Hochrisiko-Kriterien oder Transparenzpflichten anwendbar"]

    obligations = ["Keine verpflichtenden Anforderungen nach EU AI Act (außer universellen Pflichten)"]

    recommendations = [
        "Freiwillige Verhaltenskodizes berücksichtigen (Art. 95)",
        "Best Practices für verantwortungsvolle KI befolgen",
        "Regelmäßige Überprüfung bei Änderungen am System",
        "Risikomanagementsystem freiwillig einrichten",
        "Transparenz gegenüber Nutzern gewährleisten",
    ]

    # GPAI-Pflichten hinzufügen falls zutreffend (GPAI hat eigene Pflichten auch bei Minimal Risk!)
    if is_gpai:
        gpai_obligations_list = _get_gpai_obligations(gpai_has_systemic_risk)
        applicable_deadlines["gpai"] = AI_ACT_DEADLINES["gpai_governance"]
        reasons.append("GPAI-Modell: Trotz Minimal Risk gelten spezifische GPAI-Pflichten")

    return ClassificationResult(
        risk_level=RiskLevel.MINIMAL,
        reasons=reasons,
        obligations=obligations,
        recommendations=recommendations,
        applicable_articles=["Artikel 95 (Freiwillige Verhaltenskodizes)"],
        is_gpai=is_gpai,
        gpai_has_systemic_risk=gpai_has_systemic_risk,
        gpai_obligations=gpai_obligations_list,
        universal_obligations=universal_obligations,
        applicable_deadlines=applicable_deadlines,
        exception_documentation_required=exception_documentation_required,
        warnings=warnings
    )


def _get_gpai_obligations(has_systemic_risk: bool = False) -> list[str]:
    """Gibt die Pflichten für GPAI-Modelle zurück."""
    obligations = GPAI_OBLIGATIONS["basic"].copy()
    if has_systemic_risk:
        obligations.extend(GPAI_OBLIGATIONS["systemic_risk"])
    return obligations


def _collect_transparency_obligations(
    interacts_with_humans: bool,
    generates_deepfakes: bool,
    generates_synthetic_content: bool,
    emotion_recognition_medical_safety: bool,
    biometric_categorization_lawful: bool,
    synthetic_content_types: Optional[list[str]] = None
) -> list[str]:
    """Sammelt alle zutreffenden Transparenzpflichten (auch für HIGH Risk Systeme)."""
    obligations = []

    if interacts_with_humans:
        obligations.append("Nutzer müssen darüber informiert werden, dass sie mit einer KI interagieren (Art. 50(1))")

    if generates_deepfakes:
        obligations.append("Deepfakes müssen als künstlich erstellt/manipuliert gekennzeichnet werden (Art. 50(4))")

    if generates_synthetic_content:
        obligations.append("Synthetische Inhalte müssen maschinenlesbar als KI-generiert markiert werden (Art. 50(2))")

        # Spezifische Markierungsempfehlungen pro Medientyp
        if synthetic_content_types:
            for content_type in synthetic_content_types:
                if content_type in CODE_OF_PRACTICE_MARKING:
                    for method in CODE_OF_PRACTICE_MARKING[content_type]:
                        obligations.append(f"  [{content_type.upper()}] {method}")

    if emotion_recognition_medical_safety:
        obligations.append("Betroffene Personen müssen über Emotionserkennung informiert werden (Art. 50(3))")

    if biometric_categorization_lawful:
        obligations.append("Betroffene Personen müssen über biometrische Kategorisierung informiert werden (Art. 50(3))")

    return obligations


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
