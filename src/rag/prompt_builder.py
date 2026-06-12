class PromptBuilder:

    def _format_labs(
        self,
        labs
    ):

        output = []

        for lab_name, data in labs.items():

            output.append(

                f"""
    {lab_name}
    - Measurements: {data['count']}
    - Trend: {data['trend']}
    - Abnormal Results: {data['abnormal_count']}
    - Clinical Flag: {data['clinical_flag']}
    """

            )

        return "\n".join(output)
    
    def build_subject_prompt(
        self,
        context: dict
    ):

        demographics = (
            context.get(
                "demographics",
                {}
            )
        )

        medications = (
            context.get(
                "medications",
                {}
            )
        )

        labs = (
            context.get(
                "labs",
                {}
            )
        )

        lab_summary = (
            self._format_labs(
                labs
            )
        )

        adverse_events = (
            context.get(
                "adverse_events",
                {}
            )
        )

        prompt = f"""
You are an experienced Clinical Investigator and Pharmacovigilance Reviewer.

Analyze the supplied clinical trial subject data.

Rules:
- Do not invent information.
- Do not assume missing facts.
- Base conclusions only on the supplied context.
- Clearly separate observations from interpretations.
- Use professional clinical language.
- Do not diagnose conditions that are not explicitly present.
- Do not infer causality.
- Do not suggest drug-event relationships unless explicitly supported by the supplied data.
- If evidence is insufficient, state that additional review is required.
- Do not infer diagnoses from medication names.
- Do not infer causality unless explicitly supported by the supplied data.
- Medications alone do not establish a diagnosis.
- Abnormal laboratory results alone do not establish a diagnosis.
- Use only explicitly documented diagnoses.
- If a finding is observed but unexplained, report it as an observation requiring review.

==================================================
SUBJECT CONTEXT
==================================================

Subject ID:
{context.get("subject_id")}

DEMOGRAPHICS

Age:
{demographics.get("age")}

Sex:
{demographics.get("sex")}

Country:
{demographics.get("country")}

Diagnosis:
{demographics.get("diagnosis")}

Treatment Arm:
{demographics.get("treatment_arm")}

BMI:
{demographics.get("bmi")}

Smoking Status:
{demographics.get("smoking_status")}

Alcohol Use:
{demographics.get("alcohol_use")}

==================================================
MEDICATIONS
==================================================

Medication Count:
{medications.get("medication_count")}

Ongoing Medications:
{medications.get("ongoing_medications")}

All Medications:
{medications.get("all_medications")}

==================================================
LABORATORY SUMMARY
==================================================

{lab_summary}

==================================================
ADVERSE EVENTS
==================================================

Event Count:
{adverse_events.get("event_count")}

Serious Events:
{adverse_events.get("serious_events")}

Events:
{adverse_events.get("events")}

==================================================
ASSESSMENT OBJECTIVES
==================================================

1. Summarize the subject profile.
2. Report only medical conditions explicitly present in the supplied data.
3. Summarize medication exposure exactly as documented. Do not infer diagnoses, indications, or treatment purposes unless explicitly stated in the supplied data.
4. Review laboratory findings.
5. Highlight abnormal laboratory findings.
6. Review adverse events.
7. Describe any observed temporal or clinical associations
present in the supplied data.
8. Identify findings that may warrant further review.
9. Do not infer causality unless explicitly supported
by the supplied data.

==================================================
OUTPUT FORMAT
==================================================

SUBJECT OVERVIEW

MEDICAL PROFILE

MEDICATION REVIEW

LABORATORY ASSESSMENT

ADVERSE EVENT REVIEW

FINDINGS REQUIRING FURTHER REVIEW

OVERALL INVESTIGATOR ASSESSMENT
"""

        return prompt