# 🚀 DocuMind AI

<h3 align="center">AI-Powered Document Research Agent</h3>

<p align="center">
  Intelligent • Evidence-Based • Agentic RAG
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/LangChain-Orchestration-green?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-orange?style=for-the-badge" alt="FAISS">
  <img src="https://img.shields.io/badge/Gemini-AI-blue?style=for-the-badge" alt="Gemini AI">
  <img src="https://img.shields.io/badge/Hugging%20Face-Embeddings-yellow?style=for-the-badge&logo=huggingface" alt="Hugging Face">
</p>

---

# 🌐 Overview

**DocuMind AI** is an AI-powered document research application that allows users to upload PDF documents and ask questions about their content.

The application combines **Retrieval-Augmented Generation (RAG)** with a lightweight **agentic decision workflow**.

Instead of retrieving document information for every question, the agent first decides whether the question requires information from the uploaded document.

Based on the decision, the system either:

- Retrieves relevant information from the document using FAISS.
- Or answers the question directly using Google Gemini.

The project demonstrates **RAG pipelines, vector embeddings, semantic search, agentic workflows, REST APIs, FastAPI, LangChain, and AI-powered question answering**.

---

# ✨ Features

## 📄 Document Processing

- PDF Document Upload
- Automatic PDF Text Extraction
- Text Chunking
- Chunk Overlap
- Page Metadata Preservation
- Automatic Vector Store Creation

## 🧠 RAG Pipeline

- Hugging Face Sentence Transformer Embeddings
- Semantic Vector Search
- FAISS Vector Database
- Relevant Chunk Retrieval
- Context-Based Answer Generation
- Page-Based Source References

## 🤖 Agentic Workflow

- AI Agent for Query Classification
- Retrieval Decision
- Direct Answer Decision
- Retrieval Tool Integration
- Evidence-Based Responses

## 🔎 Semantic Search

- Vector Similarity Search
- Top-K Document Retrieval
- Score-Based Relevance Filtering
- Relevant Context Selection

## 💬 AI Question Answering

- Google Gemini Integration
- Document-Based Answers
- Direct General Questions
- Retrieved Evidence Display
- Source Page Information

## 🎨 User Interface

- Streamlit Web Interface
- Premium Dark UI
- PDF Upload Interface
- Document Processing Status
- AI Response Display
- Retrieved Evidence Viewer
- Retrieval / Direct Mode Indicator

---

# 🏗️ System Architecture

