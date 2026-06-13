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

        # -------------------------
        # SUBJECT QUERIES
        # -------------------------

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
                "adverse" in q
                or
                "ae" in q
            ):

                return (
                    "subject_ae",
                    subject_id
                )

            return (
                "subject_all",
                subject_id
            )

        # -------------------------
        # STUDY QUERIES
        # -------------------------

        if study_match:

            return (
                "study",
                study_match
                .group()
                .upper()
            )

        # -------------------------
        # COHORT QUERIES
        # -------------------------

        if "copd" in q:

            return (
                "cohort_diagnosis",
                "COPD"
            )

        if "hypertension" in q:

            return (
                "cohort_diagnosis",
                "Hypertension"
            )

        if "diabetes" in q:

            return (
                "cohort_diagnosis",
                "Type 2 Diabetes"
            )

        if (
            "female" in q
            or
            "females" in q
        ):

            return (
                "cohort_female",
                None
            )

        if (
            "male" in q
            or
            "males" in q
        ):

            return (
                "cohort_male",
                None
            )

        age_match = re.search(
            r"age\s*>\s*(\d+)",
            q
        )

        if age_match:

            return (
                "cohort_age_gt",
                int(
                    age_match.group(1)
                )
            )

        # -------------------------
        # SESSION SUBJECT QUERIES
        # -------------------------

        if "demographic" in q:

            return (
                "subject_demographics",
                None
            )

        if "medication" in q:

            return (
                "subject_medications",
                None
            )

        if "lab" in q:

            return (
                "subject_labs",
                None
            )

        if (
            "adverse" in q
            or
            "ae" in q
        ):

            return (
                "subject_ae",
                None
            )

        # -------------------------
        # AGGREGATIONS
        # -------------------------

        if "average age" in q:

            return (
                "average_age",
                None
            )

        if "top diagnoses" in q:

            return (
                "top_diagnoses",
                None
            )

        if "top medications" in q:

            return (
                "top_medications",
                None
            )

        return (
            "unknown",
            None
        )