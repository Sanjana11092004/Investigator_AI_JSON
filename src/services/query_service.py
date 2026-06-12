from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class QueryService:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

    def get_subject(
        self,
        subject_id: str
    ):

        return (
            self.engine
            .get_subject_data(
                subject_id
            )
        )

    def get_study(
        self,
        study_id: str
    ):

        return (
            self.engine
            .get_study(
                study_id
            )
        )

    def get_patient(
        self,
        patient_id: str
    ):

        return (
            self.engine
            .get_patient(
                patient_id
            )
        )