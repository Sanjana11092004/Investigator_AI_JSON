import json

from src.retrieval.cache_manager import (
    CacheManager
)

from src.retrieval.index_builder import (
    IndexBuilder
)


class JSONQueryEngine:

    def __init__(self):

        self.cache = CacheManager()

        self.index = (
            IndexBuilder()
            .build()
        )

    def _load_json(
        self,
        file_path: str
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def get_study(
        self,
        study_id: str
    ):

        cache_key = (
            f"study:{study_id}"
        )

        if self.cache.exists(
            cache_key
        ):
            return self.cache.get(
                cache_key
            )

        file_path = (
            self.index
            .study_index
            .get(study_id)
        )

        if not file_path:
            return None

        result = self._load_json(
            file_path
        )

        self.cache.set(
            cache_key,
            result
        )

        return result

    def get_patient(
        self,
        patient_id: str
    ):

        cache_key = (
            f"patient:{patient_id}"
        )

        if self.cache.exists(
            cache_key
        ):
            return self.cache.get(
                cache_key
            )

        file_path = (
            self.index
            .patient_index
            .get(patient_id)
        )

        if not file_path:
            return None

        payload = self._load_json(
            file_path
        )

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

            if (
                patient.get(
                    "patient_id"
                )
                ==
                patient_id
            ):

                self.cache.set(
                    cache_key,
                    patient
                )

                return patient

        return None

    def get_subject_data(
        self,
        subject_id: str
    ):

        cache_key = (
            f"subject:{subject_id}"
        )

        if self.cache.exists(
            cache_key
        ):
            return self.cache.get(
                cache_key
            )

        datasets = (
            self.index
            .subject_index
            .get(
                subject_id
            )
        )

        if not datasets:
            return None

        result = {}

        for category, path in (
            datasets.items()
        ):

            payload = (
                self._load_json(
                    path
                )
            )

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

            matched = []

            for record in records:

                sid = (
                    record.get(
                        "SUBJID"
                    )
                    or
                    record.get(
                        "USUBJID"
                    )
                )

                if sid == subject_id:

                    matched.append(
                        record
                    )

            result[
                category
            ] = matched

        self.cache.set(
            cache_key,
            result
        )

        return result

    def find_by_diagnosis(
        self,
        diagnosis: str
    ):

        return (
            self.index
            .diagnosis_index
            .get(
                diagnosis.lower(),
                []
            )
        )

    def find_by_medication(
        self,
        medication: str
    ):

        return (
            self.index
            .medication_index
            .get(
                medication.lower(),
                []
            )
        )

    def find_by_lab(
        self,
        lab_name: str
    ):

        return (
            self.index
            .lab_index
            .get(
                lab_name.lower(),
                []
            )
        )