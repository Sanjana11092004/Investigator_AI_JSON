from src.retrieval.aggregations import (
    Aggregations
)


class AnalyticsService:

    def __init__(self):

        self.agg = (
            Aggregations()
        )

    def summary(self):

        return {

            "total_patients":
                self.agg.total_patients(),

            "average_age":
                self.agg.average_age(),

            "top_diagnoses":
                self.agg.top_diagnoses(),

            "top_medications":
                self.agg.top_medications()
        }