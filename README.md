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
  <img src="https://img.shields.io/badge/Gemini-AI-blue?style=for-the-badge&logo=google" alt="Gemini AI">
</p>

---

## 🌐 Overview

**DocuMind AI** is an AI-powered document research application that lets users upload a PDF and ask questions about its contents.

It combines **Retrieval-Augmented Generation (RAG)** with a lightweight **agentic decision workflow**. Before answering, the agent chooses whether to retrieve information from the uploaded document or answer a general question directly using Google Gemini.

The project demonstrates:
- PDF processing and text chunking
- Gemini embeddings and FAISS semantic search
- Context-grounded question answering with page references
- A retrieval-versus-direct decision workflow
- FastAPI REST endpoints and a Streamlit interface

> **Evidence and limitations:** The retrieval path instructs Gemini to say when the retrieved context is insufficient and to mention source pages. This is prompt-based behavior, not a guarantee that every answer will be correct. The current retrieval code does not apply an explicit score threshold, and answer quality should be verified with a test set.

---

## ✨ Features

### 📄 Document Processing
- PDF upload and text extraction using `PyPDFLoader`
- Text chunking with configurable chunk size and overlap
- Page metadata preservation
- FAISS vector store creation

### 🧠 RAG Pipeline
- Google Gemini embeddings (`gemini-embedding-001`)
- Semantic similarity search
- Top-K chunk retrieval
- Context-based answer generation
- Page-based source references

### 🤖 Agentic Decision Workflow
- Classifies a question into `RETRIEVE` or `DIRECT`
- Retrieves document chunks when document information is needed
- Uses Gemini directly for general questions
- Returns the selected mode and source context

### 💬 User Interface
- Streamlit PDF upload and question-answering interface
- Displays answers, retrieval mode, and source evidence (as supported by the UI implementation)

---

## 🏗️ Architecture

```text
                    Streamlit UI
                         |
                         v
                    FastAPI API
                         |
              +----------+-----------+
              |                      |
              v                      v
          PDF Upload             User Question
              |                      |
              v                      v
         PyPDFLoader              AI Agent
              |                      |
              v                +-----+-----+
         Text Chunking         |           |
              |             RETRIEVE     DIRECT
              v                |           |
       Gemini Embeddings       v           v
              |              FAISS      Gemini
              v             Search      Direct
            FAISS              |
         Vector Store           v
                         Relevant Chunks
                               |
                               v
                             Gemini
                               |
                               v
                         Final Response
```

---

## 🔄 How It Works

### 1. Upload and index a PDF
1. The FastAPI backend receives the PDF.
2. `PyPDFLoader` extracts its text and page metadata.
3. `RecursiveCharacterTextSplitter` splits the text into chunks using a chunk size of 800 characters and overlap of 120 characters.
4. `GoogleGenerativeAIEmbeddings` converts chunks into vectors.
5. FAISS stores the vectors for similarity search.

### 2. Ask a question
1. The Streamlit UI sends the question to the FastAPI backend.
2. The `DocumentResearchAgent` asks Gemini to choose `RETRIEVE` or `DIRECT`.
3. If the decision contains `RETRIEVE`, the agent calls the document-search tool.
4. The retrieval function gets up to five similar chunks and the agent keeps the three lowest-score results.
5. The retrieved text and page numbers are provided to Gemini to generate an answer.
6. If the decision is `DIRECT`, the question is sent to Gemini without document context.
7. The API returns the answer, selected mode, and sources.

**Important:** The code sorts FAISS results by ascending score. The interpretation of a score depends on the configured distance metric; the current code does not apply a fixed relevance threshold.

---

## 🔎 Retrieval and Missing Evidence

For document-based questions, the answer prompt tells Gemini to:
- Use only the retrieved document context
- State when the context does not contain enough information
- Mention the page number(s) used

This is a useful instruction, but it is not a deterministic safeguard. If retrieval returns irrelevant chunks, or the model does not follow the instruction, an unsupported answer may still occur.

### Current behavior and limitations
- Retrieval requests up to five chunks and passes up to three chunks to Gemini.
- There is no explicit score threshold in the current `rag.py` code to reject weak matches.
- The code does not independently verify that every generated claim is supported by a cited chunk.
- Missing-evidence behavior should be tested with questions whose answers are deliberately absent from the PDF.

### Recommended test cases
Use a known test PDF and record the actual output for each case.

| Test | Example question | What to check |
|---|---|---|
| Answer present | “What degree does the candidate hold?” | Answer matches the PDF and cites the correct page |
| Answer absent | “What is the candidate’s annual salary?” (when salary is not in the PDF) | System clearly says the document does not provide enough information |
| Weakly related content | Ask about a topic mentioned only indirectly | Answer does not overstate what the document says |
| General question | “What is the capital of France?” | Agent selects direct mode if its classifier determines retrieval is unnecessary |

These are proposed tests, not measured results. Fill in the observed answers and pass/fail outcomes after running them.

---

## 📊 Evaluation

Answer quality should be measured using a small, repeatable test set rather than inferred from example questions alone.

For each test case, record:
- The question
- The expected answer or expected abstention
- The actual answer
- Whether the answer is factually supported by the PDF
- Whether the cited page is correct
- Whether the system appropriately abstains when evidence is missing

