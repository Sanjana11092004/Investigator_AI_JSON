from src.retrieval.aggregations import (
    Aggregations
)

agg = Aggregations()

print(
    "\nTOTAL PATIENTS"
)

print(
    agg.total_patients()
)

print(
    "\nAVERAGE AGE"
)

print(
    agg.average_age()
)

print(
    "\nGENDER DISTRIBUTION"
)

print(
    agg.gender_distribution()
)

print(
    "\nTOP DIAGNOSES"
)

print(
    agg.top_diagnoses()
)

print(
    "\nTOP MEDICATIONS"
)

print(
    agg.top_medications()
)