import json
from pathlib import Path

from src.ingestion.dataset_classifier import (
    DatasetClassifier
)
from src.ingestion.excel_processor import (
    ExcelProcessor
)

from src.models.document_models import (
    ClinicalDocument
)

from src.storage.file_hash_store import (
    FileHashStore
)

from src.storage.json_store import (
    JSONStore
)

from src.storage.metadata_store import (
    MetadataStore
)


class StructuredConverter:

    def __init__(self):

        self.json_store = JSONStore()

        self.metadata_store = MetadataStore()

    def process_excel(
        self,
        file_path: str
    ):

        file_hash = (
            FileHashStore.calculate_hash(
                file_path
            )
        )

        if self.metadata_store.file_exists(
            file_hash
        ):

            print(
                "File already processed. Skipping."
            )

            return []

        processor = ExcelProcessor()

        workbook = (
            processor.read_workbook(
                file_path
            )
        )

        generated_files = []

        for sheet_name, dataframe in workbook.items():

            category = (
                DatasetClassifier
                .classify_sheet(
                    sheet_name
                )
            )

            records = (
                dataframe.to_dict(
                    orient="records"
                )
            )

            metadata = {
                "sheet_name": sheet_name,
                "record_count": len(records),
                "columns": list(
                    dataframe.columns
                )
            }

            if (
                len(dataframe) > 0
                and "STUDYID"
                in dataframe.columns
            ):
                metadata[
                    "study_id"
                ] = str(
                    dataframe.iloc[0][
                        "STUDYID"
                    ]
                )

            if (
                len(dataframe) > 0
                and "DOMAIN"
                in dataframe.columns
            ):
                metadata[
                    "domain"
                ] = str(
                    dataframe.iloc[0][
                        "DOMAIN"
                    ]
                )

            study_id = metadata.get(
                "study_id",
                "UNKNOWN"
            )

            domain = metadata.get(
                "domain",
                category.upper()
            )

            document = ClinicalDocument(
                file_name=f"{study_id}_{domain}",
                source_file=Path(
                    file_path
                ).name,
                source_type="xlsx",
                category=category,
                metadata=metadata,
                data={
                    "records": records
                }
            )

            output_path = (
                self.json_store
                .save_document(
                    document
                )
            )

            self.metadata_store.register_document(
                document_id=document.document_id,
                category=document.category,
                source_file=document.source_file,
                source_type=document.source_type,
                json_path=str(output_path),
                file_hash=file_hash
            )

            generated_files.append(
                output_path
            )

        return generated_files

    def process_study_json(
        self,
        file_path: str
    ):

        file_hash = (
            FileHashStore.calculate_hash(
                file_path
            )
        )

        if self.metadata_store.file_exists(
            file_hash
        ):

            print(
                "File already processed. Skipping."
            )

            return None

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            payload = json.load(f)

        study_id = (
            payload
            .get(
                "protocolSection",
                {}
            )
            .get(
                "identificationModule",
                {}
            )
            .get(
                "nctId"
            )
        )

        document = ClinicalDocument(
            file_name=study_id,
            source_file=Path(
                file_path
            ).name,
            source_type="json",
            category="studies",
            metadata={
                "study_id": study_id
            },
            data=payload
        )

        output_path = (
            self.json_store
            .save_document(
                document
            )
        )

        self.metadata_store.register_document(
            document_id=document.document_id,
            category=document.category,
            source_file=document.source_file,
            source_type=document.source_type,
            json_path=str(output_path),
            file_hash=file_hash
        )

        return output_path