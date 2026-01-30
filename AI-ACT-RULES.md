# EU AI Act Klassifizierungsregeln

Zusammenfassung der wichtigsten Regeln zur Klassifikation von KI-Systemen nach der **EU AI Act (Verordnung (EU) 2024/1689)**.

Erstellt: 2026-01-30
Quellen: EU AI Act Regulation, classifier_logic.py, Web-Recherche

---

## 📊 Überblick: Risikobasiertes System

Der EU AI Act verwendet einen **risikobasierten Ansatz** mit vier Risikoklassen:

| Risikostufe | Beschreibung | Regulierung | Strafe bei Verstoß |
|-------------|--------------|-------------|-------------------|
| 🚫 **Unannehmbares Risiko** | Verbotene KI-Systeme | Vollständiges Verbot | Bis zu 35 Mio. EUR oder 7% des weltweiten Jahresumsatzes |
| ⚠️ **Hohes Risiko** | Kritische Anwendungen | Strenge Compliance-Pflichten | Bis zu 15 Mio. EUR oder 3% des weltweiten Jahresumsatzes |
| ℹ️ **Begrenztes Risiko** | Transparenz-relevante Systeme | Offenlegungspflichten | Bis zu 7,5 Mio. EUR oder 1,5% des weltweiten Jahresumsatzes |
| ✅ **Minimales Risiko** | Alle anderen KI-Systeme | Keine verpflichtenden Anforderungen | - |

---

## 🚫 Stufe 1: Unannehmbares Risiko (Verbotene Praktiken)

**Rechtsgrundlage**: Artikel 5

Diese KI-Systeme sind **in der EU vollständig verboten**, da sie Grundrechte und EU-Werte verletzen:

### Verbotene Praktiken

1. **Unterschwellige Manipulation (Art. 5(1)(a))**
   - KI-Systeme, die unterschwellige Techniken einsetzen, um das Bewusstsein zu umgehen
   - Ziel: Verhalten von Personen zu beeinflussen, das ihnen oder anderen schadet

2. **Ausnutzung von Schutzbedürftigen (Art. 5(1)(b))**
   - Ausnutzung von Schwächen aufgrund von Alter, Behinderung oder sozioökonomischer Lage
   - Führt zu Verhalten, das der Person oder anderen schadet

3. **Soziales Scoring (Art. 5(1)(c))**
   - Bewertung oder Klassifizierung von Personen basierend auf sozialem Verhalten
   - Führt zu nachteiliger Behandlung in nicht zusammenhängenden Kontexten

4. **Predictive Policing - nur Profiling (Art. 5(1)(d))**
   - Vorhersage von Straftaten **ausschließlich** basierend auf Profiling
   - Ohne Berücksichtigung objektiver, nachprüfbarer Fakten

5. **Gesichtserkennungs-Scraping (Art. 5(1)(e))**
   - Ungezieltes Scraping von Gesichtsbildern aus Internet oder CCTV
   - Zum Erstellen von Gesichtserkennungsdatenbanken

6. **Emotionserkennung am Arbeitsplatz/in Bildung (Art. 5(1)(f))**
   - Ableitung von Emotionen am Arbeitsplatz oder in Bildungseinrichtungen
   - **Ausnahme**: Medizinische oder sicherheitsrelevante Zwecke

7. **Biometrische Kategorisierung (sensibel) (Art. 5(1)(g))**
   - Kategorisierung durch Ableitung von:
     - Rasse oder ethnischer Herkunft
     - Politischen Meinungen
     - Gewerkschaftszugehörigkeit
     - Religiösen/philosophischen Überzeugungen
     - Sexuellem Verhalten oder sexueller Orientierung

8. **Echtzeit-Biometrie in öffentlichen Räumen (Art. 5(1)(h))**
   - Echtzeit-Fernidentifizierung in öffentlich zugänglichen Räumen
   - Für Strafverfolgungszwecke (mit sehr engen Ausnahmen)

### Konsequenzen

