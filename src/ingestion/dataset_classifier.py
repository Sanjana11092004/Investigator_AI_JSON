class DatasetClassifier:

    DOMAIN_MAP = {
        "DM": "demographics",
        "LB": "labs",
        "AE": "adverse_events",
        "CM": "medications",
        "MH": "medical_history"
    }

    @classmethod
    def classify_sheet(
        cls,
        sheet_name: str
    ) -> str:

        domain = sheet_name.split("-")[0].strip().upper()

        return cls.DOMAIN_MAP.get(
            domain,
            "custom"
        )