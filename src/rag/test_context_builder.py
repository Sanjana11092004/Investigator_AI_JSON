from pprint import pprint

from src.rag.context_builder import (
    ContextBuilder
)

builder = (
    ContextBuilder()
)

context = (
    builder.build_subject_context(
        "SUBJ-0001"
    )
)

pprint(context)