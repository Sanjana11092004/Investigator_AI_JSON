
from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

from src.retrieval.aggregations import (
    Aggregations
)


from src.session.session_manager import (
    SessionManager
)

from src.services.response_generation_service import (
    ResponseGenerationService
)

from src.services.intent_classification_service import (
    IntentClassificationService
)

from src.services.context_builder import (
    ContextBuilder
)


class InvestigatorService:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

        self.agg = (
            Aggregations()
        )

        self.sessions = (
            SessionManager()
        )

        self.response_generator = (
            ResponseGenerationService()
        )

        self.intent_classifier = (
            IntentClassificationService()
        )

        self.context_builder = (
            ContextBuilder()
        )

    def ask(
        self,
        question: str,
        session_id: str = "default"
    ):

        self.sessions.create_session(
            session_id
        )

        session = (
            self.sessions.get(
                session_id
            )
        )

        classification = (
            self.intent_classifier
            .classify(
                question,
                session
            )
        )
        print("CLASSIFICATION =", classification)

        intent = (
            classification.get(
                "intent"
            )
        )

        value = (
            classification.get(
                "entity_id"
            )
        )

        # -------------------------
        # SESSION MEMORY RESOLUTION
        # -------------------------

        if value is None:

            if intent == "patient":

                value = (
                    session.get(
                        "active_patient_id"
                    )
                )

            elif intent == "study":

                value = (
                    session.get(
                        "active_study_id"
                    )
                )

            elif intent == "subject":

                value = (
                    session.get(
                        "active_subject_id"
                    )
                )

        # -------------------------
        # STORE ACTIVE ENTITY
        # -------------------------

        if isinstance(
            value,
            str
        ):

            if value.startswith(
                "PT-"
            ):

                self.sessions.set_active_patient(
                    session_id,
                    value
                )

            elif value.startswith(
                "SUBJ-"
            ):

                self.sessions.set_active_subject(
                    session_id,
                    value
                )

            elif value.startswith(
                "NCT"
            ):

                self.sessions.set_active_study(
                    session_id,
                    value
                )

        # -------------------------
        # SUBJECT
        # -------------------------

        if intent == "subject":

            subject_data = (
                self.engine
                .get_subject_data(
                    value
                )
            )

            context = (
                self.context_builder
                .build_subject_context(
                    subject_data
                )
            )

            return (
                self.response_generator
                .generate_response(
                    question,
                    context
                )
            )

        # -------------------------
        # PATIENT
        # -------------------------

        if intent == "patient":

            patient_data = (
                self.engine
                .get_patient(
                    value
                )
            )

            context = (
                self.context_builder
                .build_patient_context(
                    patient_data
                )
            )

            return (
                self.response_generator
                .generate_response(
                    question,
                    context
                )
            )

        # -------------------------
        # STUDY
        # -------------------------

        if intent == "study":

            study_data = (
                self.engine
                .get_study(
                    value
                )
            )

            context = (
                self.context_builder
                .build_study_context(
                    study_data
                )
            )

            return (
                self.response_generator
                .generate_response(
                    question,
                    context
                )
            )

        # -------------------------
        # ANALYTICS
        # -------------------------

        if intent == "analytics":

            return {

                "average_age":
                self.agg.average_age(),

                "top_diagnoses":
                self.agg.top_diagnoses(),

                "top_medications":
                self.agg.top_medications()
            }

        # -------------------------
        # OUT OF SCOPE
        # -------------------------

        return {

            "message":

            (
                "This system supports clinical trial "
                "investigations only. "
                "Please ask about patients, subjects, "
                "studies, medications, diagnoses, "
                "laboratory results, adverse events, "
                "clinical summaries, cohorts, or analytics."
            )

        }
        
        