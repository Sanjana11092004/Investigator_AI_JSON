from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

engine = (
    JSONQueryEngine()
)

print(
    "\n===== STUDY ====="
)

study = engine.get_study(
    "NCT05575635"
)

print(
    study["metadata"][
        "study_id"
    ]
)

print(
    "\n===== PATIENT ====="
)

patient = engine.get_patient(
    "PAT-1"
)

print(
    patient["patient_id"]
)

print(
    patient["diagnoses"]
)

print(
    "\n===== SUBJECT ====="
)

subject = (
    engine.get_subject_data(
        "SUBJ-0001"
    )
)

print(
    subject.keys()
)

print(
    "\n===== DIAGNOSIS ====="
)

print(
    engine.find_by_diagnosis(
        "COPD"
    )
)