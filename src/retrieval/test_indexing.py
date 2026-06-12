from src.retrieval.index_builder import (
    IndexBuilder
)

builder = IndexBuilder()

index = builder.build()

print(
    "\nStudies:",
    len(index.study_index)
)

print(
    "Patients:",
    len(index.patient_index)
)

print(
    "Subjects:",
    len(index.subject_index)
)

print(
    "Keywords:",
    len(index.keyword_index)
)

print(
    "\nExample Study:"
)

print(
    next(
        iter(
            index.study_index.items()
        )
    )
)

print(
    "\nExample Patient:"
)

print(
    next(
        iter(
            index.patient_index.items()
        )
    )
)

print(
    "\nExample Subject:"
)

print(
    next(
        iter(
            index.subject_index.items()
        )
    )
)

print(
    "\nExample Keyword:"
)

print(
    next(
        iter(
            index.keyword_index.items()
        )
    )
)