- ❌ Betrieb in der EU **nicht gestattet**
- ❌ Sofortige Einstellung aller Aktivitäten erforderlich
- ⚖️ Strafe: Bis zu **35 Mio. EUR** oder **7% des weltweiten Jahresumsatzes**

---

## ⚠️ Stufe 2: Hohes Risiko

**Rechtsgrundlage**: Artikel 6, Anhang I & III

Hochrisiko-KI-Systeme können über **zwei Wege (Pathways)** identifiziert werden:

### Pathway A: Regulierte Produkte (Anhang I)

Ein KI-System ist Hochrisiko, wenn **alle folgenden Bedingungen** erfüllt sind:

1. ✅ Das KI-System ist eine **Sicherheitskomponente** eines regulierten Produkts **ODER**
2. ✅ Das KI-System **IST selbst** ein reguliertes Produkt
3. ✅ Das Produkt erfordert eine **Drittanbieter-Konformitätsbewertung**

**Produktkategorien (Anhang I)**:
- Medizinprodukte (Klasse IIa und höher)
- In-vitro-Diagnostika
- Maschinen und Anlagen
- Zivilluftfahrtsysteme
- Kraftfahrzeuge und Anhänger
- Eisenbahnsysteme
- (und weitere)

**Anwendbare Frist**: 02.08.2027

### Pathway B: Anwendungsbereiche (Anhang III)

Ein KI-System ist Hochrisiko, wenn es in einem der folgenden Bereiche eingesetzt wird:

#### 1. Biometrie (Anhang III, Nr. 1)
- Biometrische Fernidentifikation (nicht nur Verifikation)
- Biometrische Kategorisierung nach sensiblen Merkmalen
- Emotionserkennungssysteme

#### 2. Kritische Infrastruktur (Anhang III, Nr. 2)
- Sicherheitskomponenten für digitale Infrastruktur
- Straßenverkehrsmanagement
- Wasser-/Gas-/Heizungs-/Stromversorgung

#### 3. Bildung und Berufsausbildung (Anhang III, Nr. 3)
- Zulassungsentscheidungen zu Bildungseinrichtungen
- Benotung und Bewertung von Lernenden
- Verhaltensüberwachung von Schülern/Studenten
- Prüfungsbetrugs-Erkennung

#### 4. Beschäftigung und Personalmanagement (Anhang III, Nr. 4)
- Rekrutierung und Lebenslauf-Screening
- Zielgerichtete Stellenanzeigen
- Bewerbungsgespräch-Auswertung
- Leistungsüberwachung von Mitarbeitern
- Beförderungs-/Kündigungsentscheidungen
- Aufgabenzuweisung

#### 5. Zugang zu wesentlichen Diensten (Anhang III, Nr. 5)
- Kreditwürdigkeitsprüfung
- Risikobewertung für Lebens-/Krankenversicherung
- Sozialleistungs-Berechtigung
- Notruf-Bewertung und Dispatching
- Medizinische Triage

#### 6. Strafverfolgung (Anhang III, Nr. 6)
- Risikobewertung für (Rück-)Fälligkeit
- Polygraph und ähnliche Werkzeuge
- Beweis-Zuverlässigkeitsbewertung
- Profiling bei Ermittlungen
- Kriminalitätsanalyse

#### 7. Migration und Grenzkontrolle (Anhang III, Nr. 7)
- Sicherheits-/Gesundheits-/Migrationsrisikobewertung
- Asyl-/Visa-/Aufenthaltsgenehmigungsprüfung
- Dokumenten-Echtheitsprüfung
- Personenerkennung und -identifikation

#### 8. Justiz und demokratische Prozesse (Anhang III, Nr. 8)
- Rechtsrecherche und -interpretation
- Alternative Streitbeilegung
- Beweisbewertung
- Beeinflussung von Gerichtsentscheidungen

### ⚠️ Wichtig: Ausnahmen von Hochrisiko

Ein KI-System aus Anhang III ist **NICHT hochriskant**, wenn es:

