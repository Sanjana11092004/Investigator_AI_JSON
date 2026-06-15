# test_patient_lookup.py

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

engine = JSONQueryEngine()

patient = engine.get_patient(
    "PAT-301"
)

print(patient)