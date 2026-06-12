import re


class NaturalLanguageRouter:

    def route(
        self,
        question: str
    ):

        q = question.lower()

        subject_match = re.search(
            r"subj-\d+",
            q
        )

        study_match = re.search(
            r"nct\d+",
            q
        )

        if subject_match:

            subject_id = (
                subject_match
                .group()
                .upper()
            )

            if "demographic" in q:

                return (
                    "subject_demographics",
                    subject_id
                )

            if "medication" in q:

                return (
                    "subject_medications",
                    subject_id
                )

            if "lab" in q:

                return (
                    "subject_labs",
                    subject_id
                )

            if (
                "adverse"
                in q
                or
                "ae"
                in q
            ):

                return (
                    "subject_ae",
                    subject_id
                )

            return (
                "subject_all",
                subject_id
            )

        if study_match:

            return (
                "study",
                study_match
                .group()
                .upper()
            )

        if (
            "average age"
            in q
        ):

            return (
                "average_age",
                None
            )

        if (
            "top diagnoses"
            in q
        ):

            return (
                "top_diagnoses",
                None
            )

        if (
            "top medications"
            in q
        ):

            return (
                "top_medications",
                None
            )

        return (
            "unknown",
            None
        )