1. ✅ Nur eine **enge verfahrenstechnische Aufgabe** ausführt, ODER
2. ✅ Nur das Ergebnis **bereits abgeschlossener menschlicher Aktivität** verbessert, ODER
3. ✅ Nur **Entscheidungsmuster erkennt**, ohne menschliche Bewertung zu ersetzen, ODER
4. ✅ Nur eine **vorbereitende Aufgabe** für eine Bewertung ausführt

**❗ ABER**: Diese Ausnahmen gelten **NICHT**, wenn das System **Profiling natürlicher Personen** durchführt!

### Pflichten für Hochrisiko-Systeme

Anbieter müssen:

1. ✅ **Risikomanagementsystem** einrichten (Art. 9)
2. ✅ **Daten-Governance** sicherstellen (Art. 10)
3. ✅ **Technische Dokumentation** erstellen (Art. 11, Anhang IV)
4. ✅ **Automatische Protokollierung** implementieren (Art. 12)
5. ✅ **Transparenz** gegenüber Betreibern gewährleisten (Art. 13)
6. ✅ **Menschliche Aufsicht** ermöglichen (Art. 14)
7. ✅ **Genauigkeit, Robustheit und Cybersicherheit** sicherstellen (Art. 15)
8. ✅ **Konformitätsbewertung** durchführen (Art. 43)
9. ✅ **CE-Kennzeichnung** anbringen (Art. 48)
10. ✅ **Registrierung in EU-Datenbank** (Art. 49)
11. ✅ **Post-Market-Monitoring** einrichten (Art. 72)

**Anwendbare Frist**: 02.08.2026

---

## ℹ️ Stufe 3: Begrenztes Risiko (Transparenzpflichten)

**Rechtsgrundlage**: Artikel 50

Diese Kategorie umfasst KI-Systeme, die **spezifische Transparenzpflichten** auslösen, aber nicht als Hochrisiko gelten.

### Wann gelten Transparenzpflichten?

Ein KI-System unterliegt Transparenzpflichten, wenn es:

#### 1. Mit Menschen interagiert (Art. 50(1))

**Trigger**: Chatbots, virtuelle Assistenten, Konversations-KI

**Pflicht**:
- Nutzer müssen **darüber informiert werden**, dass sie mit einer KI interagieren
- Ausnahme: Wenn es aus dem Kontext **offensichtlich** ist

**Beispiele**:
- Kundenservice-Chatbots
- Virtuelle Assistenten
- AI-gestützte Live-Chat-Systeme

#### 2. Emotionen erkennt (Art. 50(3))

**Trigger**: Emotionserkennung für **medizinische oder Sicherheitszwecke**

**Pflicht**:
- Betroffene Personen müssen über die Verarbeitung informiert werden
- Gilt NICHT für Arbeitsplatz/Bildung (das wäre verboten!)

**Beispiele**:
- Medizinische Diagnosesysteme mit Emotionserkennung
- Sicherheitssysteme zur Gefahrenerkennung

#### 3. Biometrische Kategorisierung durchführt (Art. 50(3))

**Trigger**: Rechtmäßige biometrische Kategorisierung (z.B. Filterung von Datensätzen)

**Pflicht**:
- Information der betroffenen Personen
- Gilt NICHT für sensible Kategorien (das wäre verboten!)

#### 4. Synthetische Inhalte generiert (Art. 50(2))

**Trigger**: Generierung von Text, Audio, Bildern oder Video

**Pflicht**:
- **Maschinenlesbare Markierung** der Inhalte als KI-generiert
- Die Markierung muss:
  - ✅ Effektiv und interoperabel sein
  - ✅ Robust und zuverlässig sein
  - ✅ Dem Stand der Technik entsprechen

**Beispiele**:
- Text-Generatoren (GPT, Claude, etc.)
- Bild-Generatoren (DALL-E, Midjourney, Stable Diffusion)
- Video-Generatoren
- Audio/Musik-Generatoren

#### 5. Deepfakes generiert (Art. 50(4))

**Trigger**: Realistische synthetische Medien von echten Personen

