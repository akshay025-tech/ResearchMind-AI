import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:1b"


def generate_answer(question: str, context: str) -> str:
    """
    Generate a grounded answer using retrieved context.
    """

    prompt = f"""
You are ResearchMind, a research assistant.

Answer the user's question using ONLY the provided context.

If the context does not contain enough information to answer,
say that the information is not available in the provided context.

Do not invent facts.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"].strip()