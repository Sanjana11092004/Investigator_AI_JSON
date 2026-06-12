from collections import Counter

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class Aggregations:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

    def demographics_file(self):

        subject = next(
            iter(
                self.engine.index.subject_index
            )
        )

        return (
            self.engine
            .index
            .subject_index[
                subject
            ]["demographics"]
        )

    def _load_demographics(self):

        path = (
            self.demographics_file()
        )

        payload = (
            self.engine
            ._load_json(path)
        )

        return (
            payload["data"]["records"]
        )

    def total_patients(self):

        return len(
            self._load_demographics()
        )

    def average_age(self):

        records = (
            self._load_demographics()
        )

        ages = [

            r["AGE"]

            for r in records

            if r.get("AGE")

        ]

        return round(
            sum(ages) / len(ages),
            2
        )

    def gender_distribution(self):

        records = (
            self._load_demographics()
        )

        return dict(

            Counter(

                r["SEX"]

                for r in records

            )

        )

    def country_distribution(self):

        records = (
            self._load_demographics()
        )

        return dict(

            Counter(

                r["COUNTRY"]

                for r in records

            )

        )

    def diagnosis_frequency(self):

        records = (
            self._load_demographics()
        )

        return dict(

            Counter(

                r["DIAGNOSIS"]

                for r in records

                if r.get(
                    "DIAGNOSIS"
                )

            )

        )

    def top_diagnoses(
        self,
        n: int = 10
    ):

        freq = (
            self.diagnosis_frequency()
        )

        return sorted(

            freq.items(),

            key=lambda x: x[1],

            reverse=True

        )[:n]

    def medication_frequency(self):

        meds = {}

        for key, subjects in (

            self.engine
            .index
            .medication_index
            .items()

        ):

            meds[key] = len(
                subjects
            )

        return meds

    def top_medications(
        self,
        n: int = 10
    ):

        freq = (
            self.medication_frequency()
        )

        return sorted(

            freq.items(),

            key=lambda x: x[1],

            reverse=True

        )[:n]