**Pflicht**:
- **Offenlegungspflicht**: Inhalte müssen als künstlich erstellt/manipuliert gekennzeichnet werden
- **Ausnahmen** (nur minimale Offenlegung erforderlich):
  - Offensichtlich künstlerische Inhalte
  - Offensichtlich kreative Inhalte
  - Offensichtlich satirische Inhalte
  - Offensichtlich fiktionale Inhalte

**Wichtig**: Auch **rechtmäßige** Deepfakes müssen gekennzeichnet werden!

**Beispiele**:
- Face-Swap-Videos
- Voice-Cloning
- Realistische KI-Avatare echter Personen

### Code of Practice (Verhaltenskodex)

**Status**: Erster Entwurf veröffentlicht am 17.12.2025

Der **Code of Practice on Transparency of AI-Generated Content** bietet praktische Anleitungen:

#### Empfohlene Kennzeichnungsmethoden:

**Für Video**:
- Persistente visuelle Indikatoren
- Eröffnungs-Disclaimer
- Bei Live-Video: Durchgehende Kennzeichnung

**Für Bilder**:
- Sichtbare Labels oder Disclaimer
- Wasserzeichen
- Metadaten-Markierung

**Für Audio**:
- Hörbare Disclaimer am Anfang
- Bei längeren Inhalten: Wiederholte Hinweise

**Für Text**:
- Gemeinsames Symbol/Icon
- Sichtbar beim ersten Kontakt
- Konsistente Platzierung

#### Zeitplan:
- **März 2026**: Zweiter Entwurf erwartet
- **Juni 2026**: Finale Version erwartet
- **02.08.2026**: Artikel 50 tritt in Kraft

### Strafen bei Verstoß

⚖️ Bis zu **7,5 Mio. EUR** oder **1,5% des weltweiten Jahresumsatzes**

---

## ✅ Stufe 4: Minimales Risiko

**Keine verpflichtenden Anforderungen des EU AI Act**

### Was ist Minimales Risiko?

Dies ist die **Standard-Kategorie** für alle KI-Systeme, die nicht in die anderen Kategorien fallen:

- ✅ Keine verbotenen Praktiken
- ✅ Kein Hochrisiko (weder Pathway A noch B)
- ✅ Keine Transparenzpflichten

**Wichtig**: Die **überwiegende Mehrheit** aller derzeit in der EU eingesetzten KI-Systeme fällt in diese Kategorie!

### Beispiele für Minimales Risiko

- **Spam-Filter** für E-Mails
- **Empfehlungssysteme** (Produkte, Inhalte)
- **KI-gestützte Videospiele**
- **Inventar-Management-Systeme**
- **Wettervorhersage-Systeme**
- **Routenplanung** (nicht für kritische Infrastruktur)
- **Übersetzungs-Tools** (ohne Interaktion)
- **Automatische Bildoptimierung**
- **KI-gestützte Suchmaschinen**
- **Produktionsoptimierung** (nicht sicherheitskritisch)

### Freiwillige Maßnahmen

Obwohl keine Pflichten bestehen, wird **empfohlen**:

#### 1. Freiwillige Verhaltenskodizes (Art. 95)

Die Europäische Kommission und die Mitgliedstaaten **ermutigen** Anbieter zur freiwilligen Anwendung von:

- ✅ Risikomanagementsystemen
- ✅ Daten-Governance-Praktiken
- ✅ Transparenzmaßnahmen
- ✅ Menschlicher Aufsicht
- ✅ Genauigkeits- und Robustheitsanforderungen

**Ziel**: Best Practices auch für nicht-regulierte Systeme etablieren

#### 2. KI-Kompetenz (AI Literacy)

**Pflicht für ALLE Anbieter und Betreiber** (auch Minimal Risk!):

- ✅ Sicherstellen, dass Mitarbeiter, die mit KI-Systemen arbeiten, über ausreichende **KI-Kompetenz** verfügen
- ✅ Training und Schulung bereitstellen

#### 3. DSGVO-Konformität

