import re


class SmartSegmenter:

    def split(
        self,
        text: str
    ) -> list[str]:

        # --------------------------------
        # FORMAT 1
        # Clinical Narrative PDFs
        # --------------------------------

        if re.search(
            r"CLINICAL\s+NARRATIVE\s+NOTE\s+PT-\d+",
            text,
            re.IGNORECASE
        ):

            parts = re.split(
                r"(?=CLINICAL\s+NARRATIVE\s+NOTE\s+PT-\d+)",
                text,
                flags=re.IGNORECASE
            )

            return [

                part.strip()

                for part in parts

                if part.strip().upper().startswith(
                    "CLINICAL NARRATIVE NOTE PT-"
                )

            ]

        # --------------------------------
        # FORMAT 2
        # PAT-001 | ...
        # --------------------------------

        if re.search(
            r"PAT-\d+\s*\|",
            text
        ):

            parts = re.split(
                r"(?=PAT-\d+\s*\|)",
                text
            )

            return [

                part.strip()

                for part in parts

                if part.strip().startswith(
                    "PAT-"
                )

            ]

        # --------------------------------
        # FORMAT 3
        # Generic patient ids
        # PT-001, CASE-001 etc.
        # --------------------------------

        matches = re.findall(
            r"\b[A-Z]{2,10}-\d+\b",
            text
        )

        unique_ids = set(matches)

        if len(unique_ids) > 1:

            first_id = list(unique_ids)[0]

            parts = re.split(
                rf"(?={re.escape(first_id)})",
                text
            )

            return [

                part.strip()

                for part in parts

                if part.strip()

            ]


        # --------------------------------
        # FORMAT 3
        # MR-201 style narratives
        # --------------------------------

        if re.search(
            r"CLINICAL\s+NARRATIVE\s+NOTE\s+MR-\d+",
            text,
            re.IGNORECASE
        ):

            parts = re.split(
                r"(?=CLINICAL\s+NARRATIVE\s+NOTE\s+MR-\d+)",
                text,
                flags=re.IGNORECASE
            )

            return [

                part.strip()

                for part in parts

                if part.strip().upper().startswith(
                    "CLINICAL NARRATIVE NOTE"
                )

            ]

        # --------------------------------
        # FALLBACK
        # --------------------------------

        return [text]