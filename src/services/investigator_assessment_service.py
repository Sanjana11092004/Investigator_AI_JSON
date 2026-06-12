from src.rag.investigator_rag import (
    InvestigatorRAG
)


class InvestigatorAssessmentService:

    def __init__(self):

        self.rag = (
            InvestigatorRAG()
        )

    def generate_subject_assessment(
        self,
        subject_id: str
    ):

        assessment = (

            self.rag
            .investigate_subject(
                subject_id
            )

        )

        return {

            "subject_id":
            subject_id,

            "assessment":
            assessment
        }