**Wichtig**: KI-Systeme unterliegen weiterhin der **DSGVO** (Datenschutz-Grundverordnung)!

- ✅ Rechtmäßigkeit der Datenverarbeitung
- ✅ Zweckbindung
- ✅ Datenminimierung
- ✅ Betroffenenrechte (Auskunft, Löschung, etc.)
- ✅ Datenschutz-Folgenabschätzung bei Bedarf

### General Purpose AI (GPAI) / Allzweck-KI

**Besondere Kategorie innerhalb von Minimal Risk**

**Definition**: KI-Modelle, die eine Vielzahl von Aufgaben ausführen können

**Beispiele**: GPT-4, Claude, Gemini, Llama

#### Transparenzpflichten für GPAI (ab 02.08.2025):

1. ✅ **Technische Dokumentation** erstellen und aktualisieren
2. ✅ **Urheberrechtliche Informationen** bereitstellen
   - Ausreichend detaillierte Zusammenfassung der für das Training verwendeten Inhalte
3. ✅ **Downstream-Provider** über Capabilities und Limitations informieren

#### GPAI mit systemischen Risiken:

Wenn das Modell besonders **leistungsfähig** ist oder **weitverbreitet** genutzt wird:

- ✅ Modell-Evaluierungen durchführen
- ✅ Schwerwiegende Vorfälle verfolgen und melden
- ✅ Angemessene Cybersicherheit sicherstellen
- ✅ Energieeffizienz berücksichtigen

#### Compliance-Nachweis:

- Anbieter können Konformität durch **freiwillige Verhaltenskodizes** nachweisen
- Bis harmonisierte Normen veröffentlicht werden

### Vorteile der Freiwilligkeit

Auch ohne Pflichten können freiwillige Maßnahmen:

- 🎯 **Vertrauen** bei Nutzern schaffen
- 🎯 **Wettbewerbsvorteile** bieten
- 🎯 **Haftungsrisiken** reduzieren
- 🎯 **Zukünftige Compliance** vorbereiten (falls sich Einstufung ändert)
- 🎯 **Best Practices** der Branche etablieren

---

## 🔄 Klassifizierungs-Algorithmus

### Entscheidungsbaum

```
1. Prüfung: Verbotene Praktiken (Art. 5)
   ├─ JA → 🚫 UNANNEHMBARES RISIKO
   └─ NEIN → Weiter zu 2.

2. Prüfung: Hochrisiko Pathway A (Anhang I)
   ├─ Sicherheitskomponente ODER Produkt selbst?
   │  ├─ JA → Erfordert Drittanbieter-Bewertung?
   │  │  ├─ JA → ⚠️ HOHES RISIKO
   │  │  └─ NEIN → Weiter zu 3.
   │  └─ NEIN → Weiter zu 3.

3. Prüfung: Hochrisiko Pathway B (Anhang III)
   ├─ System in Hochrisiko-Bereich (Anhang III)?
   │  ├─ JA → Ausnahmen anwendbar?
   │  │  ├─ System führt Profiling durch?
   │  │  │  ├─ JA → Ausnahmen NICHT anwendbar → ⚠️ HOHES RISIKO
   │  │  │  └─ NEIN → Prüfe Ausnahmekriterien
   │  │  │     ├─ Ausnahme trifft zu → Weiter zu 4.
   │  │  │     └─ Ausnahme trifft NICHT zu → ⚠️ HOHES RISIKO
   │  └─ NEIN → Weiter zu 4.

4. Prüfung: Transparenzpflichten (Art. 50)
   ├─ Interagiert mit Menschen? → ℹ️ BEGRENZTES RISIKO
   ├─ Generiert Deepfakes? → ℹ️ BEGRENZTES RISIKO
   ├─ Generiert synthetische Inhalte? → ℹ️ BEGRENZTES RISIKO
   ├─ Emotionserkennung (medizinisch/Sicherheit)? → ℹ️ BEGRENZTES RISIKO
   ├─ Rechtmäßige biometrische Kategorisierung? → ℹ️ BEGRENZTES RISIKO
   └─ Keine Trigger → Weiter zu 5.

5. Standard: ✅ MINIMALES RISIKO
```

