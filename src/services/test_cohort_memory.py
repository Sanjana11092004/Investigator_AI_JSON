from src.services.investigator_service import (
    InvestigatorService
)

svc = InvestigatorService()

print(
    "\nSTEP 1"
)

print(
    svc.ask(
        "Show COPD patients"
    )
)

print(
    "\nSTEP 2"
)

print(
    svc.ask(
        "Show only females"
    )
)

print(
    "\nSTEP 3"
)

print(
    svc.ask(
        "Show age > 60"
    )
)