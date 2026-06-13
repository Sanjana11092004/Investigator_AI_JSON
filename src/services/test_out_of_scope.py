from src.services.investigator_service import (
    InvestigatorService
)

service = InvestigatorService()

print(

    service.ask(
        "What is quantum physics?"
    )

)

print()

print(

    service.ask(
        "Write a python script"
    )

)