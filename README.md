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
</p>

---

# 🌐 Overview

**DocuMind AI** is an AI-powered document research application that allows users to upload PDF documents and ask questions about their content.

The application combines **Retrieval-Augmented Generation (RAG)** with a lightweight **agentic decision workflow**.

Instead of retrieving document information for every question, the agent first decides whether the question requires information from the uploaded document.

Based on the decision, the system either:

- Retrieves relevant information from the uploaded document using FAISS.
- Or answers the question directly using Google Gemini.

The project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- FAISS Vector Search
- Agentic Decision Workflows
- LangChain
- FastAPI REST APIs
- Streamlit
- PDF Document Processing
- Evidence-Based AI Responses

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

- Gemini Embeddings
- Semantic Vector Search
- FAISS Vector Database
- Relevant Chunk Retrieval
- Context-Based Answer Generation
- Page-Based Source References

## 🤖 Agentic Workflow

- AI Agent for Query Classification
- Retrieval Decision
- Direct Answer Decision
- Document Retrieval Tool
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
         Gemini Embeddings           ▼             ▼
                 │                  FAISS        Gemini
                 ▼                 Search        Direct
               FAISS                 │
           Vector Store              ▼
                              Relevant Chunks
                                     │
                                     ▼
                                  Gemini
                                     │
                                     ▼
                              Final Response
```

---

# 🔄 RAG Workflow

The application follows a Retrieval-Augmented Generation workflow:

```text
                         PDF
                          │
                          ▼
                  Text Extraction
                          │
                          ▼
                    Text Chunking
                          │
                          ▼
                  Gemini Embeddings
                          │
                          ▼
                   FAISS Vector Store
                          │
                          ▼
                    User Question
                          │
                          ▼
                     AI Agent
                          │
                  ┌───────┴───────┐
                  │               │
                  ▼               ▼
              RETRIEVE          DIRECT
                  │               │
                  ▼               ▼
             FAISS Search       Gemini
                  │               │
                  ▼               │
            Relevant Chunks       │
                  │               │
                  └───────┬───────┘
                          ▼
                        Gemini
                          │
                          ▼
                     Final Answer
```

---

# 🤖 Agentic Decision Workflow

Before answering a question, the agent determines whether information from the uploaded document is required.

```text
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
           Search FAISS           Gemini
                │                 Directly
                ▼                   │
         Relevant Chunks            │
                │                   │
                └─────────┬─────────┘
                          ▼
                     Final Answer
```

### RETRIEVE

If the question requires information from the uploaded document:

```text
User Question
      ↓
AI Agent
      ↓
RETRIEVE
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Gemini
      ↓
Answer + Page Sources
```

### DIRECT

If the question does not require information from the uploaded document:

```text
User Question
      ↓
AI Agent
      ↓
DIRECT
      ↓
Gemini
      ↓
Direct Answer
```

---

# 🔎 Retrieval Process

The retrieval process works as follows:

```text
User Question
      ↓
Query Embedding
      ↓
FAISS Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
Score-Based Relevance Filtering
      ↓
Relevant Context
      ↓
Gemini
      ↓
Final Answer
```

The application currently uses **FAISS similarity retrieval followed by score-based relevance filtering**.

Advanced reranking techniques such as cross-encoder reranking can be added in future versions.

---

# 🧠 Embeddings

DocuMind AI uses **Google Gemini Embeddings** to convert text chunks into numerical vector representations.

### Embedding Model

```text
gemini-embedding-001
```

The generated vectors are stored inside the **FAISS vector store**.

When a user asks a question, the query is also converted into a vector representation and compared against the stored document vectors.

This allows the system to retrieve semantically relevant information instead of relying only on exact keyword matching.

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Backend

- FastAPI
- Uvicorn
- Pydantic

## AI / LLM

- Google Gemini
- LangChain
- LangChain Google GenAI

## RAG

- Retrieval-Augmented Generation
- Gemini Embeddings
- FAISS
- PyPDF
- Recursive Character Text Splitter

## Embeddings

- Google Gemini Embeddings
- `gemini-embedding-001`

## Frontend

- Streamlit

## Environment & Tools

- Python Virtual Environment
- python-dotenv
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
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
```

---

# 📁 Application Components

## `app/config.py`

Handles environment configuration and loads the Gemini API key from the `.env` file.

```python
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```

---

## `app/rag.py`

Responsible for the RAG pipeline:

- PDF loading
- Text extraction
- Text chunking
- Chunk overlap
- Gemini embedding generation
- FAISS vector store creation
- Document retrieval
- Similarity score calculation

---

## `app/agent.py`

Contains the document research agent.

The agent:

- Receives the user's question
- Decides between `RETRIEVE` and `DIRECT`
- Uses the document retrieval tool when required
- Retrieves relevant document chunks
- Sends retrieved context to Gemini
- Generates the final answer
- Returns document source information

---

## `app/main.py`

Contains the FastAPI application and REST API endpoints.

Available endpoints:

```text
GET  /
POST /upload
POST /ask
```

The backend handles:

- PDF uploads
- Document processing
- Vector store creation
- Question answering
- Agent execution

---

## `streamlit_app.py`

Provides the frontend interface for:

- Uploading PDFs
- Processing documents
- Asking questions
- Viewing AI responses
- Viewing retrieved evidence
- Displaying retrieval/direct mode

The Streamlit frontend communicates with the FastAPI backend using HTTP requests.

---

# 🔌 API Endpoints

## Health Check

### `GET /`

Checks whether the FastAPI backend is running.

### Response

```json
{
  "message": "Document Research Agent API is running"
}
```

---

# 📤 Upload PDF

### `POST /upload`

