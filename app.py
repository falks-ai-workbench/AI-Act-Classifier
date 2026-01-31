"""
EU AI Act Klassifizierungs-Tool
Streamlit-basierte Webanwendung zur automatischen Einstufung von KI-Systemen
"""

import streamlit as st
from datetime import datetime, date

from classifier_logic import (
    classify_ai_system,
    RiskLevel,
    HIGH_RISK_DOMAINS,
    PROHIBITED_PRACTICES,
    ANNEX_I_PRODUCTS,
    REALTIME_BIOMETRIC_EXCEPTIONS,
    CODE_OF_PRACTICE_MARKING,
    AI_ACT_DEADLINES,
    get_risk_color
)
from export_utils import (
    generate_markdown_report,
    generate_technical_documentation_template,
    export_to_csv,
    export_to_excel,
    create_classification_summary
)


# Seitenkonfiguration
st.set_page_config(
    page_title="EU AI Act Klassifizierung",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .risk-unacceptable {
        background-color: #ffcccc;
        border-left: 5px solid #ff0000;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .risk-high {
        background-color: #ffe6cc;
        border-left: 5px solid #ff9900;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .risk-limited {
        background-color: #fff9cc;
        border-left: 5px solid #ffcc00;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .risk-minimal {
        background-color: #ccffcc;
        border-left: 5px solid #00cc00;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stExpander {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
    }
    .info-box {
        background-color: #e7f3fe;
        border-left: 5px solid #2196F3;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .gpai-box {
        background-color: #e8daef;
        border-left: 5px solid #8e44ad;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .universal-box {
        background-color: #d5f4e6;
        border-left: 5px solid #27ae60;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .deadline-box {
        background-color: #fdebd0;
        border-left: 5px solid #e67e22;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Session State initialisieren
if 'classifications' not in st.session_state:
    st.session_state.classifications = []

if 'current_result' not in st.session_state:
    st.session_state.current_result = None


def main():
    # Header
    st.title("🤖 EU AI Act Klassifizierungs-Tool")
    st.markdown("""
    Dieses Tool hilft Ihnen, Ihr KI-System nach den Risikoklassen des **EU AI Act (Verordnung (EU) 2024/1689)** einzustufen.
    Beantworten Sie die folgenden Fragen, um eine automatische Klassifizierung und Dokumentation zu erhalten.
    """)

    # Sidebar mit Informationen
    with st.sidebar:
        st.header("📋 Information")
        st.markdown("""
        **Risikostufen des EU AI Act:**

        🚫 **Unannehmbares Risiko**
        - Verbotene KI-Systeme
        - Strafe: bis 35 Mio. EUR / 7%

        ⚠️ **Hohes Risiko**
        - Strenge Compliance-Pflichten
        - Strafe: bis 15 Mio. EUR / 3%

        ℹ️ **Begrenztes Risiko**
        - Transparenzpflichten
        - Strafe: bis 7,5 Mio. EUR / 1,5%

        ✅ **Minimales Risiko**
        - Keine verpflichtenden Anforderungen
        """)

        st.divider()

        st.header("📅 Wichtige Fristen")
        st.markdown("""
        - **02.02.2025**: Verbote gelten
        - **02.08.2025**: Governance-Regeln
        - **02.08.2026**: Volle Anwendung
        - **02.08.2027**: Anhang I Produkte
        """)

        st.divider()

        # Bisherige Klassifizierungen
        if st.session_state.classifications:
            st.header("📊 Bisherige Klassifizierungen")
            for i, c in enumerate(st.session_state.classifications[-5:]):  # Letzte 5
                st.markdown(f"**{c['Systemname']}**")
                st.caption(c['Risikostufe'])

    # Hauptbereich mit Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 Neue Klassifizierung",
        "📊 Ergebnis & Export",
        "📚 Referenz",
        "💾 Alle Klassifizierungen"
    ])

    with tab1:
        create_classification_form()

    with tab2:
        show_results()

    with tab3:
        show_reference()

    with tab4:
        show_all_classifications()


