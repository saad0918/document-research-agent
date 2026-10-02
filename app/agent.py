from typing import Dict

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from app.rag import retrieve_documents
from app.config import GOOGLE_API_KEY


class DocumentResearchAgent:

    def __init__(self, vector_store):
        self.vector_store = vector_store

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-3.8-flash",
            temperature=0.2,
            google_api_key=GOOGLE_API_KEY,
        )

        @tool
        def search_documents(query: str) -> str:
            """Search the uploaded document for relevant information."""

            results = retrieve_documents(
                self.vector_store,
                query,
                k=5
            )

            results = sorted(
                results,
                key=lambda x: x["score"]
            )[:3]

            formatted = []

            for item in results:
                formatted.append(
                    f"[Page {item['page']}]\n{item['content']}"
                )

            return "\n\n---\n\n".join(formatted)

        self.search_documents = search_documents

    def answer(self, question: str) -> Dict:
        """Decide whether retrieval is needed and generate an answer."""

        decision_prompt = f"""
You are a document research agent.

User question:
{question}

Decide whether answering this question requires information
from the uploaded document.

Return exactly one word:
RETRIEVE
or
DIRECT
"""

        decision_response = self.llm.invoke(
            [
                SystemMessage(
                    content="You are a careful research agent."
                ),
                HumanMessage(
                    content=decision_prompt
                ),
            ]
        )

        decision = decision_response.text.strip().upper()

        if "RETRIEVE" in decision:

            context = self.search_documents.invoke(question)

            answer_prompt = f"""
Answer the user's question using ONLY the retrieved
document context below.

If the context does not contain enough information,
clearly say that the document does not provide enough information.

Always mention the page number(s) used.

Question:
{question}

Retrieved context:
{context}
"""

            response = self.llm.invoke(
                [
                    SystemMessage(
                        content="Answer using retrieved evidence and cite pages."
                    ),
                    HumanMessage(
                        content=answer_prompt
                    ),
                ]
            )

            return {
                "answer": response.text,
                "mode": "retrieval",
                "sources": context,
            }

        response = self.llm.invoke(
            [
                SystemMessage(
                    content="Answer the user's question directly and concisely."
                ),
                HumanMessage(
                    content=question
                ),
            ]
        )

        return {
            "answer": response.text,
            "mode": "direct",
            "sources": "",
        }