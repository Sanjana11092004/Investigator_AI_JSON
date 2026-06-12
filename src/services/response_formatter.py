class ResponseFormatter:

    def format_demographics(
        self,
        records
    ):

        if not records:
            return {}

        record = records[0]

        return {

            "subject_id":
            record.get("SUBJID"),

            "age":
            record.get("AGE"),

            "sex":
            record.get("SEX"),

            "country":
            record.get("COUNTRY"),

            "diagnosis":
            record.get("DIAGNOSIS"),

            "treatment_arm":
            record.get("ARM"),

            "bmi":
            record.get("BMI"),

            "bmi_category":
            record.get("BMICAT"),

            "smoking_status":
            record.get("SMOKESTAT"),

            "alcohol_use":
            record.get("ALCOHOLUSE")
        }

    def format_medications(
        self,
        records
    ):

        if not records:
            return {}

        subject_id = (
            records[0]
            .get("USUBJID")
        )

        ongoing = []

        all_medications = []

        for record in records:

            medication = (
                record.get(
                    "CMTRT"
                )
            )

            if medication:

                all_medications.append(
                    medication
                )

            if (
                record.get(
                    "CMONGO"
                ) == "Y"
            ):

                ongoing.append(
                    medication
                )

        return {

            "subject_id":
            subject_id,

            "medication_count":
            len(
                all_medications
            ),

            "ongoing_medications":
            ongoing,

            "all_medications":
            all_medications
        }

    def format_adverse_events(
        self,
        records
    ):

        if not records:
            return {}

        subject_id = (
            records[0]
            .get("USUBJID")
        )

        events = []

        serious_count = 0

        for record in records:

            event = (
                record.get(
                    "AETERM"
                )
            )

            if event:

                events.append(
                    event
                )

            if (
                record.get(
                    "AESERFL"
                ) == "Y"
            ):

                serious_count += 1

        return {

            "subject_id":
            subject_id,

            "event_count":
            len(events),

            "serious_events":
            serious_count,

            "events":
            events
        }

    def format_labs(
        self,
        records
    ):

        if not records:
            return {}

        summary = {}

        for record in records:

            test_name = (
                record.get(
                    "LBTESTCD"
                )
            )

            value = (
                record.get(
                    "LBSTRESN"
                )
            )

            abnormal = (
                record.get(
                    "LBNRIND"
                )
            )

            if test_name not in summary:

                summary[test_name] = {

                    "count": 0,
                    "values": [],
                    "abnormal_count": 0
                }

            summary[test_name]["count"] += 1

            summary[test_name]["values"].append(
                value
            )

            if abnormal != "NORMAL":

                summary[test_name][
                    "abnormal_count"
                ] += 1

        for test_name, data in summary.items():

            values = data["values"]

            first_value = values[0]
            last_value = values[-1]

            if last_value > first_value:

                trend = "increasing"

            elif last_value < first_value:

                trend = "decreasing"

            else:

                trend = "stable"

            if data["abnormal_count"] >= 3:

                clinical_flag = (
                    "repeated abnormal findings"
                )

            elif data["abnormal_count"] > 0:

                clinical_flag = (
                    "isolated abnormal findings"
                )

            else:

                clinical_flag = (
                    "within normal limits"
                )

            summary[test_name] = {

                "count":
                data["count"],

                "min":
                min(values),

                "max":
                max(values),

                "abnormal_count":
                data["abnormal_count"],

                "trend":
                trend,

                "clinical_flag":
                clinical_flag
            }

        return summary