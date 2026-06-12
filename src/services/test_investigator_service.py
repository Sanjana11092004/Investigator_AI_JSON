from src.services.investigator_service import (
    InvestigatorService
)

service = (
    InvestigatorService()
)

print(
    "\nAVG AGE\n"
)

print(

    service.ask(
        "average age"
    )

)

print(
    "\nTOP DIAGNOSES\n"
)

print(

    service.ask(
        "top diagnoses"
    )

)

print(
    "\nSUBJECT\n"
)

print(

    service.ask(
        "show demographics for SUBJ-0001"
    )

)