from src.services.investigator_service import (
    InvestigatorService
)

service = (
    InvestigatorService()
)

session_id = "demo_session"

print("\nSTEP 1")
print(
    service.ask(
        "show demographics for SUBJ-0001",
        session_id
    )
)

print("\nSTEP 2")
print(
    service.ask(
        "show medications",
        session_id
    )
)

print("\nSTEP 3")
print(
    service.ask(
        "show labs",
        session_id
    )
)

print("\nSTEP 4")
print(
    service.ask(
        "show adverse events",
        session_id
    )
)