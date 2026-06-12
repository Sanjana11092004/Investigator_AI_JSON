from src.session.session_manager import (
    SessionManager
)

manager = SessionManager()

session_id = "demo"

manager.create_session(
    session_id
)

manager.set_active_subject(
    session_id,
    "SUBJ-0001"
)

manager.set_active_study(
    session_id,
    "NCT05575635"
)

manager.set_last_query(
    session_id,
    "Show demographics"
)

print(

    manager.get(
        session_id
    )

)