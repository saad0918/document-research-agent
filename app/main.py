import os
import tempfile

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel

from app.rag import build_vector_store
from app.agent import DocumentResearchAgent


app = FastAPI(title="Document Research Agent")

agent = None


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Document Research Agent API is running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global agent

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    contents = await file.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:
        temp.write(contents)
        pdf_path = temp.name

    try:
        vector_store, chunk_count = build_vector_store(pdf_path)

        agent = DocumentResearchAgent(vector_store)

        return {
            "message": "PDF processed successfully",
            "filename": file.filename,
            "chunks": chunk_count
        }

    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)


@app.post("/ask")
def ask_question(request: QuestionRequest):

    if agent is None:
        raise HTTPException(
            status_code=400,
            detail="Upload a PDF before asking questions."
        )

    return agent.answer(request.question)
