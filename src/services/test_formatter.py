from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

from src.services.response_formatter import (
    ResponseFormatter
)

engine = (
    JSONQueryEngine()
)

formatter = (
    ResponseFormatter()
)

subject = (
    engine.get_subject_data(
        "SUBJ-0001"
    )
)

print(
    "\nDEMOGRAPHICS\n"
)

print(

    formatter
    .format_demographics(

        subject[
            "demographics"
        ]

    )

)

print(
    "\nMEDICATIONS\n"
)

print(

    formatter
    .format_medications(

        subject[
            "medications"
        ]

    )

)

print(
    "\nADVERSE EVENTS\n"
)

print(

    formatter
    .format_adverse_events(

        subject[
            "adverse_events"
        ]

    )

)

print(
    "\nLAB SUMMARY\n"
)

print(

    formatter
    .format_labs(

        subject[
            "labs"
        ]

    )

)