from src.rag.context_builder import (
    ContextBuilder
)

from src.rag.prompt_builder import (
    PromptBuilder
)

context = (
    ContextBuilder()
    .build_subject_context(
        "SUBJ-0001"
    )
)

prompt = (
    PromptBuilder()
    .build_subject_prompt(
        context
    )
)

print(
    prompt
)