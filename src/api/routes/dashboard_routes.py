from fastapi import APIRouter

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)

router = APIRouter()

engine = JSONQueryEngine()


@router.get("/dashboard/stats")
def dashboard_stats():

    subject_count = len(
        engine.index.subject_index
    )

    study_count = len(
        engine.index.study_index
    )

    document_count = sum(

        len(files)

        for files in
        engine.index.category_index.values()

    )

    ae_count = 0
    lab_count = 0
    med_count = 0

    for subject_id in (
        engine.index.subject_index.keys()
    ):

        subject = (
            engine.get_subject_data(
                subject_id
            )
        )

        ae_count += len(
            subject.get(
                "adverse_events",
                []
            )
        )

        lab_count += len(
            subject.get(
                "labs",
                []
            )
        )

        med_count += len(
            subject.get(
                "medications",
                []
            )
        )

    return {

        "patients":
        subject_count,

        "adverse_events":
        ae_count,

        "labs":
        lab_count,

        "medications":
        med_count,

        "studies":
        study_count,

        "documents":
        document_count

    }

@router.get("/dashboard/documents")
def dashboard_documents():

    documents = []

    for category, files in (

        engine.index
        .category_index
        .items()

    ):

        for file in files:

            documents.append({

                "name":
                file.split("\\")[-1]
                .split("/")[-1],

                "category":
                category

            })

    return documents