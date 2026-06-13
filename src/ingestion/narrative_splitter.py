import re


class NarrativeSplitter:

    def split(
        self,
        text: str
    ) -> list[str]:

        pattern = r"(?=PAT-\d+\s*\|)"

        narratives = re.split(
            pattern,
            text
        )

        cleaned = []

        for narrative in narratives:

            narrative = narrative.strip()

            if narrative.startswith("PAT-"):

                cleaned.append(
                    narrative
                )

        return cleaned