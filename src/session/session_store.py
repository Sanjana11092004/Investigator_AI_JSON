import json
from pathlib import Path


class SessionStore:

    def __init__(self):

        self.session_file = Path(
            "sessions/active_sessions.json"
        )

        if not self.session_file.exists():

            self.session_file.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                self.session_file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {},
                    f,
                    indent=2
                )

        self.sessions = (
            self._load()
        )

    def _load(self):

        with open(
            self.session_file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def _save(self):

        with open(
            self.session_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.sessions,
                f,
                indent=2
            )

    def get_session(
        self,
        session_id: str
    ):

        return self.sessions.get(
            session_id
        )

    def save_session(
        self,
        session_id: str,
        data: dict
    ):

        self.sessions[
            session_id
        ] = data

        self._save()

    def exists(
        self,
        session_id: str
    ) -> bool:

        return (
            session_id
            in
            self.sessions
        )