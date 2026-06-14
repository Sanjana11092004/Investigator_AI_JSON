class ContextBuilder:

    def build_patient_context(
        self,
        patient: dict
    ) -> str:

        if not patient:
            return "No patient data found."

        context = f"""
Patient ID: {patient.get('patient_id')}

Age: {patient.get('age')}

Gender: {patient.get('gender')}

Chief Complaint:
{patient.get('chief_complaint')}

Diagnoses:
{', '.join(patient.get('diagnoses', []))}

Medications:
{', '.join(patient.get('medications', []))}

Adverse Events:
{', '.join(patient.get('adverse_events', []))}
"""

        return context.strip()

    def build_study_context(
        self,
        study: dict
    ) -> str:

        if not study:
            return "No study data found."

        protocol = (
            study
            .get("data", {})
            .get("protocolSection", {})
        )

        identification = (
            protocol.get(
                "identificationModule",
                {}
            )
        )

        status = (
            protocol.get(
                "statusModule",
                {}
            )
        )

        conditions = (
            protocol.get(
                "conditionsModule",
                {}
            )
        )

        design = (
            protocol.get(
                "designModule",
                {}
            )
        )

        summary = (
            protocol.get(
                "descriptionModule",
                {}
            )
        )

        interventions = (
            protocol.get(
                "armsInterventionsModule",
                {}
            )
        )

        context = f"""
    Study ID:
    {identification.get('nctId')}

    Title:
    {identification.get('briefTitle')}

    Official Title:
    {identification.get('officialTitle')}

    Status:
    {status.get('overallStatus')}

    Study Type:
    {design.get('studyType')}

    Phase:
    {', '.join(design.get('phases', []))}

    Conditions:
    {', '.join(conditions.get('conditions', []))}

    Summary:
    {summary.get('briefSummary')}

    Interventions:
    {', '.join(
        [
            i.get('name')
            for i in interventions.get(
                'interventions',
                []
            )
        ]
    )}
    """

        return context.strip()


    def build_subject_context(
        self,
        subject: dict
    ) -> str:

        if not subject:
            return "No subject data found."

        demographics = (
            subject.get(
                "demographics",
                []
            )
        )

        medications = (
            subject.get(
                "medications",
                []
            )
        )

        adverse_events = (
            subject.get(
                "adverse_events",
                []
            )
        )

        medical_history = (
            subject.get(
                "medical_history",
                []
            )
        )

        labs = (
            subject.get(
                "labs",
                []
            )
        )

        dm = (
            demographics[0]
            if demographics
            else {}
        )

        lab_summary = []

        for lab in labs[:10]:

            lab_summary.append(

                f"{lab.get('LBTESTCD')}: "
                f"{lab.get('LBSTRESN')} "
                f"{lab.get('LBSTRESU')} "
                f"({lab.get('LBNRIND')})"

            )

        context = f"""
    Subject ID:
    {dm.get('USUBJID')}

    Age:
    {dm.get('AGE')}

    Sex:
    {dm.get('SEX')}

    Diagnosis:
    {dm.get('DIAGNOSIS')}

    BMI:
    {dm.get('BMI')}

    Medical History:
    {', '.join(
        [
            mh.get('MHTERM')
            for mh in medical_history
        ]
    )}

    Medications:
    {', '.join(
        [
            med.get('CMTRT')
            for med in medications
        ]
    )}

    Adverse Events:
    {', '.join(
        [
            ae.get('AETERM')
            for ae in adverse_events
        ]
    )}

    Key Labs:
    {chr(10).join(lab_summary)}
    """

        return context.strip()