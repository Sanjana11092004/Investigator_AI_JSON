from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

from src.services.response_formatter import (
    ResponseFormatter
)


class ContextBuilder:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

        self.formatter = (
            ResponseFormatter()
        )

    def build_subject_context(
        self,
        subject_id: str
    ):

        subject_data = (
            self.engine
            .get_subject_data(
                subject_id
            )
        )

        demographics = (
            self.formatter
            .format_demographics(
                subject_data.get(
                    "demographics",
                    []
                )
            )
        )

        medications = (
            self.formatter
            .format_medications(
                subject_data.get(
                    "medications",
                    []
                )
            )
        )

        labs = (
            self.formatter
            .format_labs(
                subject_data.get(
                    "labs",
                    []
                )
            )
        )

        adverse_events = (
            self.formatter
            .format_adverse_events(
                subject_data.get(
                    "adverse_events",
                    []
                )
            )
        )

        return {

            "subject_id":
            subject_id,

            "demographics":
            demographics,

            "medications":
            medications,

            "labs":
            labs,

            "adverse_events":
            adverse_events
        }