Suggested metrics once tests have been run:
- **Answer correctness rate:** correct answers divided by questions with answerable questions
- **Evidence support rate:** answers whose factual claims are supported by retrieved context divided by answers evaluated
- **Citation accuracy:** answers with correct page references divided by answers that provide citations
- **Abstention success rate:** missing-answer questions correctly identified as unanswerable divided by missing-answer questions tested

> No evaluation scores are reported here because actual test results have not been provided. Add measured results only after running and documenting the tests.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI, Uvicorn, Pydantic
- **LLM:** Google Gemini via LangChain
- **RAG:** LangChain, PyPDF, `RecursiveCharacterTextSplitter`
- **Embeddings:** `gemini-embedding-001`
- **Vector search:** FAISS
- **Frontend:** Streamlit
- **Configuration:** `python-dotenv`

---

## 📂 Project Structure

```text
document-research-agent/
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── main.py
│   └── rag.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 📁 Main Components

### `app/config.py`
Loads the Gemini API key from environment configuration.

### `app/rag.py`
- Loads PDF pages with `PyPDFLoader`
- Splits text into overlapping chunks
- Generates Gemini embeddings
- Creates a FAISS vector store
- Retrieves similar chunks and returns their content, page number, and score

### `app/agent.py`
- Uses Gemini to select `RETRIEVE` or `DIRECT`
- Defines a document-search tool
- Passes retrieved context to Gemini for document-based answers
- Instructs Gemini to state when evidence is insufficient and cite page numbers
- Returns the answer, mode, and sources

### `app/main.py`
Hosts the FastAPI application and REST API endpoints for health checking, PDF upload, and question answering.

### `streamlit_app.py`
Provides the Streamlit interface and communicates with the FastAPI backend over HTTP.

---

## 🔌 API Endpoints

### `GET /`
Checks whether the backend is running.

### `POST /upload`
Uploads and processes a PDF. According to the documented implementation, the backend extracts text, chunks it, creates embeddings and a FAISS vector store, and initializes the research agent.

Example response shape:

```json
{
  "message": "PDF processed successfully",
  "filename": "resume.pdf",
  "chunks": 5
}
```

The number of chunks shown is an example, not a fixed value.

### `POST /ask`
Sends a question to the agent.

Example request:

```json
{
  "question": "What projects are mentioned in my resume?"
}
```

Example response shape:

```json
{
  "answer": "The document mentions three projects...",
  "mode": "retrieval",
  "sources": "[Page 2] ..."
}
```

The answer and source text above are illustrative examples; actual output depends on the uploaded PDF and model response.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saad0918/document-research-agent.git
cd document-research-agent
```

### 2. Create and activate a virtual environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Never commit your real API key. Use `.env.example` as a template.

### 5. Start the backend

```bash
uvicorn app.main:app --reload
```

The API runs locally at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

### 6. Start the frontend

In a second terminal, activate the virtual environment and run:

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Questions

After uploading a PDF, try questions such as:
- What projects are mentioned in my resume?
- What technologies are mentioned in the document?
- What is the candidate's educational background?
- What experience is described in the document?

For a missing-evidence test, ask a question whose answer you have confirmed is absent from the uploaded PDF. Record whether the system correctly says that the document does not provide enough information.

A general-knowledge example is “What is the capital of France?” The agent is intended to route such questions through direct mode, but verify the selected mode during testing.

---

## 👨‍💻 My Contribution

Describe only the work you personally implemented. Based on the project structure and code shared, relevant contribution areas to confirm may include:
- PDF loading and text chunking
- Gemini embeddings and FAISS retrieval
- Retrieval-versus-direct decision logic
- FastAPI endpoints
- Streamlit frontend integration

Update this section to reflect your exact contribution and any collaboration.

---

## ⚠️ Limitations

The current implementation has the following known limitations based on the code reviewed:
- Missing-evidence handling relies on an LLM prompt rather than a separate deterministic validation step.
- Retrieval has no explicit score threshold for rejecting weak matches.
- The agent does not independently check every generated claim against retrieved evidence.
- Evaluation metrics have not been supplied, so answer accuracy and abstention reliability are not yet quantified.
- Retrieval quality can vary with PDF text extraction, chunk boundaries, embeddings, and the content of the question.

These limitations can be addressed in future work through a measured evaluation set, calibrated relevance thresholds, stronger evidence validation, and additional retrieval strategies.

---

## 🚀 Future Improvements

- Build a repeatable RAG evaluation dataset
- Add and validate a relevance threshold for retrieval
- Improve missing-evidence detection and answer abstention
- Add evidence-grounding and citation checks
- Support multiple documents and persistent vector storage
- Add hybrid search, reranking, and metadata filtering
- Add conversation history and document management
- Improve deployment, monitoring, and error handling

---

## 🔐 Security

- Store API credentials in environment variables.
- Keep `.env`, virtual environments, caches, and local data out of version control.
- Do not hardcode or publish API keys.

---

## 👨‍💻 Author

**Md Saad Ali**  
Computer Science & Engineering Graduate

Interests:
- Artificial Intelligence and Machine Learning
- Large Language Models
- Retrieval-Augmented Generation
- AI Agents
- Full-Stack Development

GitHub: https://github.com/saad0918

---

<p align="center">
  Built with Python • FastAPI • LangChain • FAISS • Gemini • Streamlit
</p>
