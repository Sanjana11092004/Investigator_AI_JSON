from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class CohortService:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

    def diagnosis(
        self,
        diagnosis: str
    ):

        return (

            self.engine
            .find_by_diagnosis(
                diagnosis
            )

        )

    def sex(
        self,
        subjects: list,
        sex: str
    ):

        sex = sex.upper()

        results = []

        for subject_id in subjects:

            data = (
                self.engine
                .get_subject_data(
                    subject_id
                )
            )

            if not data:
                continue

            demographics = (
                data.get(
                    "demographics",
                    []
                )
            )

            for record in demographics:

                if (
                    record.get(
                        "SEX"
                    )
                    ==
                    sex
                ):

                    results.append(
                        subject_id
                    )

                    break

        return results

    def age_greater_than(
        self,
        subjects: list,
        age: int
    ):

        results = []

        for subject_id in subjects:

            data = (
                self.engine
                .get_subject_data(
                    subject_id
                )
            )

            if not data:
                continue

            demographics = (
                data.get(
                    "demographics",
                    []
                )
            )

            for record in demographics:

                if (
                    record.get(
                        "AGE",
                        0
                    )
                    >
                    age
                ):

                    results.append(
                        subject_id
                    )

                    break

        return results