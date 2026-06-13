from src.services.investigator_service import (
    InvestigatorService
)

svc = InvestigatorService()

print(
    svc.ask(
        "Tell me a joke"
    )
)