### Wichtige Hinweise zur Klassifizierung

1. **Verbotene Praktiken haben Vorrang**: Wenn auch nur eine verbotene Praktik erfüllt ist, ist das System verboten - unabhängig von anderen Merkmalen.

2. **Hochrisiko-Ausnahmen sind eng**: Die Ausnahmen in Anhang III gelten NUR, wenn das System KEIN Profiling durchführt.

3. **Mehrfache Transparenzpflichten möglich**: Ein System kann mehrere Transparenz-Trigger erfüllen (z.B. Chatbot + synthetische Inhalte).

4. **Dokumentationspflicht**: Anbieter, die behaupten, ein Anhang-III-System sei NICHT hochriskant, müssen dies dokumentieren und auf Anfrage nachweisen.

5. **GPAI ist meist Minimal Risk**: Aber mit eigenen spezifischen Transparenz- und ggf. Risikomanagement-Pflichten.

---

## 📅 Zeitplan und Fristen

| Datum | Ereignis | Betroffene Systeme |
|-------|----------|-------------------|
| **01.08.2024** | AI Act tritt in Kraft | - |
| **02.02.2025** | Verbotene Praktiken gelten<br>KI-Kompetenzpflichten gelten | 🚫 Unannehmbares Risiko<br>✅ Alle Systeme |
| **02.08.2025** | Governance-Regeln gelten<br>GPAI-Modell-Pflichten gelten | Governance-Strukturen<br>General Purpose AI |
| **02.08.2026** | Vollständige Anwendung für Hochrisiko<br>Transparenzpflichten gelten | ⚠️ Hohes Risiko (Anhang III)<br>ℹ️ Begrenztes Risiko |
| **02.08.2027** | Hochrisiko in regulierten Produkten | ⚠️ Hohes Risiko (Anhang I) |

---

## 📚 Quellen

### Offizielle EU-Quellen
- [EU AI Act Regulation (2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [Article 5: Prohibited AI Practices](https://artificialintelligenceact.eu/article/5/)
- [Article 6: Classification Rules for High-Risk AI Systems](https://artificialintelligenceact.eu/article/6/)
- [Article 50: Transparency Obligations](https://artificialintelligenceact.eu/article/50/)
- [Article 95: Codes of Conduct for Voluntary Application](https://artificialintelligenceact.eu/article/95/)
- [Annex III: High-Risk AI Systems](https://artificialintelligenceact.eu/annex/3/)

### Implementierungsleitfäden
- [Code of Practice on marking and labelling of AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
- [AI Act | Shaping Europe's digital future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/)

### Analyseartikel
- [Understanding EU AI Act Risk Categories - Security Compass](https://www.securitycompass.com/blog/understanding-eu-ai-act-risk-categories/)
- [AI Risk Classification: Guide to EU AI Act Risk Categories - GDPR Local](https://gdprlocal.com/ai-risk-classification/)
- [What the EU's New AI Code of Practice Means for Labeling Deepfakes - TechPolicy.Press](https://www.techpolicy.press/what-the-eus-new-ai-code-of-practice-means-for-labeling-deepfakes/)

### Interne Quellen
- `classifier_logic.py` - Implementierung der Klassifizierungslogik

---

## ⚠️ Haftungsausschluss

Diese Zusammenfassung dient nur zu Informationszwecken und ersetzt keine rechtliche Beratung. Die Klassifizierung basiert auf den zum Erstellungszeitpunkt (Januar 2026) verfügbaren Informationen zum EU AI Act.

Bei Unsicherheiten oder für verbindliche Einschätzungen konsultieren Sie bitte:
- Einen auf EU AI Act spezialisierten Rechtsanwalt
- Die zuständigen nationalen Aufsichtsbehörden
- Den offiziellen EU AI Act Service Desk

Die Regulierung entwickelt sich kontinuierlich weiter. Überprüfen Sie regelmäßig auf Updates und neue Leitlinien.