Uploads and processes a PDF document.

The backend:

1. Receives the PDF.
2. Extracts text using PyPDFLoader.
3. Splits the text into chunks.
4. Generates Gemini embeddings.
5. Creates a FAISS vector store.
6. Initializes the document research agent.

### Example Response

```json
{
  "message": "PDF processed successfully",
  "filename": "resume.pdf",
  "chunks": 5
}
```

---

# 💬 Ask Question

### `POST /ask`

Sends a question to the document research agent.

### Request

```json
{
  "question": "What projects are mentioned in my resume?"
}
```

### Response

The response contains:

- AI-generated answer
- Processing mode
- Retrieved document sources

Example:

```json
{
  "answer": "The document mentions three projects...",
  "mode": "retrieval",
  "sources": "[Page 2] ..."
}
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/saad0918/document-research-agent.git
cd document-research-agent
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

The `.env` file should never be committed to GitHub.

A sample configuration is provided in:

```text
.env.example
```

---

# ▶️ Run the Application

## Start FastAPI Backend

Open a terminal and run:

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

Open another terminal.

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
streamlit run streamlit_app.py
```

The Streamlit application will open in your browser.

---

# 🔄 Complete Application Flow

The complete flow of the application is:

```text
                     User
                      │
                      ▼
                Streamlit UI
                      │
                      ▼
                 FastAPI API
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
      Upload PDF             Ask Question
          │                       │
          ▼                       ▼
    PyPDFLoader              AI Agent
          │                       │
          ▼                ┌──────┴──────┐
    Text Chunking          │             │
          │             RETRIEVE       DIRECT
          ▼                │             │
 Gemini Embeddings         ▼             ▼
          │              FAISS        Gemini
          ▼              Search        Direct
      FAISS                 │             │
  Vector Store              ▼             │
                     Relevant Chunks      │
                            │             │
                            ▼             │
                          Gemini ◄────────┘
                            │
                            ▼
                      Final Response
                            │
                            ▼
                          User
```

---

# 🧪 Example Questions

After uploading a PDF, users can ask questions such as:

```text
What projects are mentioned in my resume?
```

```text
What technologies were used in the projects?
```

```text
What is the candidate's educational background?
```

```text
What experience is mentioned in the document?
```

General questions can also be asked:

```text
What is the capital of France?
```

The agent decides whether document retrieval is required.

---

# 📊 Example Processing

## Document Question

### User

```text
What projects are mentioned in my resume?
```

```text
        ↓
        
Agent Decision

        ↓

RETRIEVE

        ↓

FAISS Similarity Search

        ↓

Relevant Resume Chunks

        ↓

Gemini

        ↓

Answer + Page Sources
```

---

## General Question

### User

```text
What is the capital of France?
```

```text
        ↓

Agent Decision

        ↓

DIRECT

        ↓

Gemini

        ↓

Direct Answer
```

---

# 🧩 Why RAG?

Large Language Models may not have access to the user's private documents.

RAG allows the application to:

1. Retrieve relevant information from the uploaded document.
2. Provide that information as context to the LLM.
3. Generate an answer based on the retrieved evidence.

This helps the system answer questions using the content of the uploaded document rather than relying only on the model's general knowledge.

---

# 🤖 Why Agentic Workflow?

A traditional RAG system can retrieve documents for every question.

DocuMind AI introduces a decision step before retrieval.

```text
Question
   ↓
Agent
   ↓
Does the document contain the required information?
   │
   ├── YES → RETRIEVE → FAISS → Gemini
   │
   └── NO  → DIRECT → Gemini
```

This creates a lightweight agentic workflow where the system chooses between two possible paths.

---

# 🔒 Security

The application uses environment variables for API credentials.

Sensitive files are excluded using `.gitignore`.

```text
.env
venv/
__pycache__/
*.pyc
.faiss/
data/
.streamlit/
```

API keys should never be hardcoded or pushed to a public repository.

---

# 🚀 Future Improvements

- Multi-document support
- Persistent vector database
- Conversation history
- User authentication
- Advanced reranking
- Hybrid search
- Metadata filtering
- Query rewriting
- Multi-query retrieval
- Streaming AI responses
- Document management
- Advanced RAG evaluation
- Production-grade agent workflows
- Cloud deployment improvements

---

# 🎯 Project Highlights

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Gemini Embeddings
- Semantic Search
- FAISS Vector Database
- LLM Integration
- Agentic Decision Workflows
- LangChain
- FastAPI REST APIs
- Streamlit UI
- PDF Document Processing
- Source-Based AI Responses
- Vector Similarity Search
- AI-Powered Document Research

---

# 📚 Key Concepts Demonstrated

### RAG

Retrieval-Augmented Generation combines document retrieval with LLM-based answer generation.

### Embeddings

Embeddings convert text into numerical vectors that capture semantic meaning.

### Vector Search

Vector search finds text chunks that are semantically similar to a user's query.

### FAISS

FAISS is used to efficiently store and search vector embeddings.

### Agent

The agent decides whether the question should use document retrieval or a direct LLM response.

### LangChain

LangChain provides orchestration components such as tools, document processing, retrieval, and LLM integration.

### FastAPI

FastAPI provides the REST API layer between the frontend and the AI backend.

### Streamlit

Streamlit provides the interactive user interface.

---

# 👨‍💻 Author

## Md Saad Ali

Computer Science & Engineering Graduate

Interested in:

- Artificial Intelligence
- Machine Learning
- Large Language Models
- Retrieval-Augmented Generation
- Full-Stack Development

### GitHub

https://github.com/saad0918

---

<p align="center">
  Built with Python • FastAPI • LangChain • FAISS • Gemini • Streamlit
</p>
