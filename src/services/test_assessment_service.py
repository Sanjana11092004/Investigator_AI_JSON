from src.services.investigator_assessment_service import (
    InvestigatorAssessmentService
)

service = (
    InvestigatorAssessmentService()
)

result = (

    service.generate_subject_assessment(
        "SUBJ-0001"
    )

)

print(
    result
)