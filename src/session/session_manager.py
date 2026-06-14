from src.session.session_store import (
    SessionStore
)


class SessionManager:

    def __init__(self):

        self.store = SessionStore()

    def create_session(
        self,
        session_id: str
    ):

        if self.store.exists(
            session_id
        ):
            return

        self.store.save_session(

            session_id,

            {
                "active_subject_id": None,
                "active_patient_id": None,
                "active_study_id": None,

                "active_cohort": [],

                "active_domain": None,

                "last_query": None,

                "last_intent": None,

                "last_action": None,

                "last_answer": None,

                "conversation_history": [],

                "last_compared_entities": []
            }

        )

    def get(
        self,
        session_id: str
    ):

        return self.store.get_session(
            session_id
        )

    def _update(
        self,
        session_id: str,
        key: str,
        value
    ):

        session = (
            self.get(
                session_id
            )
        )

        session[key] = value

        self.store.save_session(
            session_id,
            session
        )

    def set_active_subject(
        self,
        session_id: str,
        subject_id: str
    ):

        self._update(
            session_id,
            "active_subject_id",
            subject_id
        )

    def set_active_patient(
        self,
        session_id: str,
        patient_id: str
    ):

        self._update(
            session_id,
            "active_patient_id",
            patient_id
        )

    def set_active_study(
        self,
        session_id: str,
        study_id: str
    ):

        self._update(
            session_id,
            "active_study_id",
            study_id
        )

    # NEW
    def set_active_cohort(
        self,
        session_id: str,
        cohort: list
    ):

        self._update(
            session_id,
            "active_cohort",
            cohort
        )

    # NEW
    def set_active_domain(
        self,
        session_id: str,
        domain: str
    ):

        self._update(
            session_id,
            "active_domain",
            domain
        )

    def set_last_query(
        self,
        session_id: str,
        query: str
    ):

        self._update(
            session_id,
            "last_query",
            query
        )

    def set_last_intent(
        self,
        session_id: str,
        intent: str
    ):

        self._update(
            session_id,
            "last_intent",
            intent
        )


    def set_last_action(
        self,
        session_id: str,
        action: str
    ):

        self._update(
            session_id,
            "last_action",
            action
        )


    def set_last_answer(
        self,
        session_id: str,
        answer: str
    ):

        self._update(
            session_id,
            "last_answer",
            answer
        )


    def add_history(
        self,
        session_id: str,
        question: str,
        answer: str
    ):

        session = (
            self.get(
                session_id
            )
        )

        history = (
            session.get(
                "conversation_history",
                []
            )
        )

        history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        history = history[-10:]

        session[
            "conversation_history"
        ] = history

        self.store.save_session(
            session_id,
            session
        )

    def set_last_comparison(
        self,
        session_id: str,
        entities: list
    ):

        self._update(
            session_id,
            "last_compared_entities",
            entities
        )