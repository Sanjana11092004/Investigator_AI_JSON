from src.rag.context_builder import (
    ContextBuilder
)

from src.rag.prompt_builder import (
    PromptBuilder
)

from src.llm.groq_service import (
    GroqService
)


class InvestigatorRAG:

    def __init__(self):

        self.context_builder = (
            ContextBuilder()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

        self.llm = (
            GroqService()
        )

    def investigate_subject(
        self,
        subject_id: str
    ):

        context = (

            self.context_builder
            .build_subject_context(
                subject_id
            )

        )

        prompt = (

            self.prompt_builder
            .build_subject_prompt(
                context
            )

        )

        assessment = (

            self.llm.generate(
                prompt
            )

        )

        return assessment