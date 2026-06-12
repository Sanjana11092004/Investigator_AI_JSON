from src.session.session_manager import (
    SessionManager
)


class SessionService:

    def __init__(self):

        self.manager = (
            SessionManager()
        )

    def get_session(
        self,
        session_id: str
    ):

        return (
            self.manager.get(
                session_id
            )
        )