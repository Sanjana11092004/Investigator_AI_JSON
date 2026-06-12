from src.rag.investigator_rag import (
    InvestigatorRAG
)

rag = (
    InvestigatorRAG()
)

response = (

    rag.investigate_subject(
        "SUBJ-0001"
    )

)

print(
    response
)