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

        sponsors = (
            protocol.get(
                "sponsorCollaboratorsModule",
                {}
            )
        )

        outcomes = (
            protocol.get(
                "outcomesModule",
                {}
            )
        )

        eligibility = (
            protocol.get(
                "eligibilityModule",
                {}
            )
        )

        locations = (
            protocol.get(
                "contactsLocationsModule",
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

    Acronym:
    {identification.get('acronym')}

    Sponsor:
    {sponsors.get(
        'leadSponsor',
        {}
    ).get(
        'name'
    )}

    Status:
    {status.get('overallStatus')}

    Study Type:
    {design.get('studyType')}

    Phase:
    {', '.join(design.get('phases', []))}

    Enrollment:
    {design.get(
        'enrollmentInfo',
        {}
    ).get(
        'count'
    )}

    Study Start Date:
    {status.get(
        'startDateStruct',
        {}
    ).get(
        'date'
    )}

    Primary Completion Date:
    {status.get(
        'primaryCompletionDateStruct',
        {}
    ).get(
        'date'
    )}

    Study Completion Date:
    {status.get(
        'completionDateStruct',
        {}
    ).get(
        'date'
    )}

    Conditions:
    {', '.join(
        conditions.get(
            'conditions',
            []
        )
    )}

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

    Primary Outcomes:
    {', '.join(
        [
            outcome.get('measure')
            for outcome in outcomes.get(
                'primaryOutcomes',
                []
            )
        ]
    )}

    Secondary Outcomes:
    {', '.join(
        [
            outcome.get('measure')
            for outcome in outcomes.get(
                'secondaryOutcomes',
                []
            )
        ]
    )}

    Eligibility Criteria:
    {eligibility.get(
        'eligibilityCriteria'
    )}

    Eligible Sex:
    {eligibility.get('sex')}

    Minimum Age:
    {eligibility.get('minimumAge')}

    Locations:
    {', '.join(
        [
            f"{location.get('facility')} - {location.get('city')}, {location.get('country')}"
            for location in locations.get(
                'locations',
                []
            )
        ]
    )}
    """

        return context.strip()