```text
                         Streamlit UI
                              │
                              ▼
                         FastAPI API
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
            PDF Upload                User Question
                 │                         │
                 ▼                         ▼
           PyPDFLoader                AI Agent
                 │                         │
                 ▼                  ┌──────┴──────┐
           Text Chunking             │             │
                 │                RETRIEVE      DIRECT
                 ▼                   │             │
          Hugging Face               ▼             ▼
           Embeddings            FAISS         Gemini
                 │               Search        Direct
                 ▼                   │
               FAISS                ▼
          Vector Store         Relevant Chunks
                                     │
                                     ▼
                                  Gemini
                                     │
                                     ▼
                              Final Response

🔄 RAG Workflow

The application follows a Retrieval-Augmented Generation workflow:

PDF
 │
 ▼
Text Extraction
 │
 ▼
Text Chunking
 │
 ▼
Embeddings
 │
 ▼
FAISS Vector Store
 │
 ▼
User Question
 │
 ▼
Agent Decision
 │
 ├───────────────┐
 │               │
 ▼               ▼
RETRIEVE       DIRECT
 │               │
 ▼               ▼
FAISS Search   Gemini
 │               │
 ▼               │
Relevant        │
Chunks          │
 │               │
 └───────┬───────┘
         ▼
       Gemini
         │
         ▼
    Final Answer
🤖 Agentic Decision Workflow

Before answering a question, the agent determines whether the uploaded document is required.

                 User Question
                       │
                       ▼
                 AI Agent
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
          RETRIEVE             DIRECT
             │                   │
             ▼                   ▼
        Search FAISS          Gemini
             │               directly
             ▼                   │
      Relevant Chunks            │
             │                   │
             └─────────┬─────────┘
                       ▼
                  Final Answer
Retrieval Mode

When document information is required:

Question
   ↓
FAISS Similarity Search
   ↓
Relevant Document Chunks
   ↓
Gemini
   ↓
Answer + Page Sources
Direct Mode

When document information is not required:

Question
   ↓
Gemini
   ↓
Direct Answer
🛠️ Tech Stack
Programming Language
Python
Backend
FastAPI
Uvicorn
Pydantic
AI / LLM
Google Gemini
LangChain
LangChain Google GenAI
RAG
Retrieval-Augmented Generation
Hugging Face Sentence Transformers
FAISS
PyPDF
Embeddings
sentence-transformers/all-MiniLM-L6-v2
Frontend
Streamlit
Environment & Tools
Python Virtual Environment
python-dotenv
Git
GitHub
VS Code
📂 Project Structure
document-research-agent/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── main.py
│   └── rag.py
│
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
📁 Application Components
app/config.py

Handles environment configuration and loads the Gemini API key from the .env file.

app/rag.py

Responsible for the RAG pipeline:

PDF loading
Text chunking
Embedding generation
FAISS vector store creation
Document retrieval
app/agent.py

Contains the document research agent.

The agent:

Decides between RETRIEVE and DIRECT
Uses the document retrieval tool
Sends retrieved context to Gemini
Generates the final response
Returns document source information
app/main.py

Contains the FastAPI application and REST API endpoints.

Available endpoints:

GET  /
POST /upload
POST /ask
streamlit_app.py

Provides the user interface for:

Uploading PDFs
Processing documents
Asking questions
Viewing AI responses
Viewing retrieved document evidence
🔌 API Endpoints
Health Check
GET /

Response:

{
  "message": "Document Research Agent API is running"
}
Upload PDF
POST /upload

Uploads and processes a PDF document.

Example response:

{
  "message": "PDF processed successfully",
  "filename": "resume.pdf",
  "chunks": 5
}
Ask Question
POST /ask

Request:

{
  "question": "What projects are mentioned in my resume?"
}

Response contains:

AI-generated answer
Processing mode
Retrieved document sources
⚙️ Installation
1. Clone Repository
git clone https://github.com/saad0918/document-research-agent.git
cd document-research-agent
2. Create Virtual Environment
Windows
python -m venv venv

Activate:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root.

GOOGLE_API_KEY=your_gemini_api_key_here

The .env file should never be committed to GitHub.

A sample configuration is provided in:

.env.example
▶️ Run the Application
Start FastAPI Backend

Open a terminal and run:

uvicorn app.main:app --reload

Backend:

http://127.0.0.1:8000
Start Streamlit Frontend

Open another terminal, activate the virtual environment, and run:

streamlit run streamlit_app.py

The Streamlit application will open in your browser.

🧪 Example Questions

After uploading a PDF, users can ask questions such as:

What projects are mentioned in my resume?
What technologies were used in the projects?
What is the candidate's educational background?

General questions can also be asked:

What is the capital of France?

The agent decides whether document retrieval is required.

📊 Example Processing
Document Question
User:
What projects are mentioned in my resume?

        ↓

Agent Decision:
RETRIEVE

        ↓

FAISS Similarity Search

        ↓

Relevant Resume Chunks

        ↓

Gemini

        ↓

Answer + Page Sources
General Question
User:
What is the capital of France?

        ↓

Agent Decision:
DIRECT

        ↓

Gemini

        ↓

Direct Answer
🔒 Security

The application uses environment variables for API credentials.

Sensitive files are excluded using .gitignore.

.env
venv/
__pycache__/

API keys should never be hardcoded or pushed to a public repository.

🚀 Future Improvements
Multi-document support
Persistent vector database
Conversation history
User authentication
Advanced reranking
Hybrid search
Metadata filtering
Query rewriting
Streaming AI responses
Cloud deployment
Document management
Advanced RAG evaluation
🎯 Project Highlights

This project demonstrates practical implementation of:

Retrieval-Augmented Generation (RAG)
Vector Embeddings
Semantic Search
FAISS Vector Database
LLM Integration
Agentic Decision Workflows
LangChain
FastAPI REST APIs
Streamlit UI
PDF Document Processing
Source-Based AI Responses
👨‍💻 Author

Md Saad Ali

Computer Science & Engineering Graduate

GitHub

https://github.com/saad0918

<p align="center"> Built with Python • FastAPI • LangChain • FAISS • Hugging Face • Gemini • Streamlit </p> ```

Ye tumhare BlogAI README ke same type ka format hai — badges, overview, features, architecture, tech stack, structure, API, installation, workflow, future improvements, author etc.