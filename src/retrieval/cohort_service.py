import json
from pathlib import Path


class CohortService:

    def __init__(self):

        self.dm_file = Path(
            "json_store/demographics/PHVIGIL2024_DM.json"
        )

        with open(
            self.dm_file,
            "r",
            encoding="utf-8"
        ) as f:

            payload = json.load(f)

        self.records = (
            payload["data"]["records"]
        )

    def diagnosis(
        self,
        diagnosis: str
    ):

        diagnosis = (
            diagnosis.lower()
        )

        return [

            r["SUBJID"]

            for r in self.records

            if diagnosis
            in str(
                r.get(
                    "DIAGNOSIS",
                    ""
                )
            ).lower()

        ]

    def sex(
        self,
        subjects: list,
        sex: str
    ):

        sex = sex.upper()

        return [

            r["SUBJID"]

            for r in self.records

            if (
                r["SUBJID"]
                in subjects
                and
                r.get(
                    "SEX"
                ) == sex
            )

        ]

    def age_greater_than(
        self,
        subjects: list,
        age: int
    ):

        return [

            r["SUBJID"]

            for r in self.records

            if (
                r["SUBJID"]
                in subjects
                and
                r.get(
                    "AGE",
                    0
                ) > age
            )

        ]