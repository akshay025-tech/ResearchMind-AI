
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import search_documents
from app.services.context_builder import build_context
from app.services.llm_service import generate_answer
from app.services.citation_service import format_citations


EVALUATION_QUESTIONS = [
    {
        "question": "What are the four major layers of FinRobot?",
        "expected_keywords": [
            "Financial AI Agents",
            "Financial LLMs Algorithms",
            "Multi-Source LLM Foundation Models",
            "LLMOps"
        ]
    },
    {
        "question": (
            "What are the three components of the "
            "Financial AI Agents Layer?"
        ),
        "expected_keywords": [
            "Perception",
            "Brain",
            "Action"
        ]
    }
]


def evaluate_question(question, expected_keywords):
    query_embedding = generate_embeddings([question])[0]

    results = search_documents(
        query_embedding=query_embedding,
        top_k=5
    )

    context, sources = build_context(results)

    answer = generate_answer(
        question=question,
        context=context
    )

    answer_lower = answer.lower()

    matched_keywords = [
        keyword
        for keyword in expected_keywords
        if keyword.lower() in answer_lower
    ]

    score = len(matched_keywords) / len(expected_keywords) * 100

    citations = format_citations(sources)

    return {
        "question": question,
        "answer": answer,
        "matched_keywords": matched_keywords,
        "score": score,
        "citations": citations
    }


def main():
    print("=" * 60)
    print("RESEARCHMIND RAG EVALUATION")
    print("=" * 60)

    scores = []

    for index, test_case in enumerate(
        EVALUATION_QUESTIONS, start=1
    ):
        result = evaluate_question(
            test_case["question"],
            test_case["expected_keywords"]
        )

        scores.append(result["score"])

        print("\n" + "=" * 60)
        print(f"EVALUATION {index}")
        print("=" * 60)

        print("\nQUESTION:")
        print(result["question"])

        print("\nANSWER:")
        print(result["answer"])

        print("\nMATCHED KEYWORDS:")
        print(result["matched_keywords"])

        print(f"\nKEYWORD SCORE: {result['score']:.1f}%")

        print("\nCITATIONS:")
        for citation in result["citations"]:
            print(citation)

    average_score = sum(scores) / len(scores)

    print("\n" + "=" * 60)
    print(f"AVERAGE KEYWORD SCORE: {average_score:.1f}%")
    print("RAG EVALUATION COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
