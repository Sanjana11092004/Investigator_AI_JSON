from src.retrieval.natural_language_router import (
    NaturalLanguageRouter
)

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

from src.retrieval.aggregations import (
    Aggregations
)

from src.retrieval.cohort_service import (
    CohortService
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

        self.cohort = (
            CohortService()
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

        session = (
            self.sessions.get(
                session_id
            )
        )

        # -------------------------
        # SESSION SUBJECT MEMORY
        # -------------------------

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

        # -------------------------
        # STORE ACTIVE SUBJECT
        # -------------------------

        if (
            isinstance(
                value,
                str
            )
            and
            value.startswith(
                "SUBJ-"
            )
        ):

            self.sessions.set_active_subject(
                session_id,
                value
            )

        # -------------------------
        # COHORT QUERIES
        # -------------------------

        if intent == "cohort_diagnosis":

            cohort = (
                self.cohort
                .diagnosis(
                    value
                )
            )

            self.sessions.set_active_cohort(
                session_id,
                cohort
            )

            return {

                "cohort_size":
                len(cohort),

                "subjects":
                cohort
            }

        if intent == "cohort_female":

            current = (
                session.get(
                    "active_cohort",
                    []
                )
            )

            result = (
                self.cohort.sex(
                    current,
                    "F"
                )
            )

            self.sessions.set_active_cohort(
                session_id,
                result
            )

            return {

                "cohort_size":
                len(result),

                "subjects":
                result
            }

        if intent == "cohort_male":

            current = (
                session.get(
                    "active_cohort",
                    []
                )
            )

            result = (
                self.cohort.sex(
                    current,
                    "M"
                )
            )

            self.sessions.set_active_cohort(
                session_id,
                result
            )

            return {

                "cohort_size":
                len(result),

                "subjects":
                result
            }

        if intent == "cohort_age_gt":

            current = (
                session.get(
                    "active_cohort",
                    []
                )
            )

            result = (
                self.cohort
                .age_greater_than(
                    current,
                    value
                )
            )

            self.sessions.set_active_cohort(
                session_id,
                result
            )

            return {

                "cohort_size":
                len(result),

                "subjects":
                result
            }

        # -------------------------
        # SUBJECT QUERIES
        # -------------------------

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

        # -------------------------
        # STUDY
        # -------------------------

        if intent == "study":

            return (
                self.engine
                .get_study(
                    value
                )
            )

        # -------------------------
        # AGGREGATIONS
        # -------------------------

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
        
        if intent == "out_of_scope":

            return {

                "message":

                (
                    "This system supports clinical trial "
                    "investigations only. "
                    "Please ask about subjects, studies, "
                    "demographics, medications, labs, "
                    "adverse events, cohorts, or analytics."
                )

            }
        
        return {
            "message": "Unable to determine intent"
        }

        