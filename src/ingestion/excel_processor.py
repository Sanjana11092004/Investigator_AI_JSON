from pathlib import Path

import pandas as pd


class ExcelProcessor:

    def read_workbook(
        self,
        file_path: str
    ) -> dict[str, pd.DataFrame]:

        workbook = pd.read_excel(
            file_path,
            sheet_name=None
        )

        cleaned = {}

        for sheet_name, df in workbook.items():

            df = df.fillna("")

            cleaned[sheet_name] = df

        return cleaned