def create_classification_form():
    """Erstellt das Klassifizierungsformular."""

    st.header("Neue KI-System-Klassifizierung")

    # Grundlegende Informationen
    st.subheader("1️⃣ Grundlegende Informationen")

    col1, col2 = st.columns(2)
    with col1:
        system_name = st.text_input(
            "Name des KI-Systems *",
            placeholder="z.B. ChatBot Pro 2.0",
            help="Geben Sie einen eindeutigen Namen für Ihr KI-System ein"
        )
    with col2:
        provider = st.text_input(
            "Anbieter/Unternehmen *",
            placeholder="z.B. Muster GmbH",
            help="Name des Unternehmens, das das KI-System bereitstellt"
        )

    system_description = st.text_area(
        "Beschreibung des KI-Systems *",
        placeholder="Beschreiben Sie kurz den Zweck und die Funktionsweise des Systems...",
        help="Eine kurze Beschreibung der Hauptfunktionen und des Einsatzzwecks",
        height=100
    )

    st.divider()

    # Verbotene Praktiken
    st.subheader("2️⃣ Prüfung auf verbotene Praktiken (Artikel 5)")
    st.markdown("""
    <div class="info-box">
    <strong>Wichtig:</strong> Wenn Ihr System eine der folgenden Praktiken verwendet, ist es nach dem EU AI Act verboten.
    Bitte prüfen Sie sorgfältig alle Punkte.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        uses_subliminal = st.checkbox(
            "Unterschwellige Manipulation",
            help="Das System setzt unterschwellige Techniken ein, die das Bewusstsein umgehen, um Verhalten zu beeinflussen"
        )

        exploits_vulnerable = st.checkbox(
            "Ausnutzung Schutzbedürftiger",
            help="Das System nutzt Schwächen aufgrund von Alter, Behinderung oder sozioökonomischer Lage aus"
        )

        social_scoring = st.checkbox(
            "Soziales Scoring",
            help="Bewertung von Personen basierend auf sozialem Verhalten, die zu nachteiliger Behandlung führt"
        )

        predictive_policing = st.checkbox(
            "Predictive Policing (nur Profiling)",
            help="Vorhersage von Straftaten ausschließlich basierend auf Profiling ohne objektive Fakten"
        )

        # NEU: Predictive Policing mit objektiven Fakten
        predictive_policing_facts = st.checkbox(
            "Predictive Policing (mit objektiven Fakten)",
            help="Vorhersage von Straftaten unter Berücksichtigung objektiver, nachprüfbarer Fakten (HIGH RISK, nicht verboten)"
        )

    with col2:
        facial_scraping = st.checkbox(
            "Gesichtserkennung-Scraping",
            help="Erstellen von Gesichtsdatenbanken durch ungezieltes Scraping aus Internet oder CCTV"
        )

        emotion_work_edu = st.checkbox(
            "Emotionserkennung (Arbeit/Bildung)",
            help="Ableitung von Emotionen am Arbeitsplatz oder in Bildungseinrichtungen (außer medizinisch)"
        )

        biometric_sensitive = st.checkbox(
            "Biometrische Kategorisierung (sensibel)",
            help="Kategorisierung durch Ableitung von Rasse, Religion, sexueller Orientierung etc."
        )

        realtime_biometric = st.checkbox(
            "Echtzeit-Biometrie (öffentlich)",
            help="Echtzeit-Fernidentifizierung in öffentlich zugänglichen Räumen für Strafverfolgung"
        )

    # NEU: Ausnahmen für Echtzeit-Biometrie
    realtime_biometric_exception = None
    if realtime_biometric:
        st.markdown("##### Ausnahmen für Echtzeit-Biometrie (Art. 5(2))")
        st.markdown("*Unter sehr engen Bedingungen kann Echtzeit-Biometrie für Strafverfolgung erlaubt sein (HIGH RISK statt verboten):*")
        exception_options = ["Keine Ausnahme (verboten)"] + [
            f"{v['name']}: {v['description']}" for v in REALTIME_BIOMETRIC_EXCEPTIONS.values()
        ]
        selected_exception = st.selectbox(
            "Ausnahme auswählen",
            exception_options,
            help="Wählen Sie eine Ausnahme, falls zutreffend"
        )
        if selected_exception != "Keine Ausnahme (verboten)":
            for key, val in REALTIME_BIOMETRIC_EXCEPTIONS.items():
                if val['name'] in selected_exception:
                    realtime_biometric_exception = key
                    break

    st.divider()

    # Hochrisiko Pathway A
    st.subheader("3️⃣ Hochrisiko-Prüfung: Pathway A (Regulierte Produkte)")
    st.markdown("""
    <div class="info-box">
    Ist Ihr KI-System ein Sicherheitsbauteil oder selbst ein Produkt, das unter EU-Harmonisierungsvorschriften fällt?
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        is_safety_component = st.checkbox(
            "KI steuert sicherheitskritische Funktion eines Produkts",
            help="z.B. Bremsassistent, Medizingeräte-Steuerung, KI in Aufzügen oder Maschinen"
        )

    with col2:
        is_product = st.checkbox(
            "Das KI-System wird als eigenständiges Produkt verkauft",
            help="z.B. KI-Diagnosegerät, autonomer Roboter, KI-Medizinprodukt"
        )

    with col3:
        requires_assessment = st.checkbox(
            "Eine externe Prüfstelle (z.B. TÜV) muss das Produkt zertifizieren",
            help="Nicht nur Selbsterklärung des Herstellers, sondern unabhängige Sicherheitsprüfung erforderlich"
        )

    if is_safety_component or is_product:
        annex_i_product = st.selectbox(
            "Produktkategorie (Anhang I)",
            ["Bitte auswählen..."] + ANNEX_I_PRODUCTS,
            help="Wählen Sie die zutreffende Produktkategorie"
        )
    else:
        annex_i_product = None

    st.divider()

    # Hochrisiko Pathway B
    st.subheader("4️⃣ Hochrisiko-Prüfung: Pathway B (Anwendungsbereiche)")
    st.markdown("""
    <div class="info-box">
    Wird Ihr KI-System in einem der folgenden Hochrisiko-Bereiche nach Anhang III eingesetzt?
    </div>
    """, unsafe_allow_html=True)

    domain_names = {k: v["name"] for k, v in HIGH_RISK_DOMAINS.items()}
    selected_domain = st.selectbox(
        "Anwendungsbereich",
        ["Keiner dieser Bereiche"] + list(domain_names.values()),
        help="Wählen Sie den Bereich, in dem Ihr KI-System eingesetzt wird"
    )

    # Domain-Key aus dem Namen ableiten
    domain_key = None
    selected_use_case = None

    for key, domain in HIGH_RISK_DOMAINS.items():
        if domain["name"] == selected_domain:
            domain_key = key
            break

    if domain_key:
        use_cases = HIGH_RISK_DOMAINS[domain_key]["use_cases"]
        selected_use_case = st.selectbox(
            "Spezifischer Anwendungsfall",
            ["Bitte auswählen..."] + use_cases,
            help="Wählen Sie den spezifischen Anwendungsfall"
        )

        st.markdown("#### Ausnahmen prüfen")
        st.markdown("*Die folgenden Ausnahmen gelten NICHT, wenn das System Profiling natürlicher Personen durchführt.*")

        col1, col2 = st.columns(2)

        with col1:
            performs_profiling = st.checkbox(
                "System führt Profiling durch",
                help="Das System erstellt Profile natürlicher Personen"
            )

            narrow_procedural = st.checkbox(
                "Nur enge verfahrenstechnische Aufgabe",
                help="Das System führt nur eine enge verfahrenstechnische Aufgabe aus"
            )

        with col2:
            improves_human = st.checkbox(
                "Verbessert nur menschliche Arbeit",
                help="Das System verbessert nur das Ergebnis bereits abgeschlossener menschlicher Aktivität"
            )

            detects_patterns = st.checkbox(
                "Erkennt nur Muster",
                help="Das System erkennt nur Entscheidungsmuster ohne menschliche Bewertung zu ersetzen"
            )

        preparatory_only = st.checkbox(
            "Nur vorbereitende Aufgabe",
            help="Das System führt nur vorbereitende Aufgaben für eine Bewertung aus"
        )
    else:
        performs_profiling = False
        narrow_procedural = False
        improves_human = False
        detects_patterns = False
        preparatory_only = False

    st.divider()

    # Transparenzpflichten
    st.subheader("5️⃣ Transparenzpflichten (Begrenztes Risiko)")
    st.markdown("""
    <div class="info-box">
    Auch wenn Ihr System nicht als Hochrisiko eingestuft wird, können Transparenzpflichten gelten.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        interacts_humans = st.checkbox(
            "Direkte Interaktion mit Menschen",
            help="Chatbot, virtueller Assistent oder andere direkte Kommunikation"
        )

        generates_synthetic = st.checkbox(
            "Generiert synthetische Inhalte",
            help="Generiert Text, Bilder, Audio oder Video"
        )

        generates_deepfakes = st.checkbox(
            "Generiert Deepfakes",
            help="Generiert oder manipuliert realistische Medien von echten Personen"
        )

    with col2:
        emotion_medical = st.checkbox(
            "Emotionserkennung (medizinisch/Sicherheit)",
            help="Emotionserkennung für medizinische oder sicherheitsrelevante Zwecke"
        )

        biometric_lawful = st.checkbox(
            "Rechtmäßige biometrische Kategorisierung",
            help="Rechtmäßige Filterung biometrischer Datensätze"
        )

    # NEU: Medientypen für Code of Practice Empfehlungen
    synthetic_content_types = None
    if generates_synthetic:
        st.markdown("##### Welche Medientypen werden generiert?")
        content_type_options = st.multiselect(
            "Medientypen auswählen",
            ["video", "image", "audio", "text"],
            help="Wählen Sie alle Medientypen, die das System generiert (für spezifische Markierungsempfehlungen)"
        )
        if content_type_options:
            synthetic_content_types = content_type_options

    st.divider()

    # NEU: GPAI (General Purpose AI) Abschnitt
    st.subheader("6️⃣ General Purpose AI (GPAI) / Allzweck-KI")
    st.markdown("""
    <div class="info-box">
    Ist Ihr KI-System ein Allzweck-KI-Modell (GPAI), das für eine Vielzahl von Aufgaben verwendet werden kann?
    Beispiele: GPT-4, Claude, Gemini, Llama, Mistral
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        is_gpai = st.checkbox(
            "System ist ein GPAI-Modell",
            help="Das System ist ein Allzweck-KI-Modell, das für viele verschiedene Aufgaben genutzt werden kann"
        )

    with col2:
        gpai_systemic = st.checkbox(
            "GPAI mit systemischem Risiko",
            help="Das Modell hat hohe Auswirkungskapazitäten oder ist weit verbreitet (z.B. > 10^25 FLOPs für Training)",
            disabled=not is_gpai
        )

    st.divider()

    # Submit Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submit = st.button(
            "🔍 KI-System klassifizieren",
            type="primary",
            use_container_width=True
        )

    if submit:
        # Validierung
        if not system_name or not provider or not system_description:
            st.error("Bitte füllen Sie alle Pflichtfelder (*) aus.")
            return

        # Klassifizierung durchführen
        result = classify_ai_system(
            system_name=system_name,
            system_description=system_description,
            provider=provider,
            uses_subliminal_manipulation=uses_subliminal,
            exploits_vulnerable_groups=exploits_vulnerable,
            performs_social_scoring=social_scoring,
            predictive_policing_only_profiling=predictive_policing,
            predictive_policing_with_objective_facts=predictive_policing_facts,
            scrapes_facial_recognition=facial_scraping,
            emotion_recognition_work_education=emotion_work_edu,
            biometric_categorization_sensitive=biometric_sensitive,
            realtime_biometric_public=realtime_biometric,
            realtime_biometric_exception=realtime_biometric_exception,
            is_safety_component_annex_i=is_safety_component,
            is_product_annex_i=is_product,
            requires_third_party_assessment=requires_assessment,
            annex_i_product_type=annex_i_product if annex_i_product and annex_i_product != "Bitte auswählen..." else None,
            high_risk_domain=domain_key,
            high_risk_use_case=selected_use_case if selected_use_case and selected_use_case != "Bitte auswählen..." else None,
            performs_profiling=performs_profiling,
            narrow_procedural_task=narrow_procedural,
            improves_human_work=improves_human,
            detects_patterns_only=detects_patterns,
            preparatory_task_only=preparatory_only,
            interacts_with_humans=interacts_humans,
            generates_synthetic_content=generates_synthetic,
            generates_deepfakes=generates_deepfakes,
            emotion_recognition_medical_safety=emotion_medical,
            biometric_categorization_lawful=biometric_lawful,
            synthetic_content_types=synthetic_content_types,
            is_gpai=is_gpai,
            gpai_has_systemic_risk=gpai_systemic if is_gpai else False,
            reference_date=date.today()
        )

        # Ergebnis speichern
        st.session_state.current_result = {
            'result': result,
            'system_name': system_name,
            'system_description': system_description,
            'provider': provider
        }

        # Zur Klassifizierungsliste hinzufügen
        summary = create_classification_summary(result, system_name)
        summary['Anbieter'] = provider
        summary['Beschreibung'] = system_description
        st.session_state.classifications.append(summary)

        st.success("✅ Klassifizierung abgeschlossen! Wechseln Sie zum Tab 'Ergebnis & Export' für Details.")
        st.balloons()


def show_results():
    """Zeigt die Klassifizierungsergebnisse an."""

    st.header("Klassifizierungsergebnis")

    if not st.session_state.current_result:
        st.info("Noch keine Klassifizierung durchgeführt. Bitte führen Sie zuerst eine Klassifizierung durch.")
        return

    data = st.session_state.current_result
    result = data['result']
    system_name = data['system_name']
    provider = data['provider']
    system_description = data['system_description']

    # Risikostufe anzeigen
    risk_class = {
        RiskLevel.UNACCEPTABLE: "risk-unacceptable",
        RiskLevel.HIGH: "risk-high",
        RiskLevel.LIMITED: "risk-limited",
        RiskLevel.MINIMAL: "risk-minimal"
    }

    risk_emoji = {
        RiskLevel.UNACCEPTABLE: "🚫",
        RiskLevel.HIGH: "⚠️",
        RiskLevel.LIMITED: "ℹ️",
        RiskLevel.MINIMAL: "✅"
    }

    # GPAI-Indikator
    gpai_text = ""
    if result.is_gpai:
        gpai_text = "<p><strong>GPAI-Modell:</strong> Ja"
        if result.gpai_has_systemic_risk:
            gpai_text += " (mit systemischem Risiko)"
        gpai_text += "</p>"

    st.markdown(f"""
    <div class="{risk_class[result.risk_level]}">
        <h2>{risk_emoji[result.risk_level]} {result.risk_level.value}</h2>
        <p><strong>System:</strong> {system_name}</p>
        <p><strong>Anbieter:</strong> {provider}</p>
        {gpai_text}
    </div>
    """, unsafe_allow_html=True)

    # Warnungen anzeigen (falls vorhanden)
    if result.warnings:
        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ Warnungen</h4>
        </div>
        """, unsafe_allow_html=True)
        for warning in result.warnings:
            st.warning(warning)

    # Dokumentationspflicht bei Ausnahme
    if result.exception_documentation_required:
        st.markdown("""
        <div class="warning-box">
        <strong>📄 Dokumentationspflicht:</strong> Da Sie eine Ausnahme nach Artikel 6(3) geltend machen,
        müssen Sie dies dokumentieren und auf Anfrage der zuständigen Behörde nachweisen können.
        </div>
        """, unsafe_allow_html=True)

    # Details in Expanders
    with st.expander("📋 Begründung der Einstufung", expanded=True):
        for reason in result.reasons:
            st.markdown(f"- {reason}")

    with st.expander("📜 Anwendbare Artikel"):
        for article in result.applicable_articles:
            st.markdown(f"- {article}")

    with st.expander("⚖️ Rechtliche Pflichten"):
        for obligation in result.obligations:
            st.markdown(f"- {obligation}")

    # NEU: Transparenzpflichten (auch bei HIGH Risk)
    if result.transparency_obligations:
        with st.expander("🔍 Zusätzliche Transparenzpflichten (Art. 50)"):
            st.markdown("*Diese Transparenzpflichten gelten zusätzlich zu den oben genannten Pflichten:*")
            for obligation in result.transparency_obligations:
                st.markdown(f"- {obligation}")

    # NEU: GPAI-Pflichten
    if result.is_gpai and result.gpai_obligations:
        with st.expander("🤖 GPAI-spezifische Pflichten", expanded=True):
            st.markdown(f"""
            <div class="gpai-box">
            <strong>Allzweck-KI-Modell (GPAI)</strong><br>
            {'<em>Mit systemischem Risiko - zusätzliche Pflichten gelten!</em>' if result.gpai_has_systemic_risk else ''}
            </div>
            """, unsafe_allow_html=True)
            for obligation in result.gpai_obligations:
                st.markdown(f"- {obligation}")

    # NEU: Universelle Pflichten
    if result.universal_obligations:
        with st.expander("🌍 Universelle Pflichten (gelten für alle KI-Systeme)"):
            st.markdown("""
            <div class="universal-box">
            Diese Pflichten gelten unabhängig von der Risikoeinstufung:
            </div>
            """, unsafe_allow_html=True)
            for obligation in result.universal_obligations:
                st.markdown(f"- {obligation}")

    # NEU: Anwendbare Fristen
    if result.applicable_deadlines:
        with st.expander("📅 Relevante Fristen"):
            st.markdown("""
            <div class="deadline-box">
            <strong>Für Ihr System relevante Fristen des EU AI Act:</strong>
            </div>
            """, unsafe_allow_html=True)
            deadline_names = {
                "verbotene_praktiken": "Verbotene Praktiken (Art. 5)",
                "ki_kompetenz": "KI-Kompetenz (Art. 4)",
                "gpai": "GPAI-Modell-Pflichten",
                "transparenzpflichten": "Transparenzpflichten (Art. 50)",
                "hochrisiko_anhang_iii": "Hochrisiko-Systeme (Anhang III)",
                "hochrisiko_anhang_i": "Hochrisiko-Produkte (Anhang I)"
            }
            today = date.today()
            for key, deadline in result.applicable_deadlines.items():
                name = deadline_names.get(key, key)
                status = "✅ Bereits in Kraft" if today >= deadline else "⏳ Noch nicht in Kraft"
                st.markdown(f"- **{name}**: {deadline.strftime('%d.%m.%Y')} - {status}")

    with st.expander("💡 Empfehlungen"):
        for rec in result.recommendations:
            st.markdown(f"- {rec}")

    st.divider()

    # Export-Optionen
    st.subheader("📤 Export-Optionen")

    col1, col2, col3 = st.columns(3)

    with col1:
        # Markdown-Bericht
        markdown_report = generate_markdown_report(
            result, system_name, system_description, provider
        )
        st.download_button(
            "📄 Markdown-Bericht",
            markdown_report,
            f"ai_act_report_{system_name.replace(' ', '_')}.md",
            "text/markdown",
            use_container_width=True
        )

    with col2:
        # CSV-Export
        csv_data = export_to_csv([create_classification_summary(result, system_name)])
        st.download_button(
            "📊 CSV-Export",
            csv_data,
            f"ai_act_classification_{system_name.replace(' ', '_')}.csv",
            "text/csv",
            use_container_width=True
        )

    with col3:
        # Excel-Export
        excel_data = export_to_excel([create_classification_summary(result, system_name)])
        st.download_button(
            "📈 Excel-Export",
            excel_data,
            f"ai_act_classification_{system_name.replace(' ', '_')}.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    # Technische Dokumentation (nur für Hochrisiko)
    if result.risk_level == RiskLevel.HIGH:
        st.divider()
        st.subheader("📑 Technische Dokumentation (Anhang IV)")
        st.markdown("""
        Als Hochrisiko-KI-System müssen Sie eine technische Dokumentation nach Anhang IV erstellen.
        Hier können Sie eine Vorlage herunterladen:
        """)

        tech_doc = generate_technical_documentation_template(system_name, provider, result)
        st.download_button(
            "📋 Dokumentationsvorlage (Markdown)",
            tech_doc,
            f"technical_documentation_{system_name.replace(' ', '_')}.md",
            "text/markdown",
            use_container_width=True
        )


def show_reference():
    """Zeigt die Referenzinformationen an."""

    st.header("📚 EU AI Act Referenz")

    tab1, tab2, tab3 = st.tabs([
        "Verbotene Praktiken",
        "Hochrisiko-Bereiche",
        "Wichtige Fristen"
    ])

    with tab1:
        st.subheader("Verbotene Praktiken (Artikel 5)")
        for key, practice in PROHIBITED_PRACTICES.items():
            with st.expander(f"🚫 {practice['name']}"):
                st.markdown(f"**{practice['article']}**")
                st.markdown(practice['description'])

    with tab2:
        st.subheader("Hochrisiko-Anwendungsbereiche (Anhang III)")
        for key, domain in HIGH_RISK_DOMAINS.items():
            with st.expander(f"⚠️ {domain['name']}"):
                st.markdown(f"**{domain['article']}**")
                st.markdown("**Anwendungsfälle:**")
                for use_case in domain['use_cases']:
                    st.markdown(f"- {use_case}")

    with tab3:
        st.subheader("Wichtige Fristen des EU AI Act")

        timeline_data = [
            {"Datum": "01.08.2024", "Ereignis": "AI Act tritt in Kraft"},
            {"Datum": "02.02.2025", "Ereignis": "Verbotene Praktiken (Art. 5) und KI-Kompetenzpflichten gelten"},
            {"Datum": "02.08.2025", "Ereignis": "Governance-Regeln und GPAI-Modell-Pflichten gelten"},
            {"Datum": "02.08.2026", "Ereignis": "Vollständige Anwendung für Hochrisiko-Systeme (Anhang III)"},
            {"Datum": "02.08.2027", "Ereignis": "Hochrisiko-KI in regulierten Produkten (Anhang I)"}
        ]

        for item in timeline_data:
            st.markdown(f"**{item['Datum']}**: {item['Ereignis']}")


def show_all_classifications():
    """Zeigt alle bisherigen Klassifizierungen an."""

    st.header("💾 Alle Klassifizierungen")

    if not st.session_state.classifications:
        st.info("Noch keine Klassifizierungen durchgeführt.")
        return

    # Tabelle anzeigen
    import pandas as pd
    df = pd.DataFrame(st.session_state.classifications)

    # Spaltenauswahl für Anzeige
    display_cols = ['Systemname', 'Anbieter', 'Risikostufe', 'Klassifizierungsdatum']
    available_cols = [col for col in display_cols if col in df.columns]

    st.dataframe(df[available_cols], use_container_width=True)

    st.divider()

    # Massenexport
    st.subheader("📤 Alle Klassifizierungen exportieren")

    col1, col2 = st.columns(2)

    with col1:
        csv_all = export_to_csv(st.session_state.classifications)
        st.download_button(
            "📊 Alle als CSV",
            csv_all,
            f"alle_klassifizierungen_{datetime.now().strftime('%Y%m%d')}.csv",
            "text/csv",
            use_container_width=True
        )

    with col2:
        excel_all = export_to_excel(st.session_state.classifications)
        st.download_button(
            "📈 Alle als Excel",
            excel_all,
            f"alle_klassifizierungen_{datetime.now().strftime('%Y%m%d')}.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    st.divider()

    # Klassifizierungen löschen
    if st.button("🗑️ Alle Klassifizierungen löschen", type="secondary"):
        st.session_state.classifications = []
        st.session_state.current_result = None
        st.rerun()


if __name__ == "__main__":
    main()
