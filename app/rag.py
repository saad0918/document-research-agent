from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def build_vector_store(pdf_path: str):
    """Load PDF, split it into chunks, create embeddings and build FAISS."""

    # 1. Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # 2. Split document into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=120,
    )
    chunks = splitter.split_documents(documents)

    # 3. Convert chunks into embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # 4. Store embeddings in FAISS
    vector_store = FAISS.from_documents(chunks, embeddings)

    return vector_store, len(chunks)


def retrieve_documents(vector_store, query: str, k: int = 5):
    """Retrieve relevant chunks for the user's question."""

    docs_with_scores = vector_store.similarity_search_with_score(
        query,
        k=k
    )

    results = []

    for doc, score in docs_with_scores:
        results.append({
            "content": doc.page_content,
            "page": doc.metadata.get("page", 0) + 1,
            "score": float(score),
        })

    return results
