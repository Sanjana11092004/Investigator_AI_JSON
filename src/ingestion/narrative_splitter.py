import re


class NarrativeSplitter:

    def split(
        self,
        text: str
    ) -> list[str]:

        # -------------------------
        # FORMAT 1:
        # CLINICAL NARRATIVE NOTE
        # PT-101, PT-102 ...
        # -------------------------

        if re.search(
            r"CLINICAL\s+NARRATIVE\s+NOTE\s+PT-\d+",
            text
        ):

            parts = re.split(
                r"(?=CLINICAL\s+NARRATIVE\s+NOTE\s+PT-\d+)",
                text
            )

            return [

                part.strip()

                for part in parts

                if part.strip().startswith(
                    "CLINICAL NARRATIVE NOTE PT-"
                )

            ]

        # -------------------------
        # FORMAT 2:
        # PAT-001 | ...
        # PAT-002 | ...
        # -------------------------

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