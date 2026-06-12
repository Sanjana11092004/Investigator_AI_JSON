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

            return (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "demographics"
                )
            )

        if intent == "subject_medications":

            return (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "medications"
                )
            )

        if intent == "subject_labs":

            return (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "labs"
                )
            )

        if intent == "subject_ae":

            return (
                self.engine
                .get_subject_data(
                    value
                )
                .get(
                    "adverse_events"
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