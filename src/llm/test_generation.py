from src.llm.groq_service import (
    GroqService
)

llm = (
    GroqService()
)

response = (

    llm.generate(
        """
        Explain COPD in 3 sentences.
        """
    )

)

print(
    response
)