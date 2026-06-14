from src.llm.groq_service import (
    GroqService
)

from src.services.context_builder import (
    ContextBuilder
)

from src.cache.response_cache import (
    ResponseCache
)

class ResponseGenerationService:

    def __init__(self):

        self.groq = (
            GroqService()
        )

        self.context_builder = (
            ContextBuilder()
        )

        self.cache = (
            ResponseCache()
        )

    def generate_response(
        self,
        question: str,
        context
    ):

        cached = (
            self.cache.get(
                question,
                str(context)
            )
        )

        if cached:

            print(
                "CACHE HIT"
            )

            return cached

        print(
            "CACHE MISS"
        )

        prompt = f"""
    You are an expert Clinical Investigator Assistant.

    Answer ONLY using the supplied clinical context.

    Rules:

    - Never hallucinate.
    - Never invent information.
    - Never assume missing facts.
    - If information is unavailable, explicitly state that it is not available in the retrieved data.
    - Understand follow-up questions using the retrieved entity context.
    - Answer naturally and conversationally.
    - Summarize instead of dumping raw records.
    - Highlight clinically important findings first.
    - Prioritize diagnoses, medications, adverse events, laboratory abnormalities, study outcomes and safety findings.
    - For summaries provide an executive summary.
    - For comparisons clearly explain differences.
    - For analytics explain findings in plain English.
    - Do not mention JSON, retrieval systems, indexes, databases, caches or implementation details.
    
    For comparison requests:
    - Compare entities side-by-side.
    - Highlight similarities first.
    - Highlight differences second.
    - Conclude with the most clinically relevant distinction.

    Question:
    {question}

    Clinical Context:
    {context}

    Answer:
    """

        answer = (
            self.groq.generate(
                prompt
            )
        )

        self.cache.set(
            question,
            str(context),
            answer
        )

        return answer