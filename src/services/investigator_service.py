from src.retrieval.natural_language_router import (
    NaturalLanguageRouter
)

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

from src.retrieval.aggregations import (
    Aggregations
)

from src.session.session_manager import (
    SessionManager
)

from src.services.response_formatter import (
    ResponseFormatter
)


class InvestigatorService:

    def __init__(self):

        self.router = (
            NaturalLanguageRouter()
        )

        self.engine = (
            JSONQueryEngine()
        )

        self.agg = (
            Aggregations()
        )

        self.sessions = (
            SessionManager()
        )

        self.formatter = (
            ResponseFormatter()
        )

    def ask(
        self,
        question: str,
        session_id: str = "default"
    ):

        self.sessions.create_session(
            session_id
        )

        intent, value = (
            self.router.route(
                question
            )
        )

        session = self.sessions.get(
            session_id
        )

        if (
            value is None
            and
            session
        ):

            active_subject = (
                session.get(
                    "active_subject_id"
                )
            )

            if active_subject:

                if intent in [

                    "subject_demographics",
                    "subject_medications",
                    "subject_labs",
                    "subject_ae",
                    "subject_all"

                ]:

                    value = active_subject

        if value and value.startswith(
            "SUBJ-"
        ):

            self.sessions.set_active_subject(
                session_id,
                value
            )

        if intent == "subject_all":

            return (
                self.engine
                .get_subject_data(
                    value
                )
            )

        if intent == "subject_demographics":

            records = (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "demographics"
                )
            )

            return (
                self.formatter
                .format_demographics(
                    records
                )
            )

        if intent == "subject_medications":

            records = (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "medications"
                )
            )

            return (
                self.formatter
                .format_medications(
                    records
                )
            )

        if intent == "subject_labs":

            records = (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "labs"
                )
            )

            return (
                self.formatter
                .format_labs(
                    records
                )
            )

        if intent == "subject_ae":

            records = (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "adverse_events"
                )
            )

            return (
                self.formatter
                .format_adverse_events(
                    records
                )
            )

        if intent == "study":

            return (
                self.engine
                .get_study(
                    value
                )
            )

        if intent == "average_age":

            return {

                "average_age":

                self.agg.average_age()

            }

        if intent == "top_diagnoses":

            return {

                "top_diagnoses":

                self.agg.top_diagnoses()

            }

        if intent == "top_medications":

            return {

                "top_medications":

                self.agg.top_medications()

            }

        return {

            "message":

            "Unable to determine intent"
        }