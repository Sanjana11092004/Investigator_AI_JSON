
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

from src.services.analytics_service import (
    AnalyticsService
)

from src.services.reasoning_service import (
    ReasoningService
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

        self.analytics = (
            AnalyticsService()
        )

        self.reasoning = (
            ReasoningService()
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

        print("\nQUESTION RECEIVED:")
        print(question)
        print()

        classification = (
            self.intent_classifier
            .classify(
                question,
                session
            )
        )

        print("\nCLASSIFICATION:")
        print(classification)
        print()

        if (
            classification.get("action")
            == "compare"
            and
            not classification.get(
                "entity_id"
            )
        ):

            previous = (
                session.get(
                    "last_compared_entities",
                    []
                )
            )

            if len(previous) == 2:

                classification[
                    "entity_id"
                ] = ", ".join(
                    previous
                )

        if (
            classification.get("action")
            ==
            "compare"
        ):

            entity_ids = (
                classification.get(
                    "entity_id"
                )
            )

            if not entity_ids:

                return {
                    "message":
                    "Comparison requires two entities."
                }

            if isinstance(
                entity_ids,
                list
            ):

                ids = [

                    str(x).strip()

                    for x in entity_ids

                    if str(x).strip()

                ]

            else:

                ids = [

                    x.strip()

                    for x in str(
                        entity_ids
                    ).split(",")

                    if x.strip()

                ]

            if len(ids) != 2:

                return {
                    "message":
                    "Comparison requires two entities."
                }

            self.sessions.set_last_comparison(
                session_id,
                ids
            )

            if (
                classification.get(
                    "entity_type"
                )
                ==
                "patient"
            ):

                return (
                    self.reasoning
                    .compare_patients(
                        question,
                        self.engine.get_patient(
                            ids[0]
                        ),
                        self.engine.get_patient(
                            ids[1]
                        )
                    )
                )

            if (
                classification.get(
                    "entity_type"
                )
                ==
                "subject"
            ):

                return (
                    self.reasoning
                    .compare_subjects(
                        question,
                        self.engine.get_subject_data(
                            ids[0]
                        ),
                        self.engine.get_subject_data(
                            ids[1]
                        )
                    )
                )

            if (
                classification.get(
                    "entity_type"
                )
                ==
                "study"
            ):

                return (
                    self.reasoning
                    .compare_studies(
                        question,
                        self.engine.get_study(
                            ids[0]
                        ),
                        self.engine.get_study(
                            ids[1]
                        )
                    )
                )

        

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

            response = (
                self.reasoning
                .reason_over_entity(
                    question,
                    context
                )
            )

            self.sessions.set_last_intent(
                session_id,
                intent
            )

            self.sessions.set_last_action(
                session_id,
                classification.get(
                    "action"
                )
            )

            self.sessions.set_last_answer(
                session_id,
                response
            )

            self.sessions.add_history(
                session_id,
                question,
                response
            )

            return response

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

            response = (
                self.reasoning
                .reason_over_entity(
                    question,
                    context
                )
            )

            self.sessions.set_last_intent(
                session_id,
                intent
            )

            self.sessions.set_last_action(
                session_id,
                classification.get(
                    "action"
                )
            )

            self.sessions.set_last_answer(
                session_id,
                response
            )

            self.sessions.add_history(
                session_id,
                question,
                response
            )

            return response

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

            if classification.get("metric") == "enrollment":

                protocol = (
                    study_data
                    .get("data", {})
                    .get("protocolSection", {})
                )

                enrollment = (
                    protocol
                    .get("designModule", {})
                    .get("enrollmentInfo", {})
                    .get("count")
                )

                return {
                    "enrollment": enrollment
                }

            context = (
                self.context_builder
                .build_study_context(
                    study_data
                )
            )

            response = (
                self.reasoning
                .reason_over_entity(
                    question,
                    context
                )
            )

            self.sessions.set_last_intent(
                session_id,
                intent
            )

            self.sessions.set_last_action(
                session_id,
                classification.get(
                    "action"
                )
            )

            self.sessions.set_last_answer(
                session_id,
                response
            )

            self.sessions.add_history(
                session_id,
                question,
                response
            )

            return response

        # -------------------------
        # ANALYTICS
        # -------------------------

        if intent == "analytics":

            return (
                self.analytics.execute(
                    classification.get(
                        "action"
                    ),
                    classification.get(
                        "metric"
                    )
                )
            )

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
        
        