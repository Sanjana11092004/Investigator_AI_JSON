# src/services/analytics_service.py

from collections import Counter

from src.retrieval.aggregations import (
    Aggregations
)

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class AnalyticsService:

    def __init__(self):

        self.agg = (
            Aggregations()
        )

        self.engine = (
            JSONQueryEngine()
        )

    def execute(
        self,
        action: str,
        metric: str
    ):

        metric = (
            metric or ""
        ).lower()

        if (
            action == "count"
            and
            "participant" in metric
        ):

            return {
                "participants":
                self.agg.total_patients()
            }

        if (
            action == "count"
            and
            "female" in metric
        ):

            gender = (
                self.agg
                .gender_distribution()
            )

            return {
                "female_count":
                gender.get("F", 0)
            }

        if (
            action == "count"
            and
            "male" in metric
        ):

            gender = (
                self.agg
                .gender_distribution()
            )

            return {
                "male_count":
                gender.get("M", 0)
            }

        if (
            action == "average"
            and
            "age" in metric
        ):

            return {
                "average_age":
                self.agg.average_age()
            }

        if action in [
            "max",
            "min"
        ]:

            return (
                self._lab_stat(
                    metric,
                    action
                )
            )

        return {
            "message":
            "Analytics metric not supported."
        }

    def _lab_stat(
        self,
        lab_name: str,
        operation: str
    ):

        subject_ids = (
            self.engine
            .find_by_lab(
                lab_name
            )
        )

        values = []

        for subject_id in subject_ids:

            subject = (
                self.engine
                .get_subject_data(
                    subject_id
                )
            )

            labs = (
                subject.get(
                    "labs",
                    []
                )
            )

            for lab in labs:

                if (
                    lab.get(
                        "LBTEST",
                        ""
                    ).lower()
                    ==
                    lab_name.lower()
                ):

                    value = (
                        lab.get(
                            "LBSTRESN"
                        )
                    )

                    if value is not None:

                        values.append(
                            float(value)
                        )

        if not values:

            return {
                "message":
                f"No data found for {lab_name}"
            }

        if operation == "max":

            return {
                "lab_test":
                lab_name,

                "maximum":
                max(values)
            }

        return {
            "lab_test":
            lab_name,

            "minimum":
            min(values)
        }