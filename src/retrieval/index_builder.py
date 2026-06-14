import json
from pathlib import Path

from src.retrieval.json_index import (
    JSONIndex
)


class IndexBuilder:

    def __init__(self):

        self.index = JSONIndex()

    def build(self):

        # IMPORTANT: reset index every build
        self.index = JSONIndex()

        json_root = Path("json_store")

        for file_path in json_root.rglob("*.json"):
            self._index_file(file_path)

        # convert sets → lists ONLY AT END (safe)
        for key, value in list(self.index.diagnosis_index.items()):
            self.index.diagnosis_index[key] = list(value)

        for key, value in list(self.index.medication_index.items()):
            self.index.medication_index[key] = list(value)

        for key, value in list(self.index.lab_index.items()):
            self.index.lab_index[key] = list(value)

        return self.index

    def _index_file(
        self,
        file_path: Path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            payload = json.load(f)

        category = payload.get(
            "category"
        )

        self.index.category_index.setdefault(
            category,
            []
        ).append(
            str(file_path)
        )

        # -------------------------
        # STUDIES
        # -------------------------

        if category == "studies":

            study_id = (
                payload
                .get(
                    "metadata",
                    {}
                )
                .get(
                    "study_id"
                )
            )

            if study_id:

                self.index.study_index[
                    study_id
                ] = str(file_path)

        # -------------------------
        # PATIENT NARRATIVES
        # -------------------------

        elif category == "patients":

            patients = (
                payload
                .get(
                    "data",
                    {}
                )
                .get(
                    "patients",
                    []
                )
            )

            for patient in patients:

                patient_id = (
                    patient.get(
                        "patient_id"
                    )
                )

                if patient_id:

                    self.index.patient_index[
                        patient_id
                    ] = str(file_path)

                diagnoses = (
                    patient.get(
                        "diagnoses",
                        []
                    )
                )

                for diagnosis in diagnoses:

                    self.index.keyword_index.setdefault(
                        diagnosis.lower(),
                        []
                    ).append(
                        patient_id
                    )

                medications = (
                    patient.get(
                        "medications",
                        []
                    )
                )

                for medication in medications:

                    self.index.keyword_index.setdefault(
                        medication.lower(),
                        []
                    ).append(
                        patient_id
                    )

        # -------------------------
        # SDTM DOMAINS
        # -------------------------

        elif category in [

            "demographics",
            "labs",
            "adverse_events",
            "medications",
            "medical_history"

        ]:

            records = (
                payload
                .get(
                    "data",
                    {}
                )
                .get(
                    "records",
                    []
                )
            )

            for record in records:

                subject_id = (
                    record.get("SUBJID")
                    or
                    record.get("USUBJID")
                )

                if not subject_id:
                    continue

                subject_id = str(
                    subject_id
                ).strip()

                self.index.subject_index.setdefault(
                    subject_id,
                    {}
                )

                self.index.subject_index[
                    subject_id
                ][category] = str(
                    file_path
                )

                # ---------------------
                # DIAGNOSIS INDEX
                # ---------------------

                diagnosis = (
                    record.get(
                        "DIAGNOSIS"
                    )
                )

                if diagnosis:

                    self.index.diagnosis_index.setdefault(
                        diagnosis.lower(),
                        set()
                    ).add(
                        subject_id
                    )

                # ---------------------
                # MEDICATION INDEX
                # ---------------------

                medication = (
                    record.get(
                        "CMTRT"
                    )
                )

                if medication:

                    self.index.medication_index.setdefault(
                        medication.lower(),
                        set()
                    ).add(
                        subject_id
                    )

                # ---------------------
                # LAB TEST INDEX
                # ---------------------

                lab_name = (
                    record.get(
                        "LBTEST"
                    )
                )

                if lab_name:

                    self.index.lab_index.setdefault(
                        lab_name.lower(),
                        set()
                    ).add(
                        subject_id
                    )

                    self.index.lab_result_index.setdefault(
                        lab_name.lower(),
                        []
                    )

                    self.index.lab_result_index[
                        lab_name.lower()
                    ].append(

                        {
                            "subject_id": subject_id,

                            "value":
                            record.get(
                                "LBSTRESN"
                            ),

                            "unit":
                            record.get(
                                "LBSTRESU"
                            ),

                            "flag":
                            record.get(
                                "LBNRIND"
                            )
                        }

                    )

                # ---------------------
                # ADVERSE EVENT INDEX
                # ---------------------
                ae_term = (
                    record.get(
                        "AETERM"
                    )
                )

                if ae_term:

                    self.index.ae_index.setdefault(
                        ae_term.lower(),
                        []
                    )

                    self.index.ae_index[
                        ae_term.lower()
                    ].append(
                        subject_id
                    )