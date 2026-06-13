from src.retrieval.cohort_service import (
    CohortService
)

cohort = CohortService()

copd = cohort.diagnosis(
    "COPD"
)

print(
    "COPD:",
    len(copd)
)

females = cohort.sex(
    copd,
    "F"
)

print(
    "COPD FEMALES:",
    len(females)
)

older = cohort.age_greater_than(
    females,
    60
)

print(
    "COPD FEMALES >60:",
    len(older)
)

print(
    older
)