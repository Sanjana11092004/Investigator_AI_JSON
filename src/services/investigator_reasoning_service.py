from collections import Counter

from src.retrieval.json_query_engine import (
    JSONQueryEngine
)


class InvestigatorReasoningService:

    def __init__(self):

        self.engine = (
            JSONQueryEngine()
        )

    def execute(
        self,
        metric: str
    ):

        metric = (
            metric or ""
        ).lower()

        if metric == "abnormal_labs":

            return (
                self.subjects_with_abnormal_labs()
            )

        if metric == "high_risk_subjects":

            return (
                self.high_risk_subjects()
            )

        if metric == "clinical_complexity":

            return (
                self.clinical_complexity_ranking()
            )

        if metric == "multiple_adverse_events":

            return (
                self.subjects_with_multiple_adverse_events()
            )

        if metric == "safety_trends":

            return (
                self.safety_trends()
            )

        return {
            "message":
            "Reasoning metric not supported."
        }

    def subjects_with_abnormal_labs(self):

        results = []

        for subject_id in (
            self.engine.index.subject_index.keys()
        ):

            subject = (
                self.engine.get_subject_data(
                    subject_id
                )
            )

            abnormal_count = 0

            for lab in subject.get(
                "labs",
                []
            ):

                if (
                    lab.get(
                        "LBNRIND"
                    )
                    !=
                    "NORMAL"
                ):

                    abnormal_count += 1

            if abnormal_count > 0:

                results.append({

                    "subject_id":
                    subject_id,

                    "abnormal_labs":
                    abnormal_count

                })

        return sorted(

            results,

            key=lambda x:
            x["abnormal_labs"],

            reverse=True

        )

    def subjects_with_multiple_adverse_events(self):

        results = []

        for subject_id in (
            self.engine.index.subject_index.keys()
        ):

            subject = (
                self.engine.get_subject_data(
                    subject_id
                )
            )

            ae_count = len(

                subject.get(
                    "adverse_events",
                    []
                )

            )

            if ae_count > 1:

                results.append({

                    "subject_id":
                    subject_id,

                    "adverse_events":
                    ae_count

                })

        return sorted(

            results,

            key=lambda x:
            x["adverse_events"],

            reverse=True

        )

    def high_risk_subjects(self):

        results = []

        for subject_id in (
            self.engine.index.subject_index.keys()
        ):

            subject = (
                self.engine.get_subject_data(
                    subject_id
                )
            )

            demographics = (
                subject.get(
                    "demographics",
                    []
                )
            )

            age = 0

            if demographics:

                age = (
                    demographics[0]
                    .get(
                        "AGE",
                        0
                    )
                )

            abnormal_labs = len([

                lab

                for lab in
                subject.get(
                    "labs",
                    []
                )

                if
                lab.get(
                    "LBNRIND"
                )
                !=
                "NORMAL"

            ])

            serious_ae = len([

                ae

                for ae in
                subject.get(
                    "adverse_events",
                    []
                )

                if
                ae.get(
                    "AESERFL"
                )
                ==
                "Y"

            ])

            medication_count = len(

                subject.get(
                    "medications",
                    []
                )

            )

            if (

                age > 75

                or

                abnormal_labs >= 2

                or

                serious_ae > 0

                or

                medication_count >= 5

            ):

                results.append({

                    "subject_id":
                    subject_id,

                    "age":
                    age,

                    "abnormal_labs":
                    abnormal_labs,

                    "serious_ae":
                    serious_ae,

                    "medications":
                    medication_count

                })

        return results

    def clinical_complexity_ranking(self):

        rankings = []

        for subject_id in (
            self.engine.index.subject_index.keys()
        ):

            subject = (
                self.engine.get_subject_data(
                    subject_id
                )
            )

            score = 0

            demographics = (
                subject.get(
                    "demographics",
                    []
                )
            )

            if demographics:

                age = (
                    demographics[0]
                    .get(
                        "AGE",
                        0
                    )
                )

                if age > 75:

                    score += 2

            score += len(

                subject.get(
                    "medical_history",
                    []
                )

            )

            score += len(

                subject.get(
                    "medications",
                    []
                )

            )

            score += len(

                subject.get(
                    "adverse_events",
                    []
                )

            )

            score += len([

                lab

                for lab in
                subject.get(
                    "labs",
                    []
                )

                if
                lab.get(
                    "LBNRIND"
                )
                !=
                "NORMAL"

            ])

            rankings.append({

                "subject_id":
                subject_id,

                "complexity_score":
                score

            })

        return sorted(

            rankings,

            key=lambda x:
            x["complexity_score"],

            reverse=True

        )

    def safety_trends(self):

        counter = Counter()

        for ae_term, subjects in (

            self.engine
            .index
            .ae_index
            .items()

        ):

            counter[ae_term] = len(
                subjects
            )

        return {

            "top_adverse_events":

            counter.most_common(10)

        }