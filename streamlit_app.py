import requests
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_URL = "http://127.0.0.1:8000"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       GLOBAL
    ============================== */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 5%,
                rgba(99, 102, 241, 0.10),
                transparent 25%
            ),
            radial-gradient(
                circle at 5% 85%,
                rgba(59, 130, 246, 0.06),
                transparent 25%
            ),
            #090b10;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* ==============================
       SIDEBAR
    ============================== */

    section[data-testid="stSidebar"] {
        background: #0c0f15;
        border-right: 1px solid #202531;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    /* ==============================
       TEXT
    ============================== */

    h1,
    h2,
    h3 {
        letter-spacing: -0.6px;
    }

    /* ==============================
       BUTTONS
    ============================== */

    .stButton > button {
        border-radius: 10px;
        min-height: 44px;
        border: 1px solid #303746;
        background: #171b24;
        color: #f4f6fa;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #6366f1;
        background: #1b2030;
        color: white;
    }

    /* ==============================
       FILE UPLOADER
    ============================== */

    [data-testid="stFileUploader"] {
        background: #11151d;
        border: 1px dashed #394151;
        border-radius: 16px;
        padding: 12px;
    }

    /* ==============================
       TEXT INPUT
    ============================== */

    .stTextInput input {
        background-color: #11151d !important;
        border: 1px solid #2c3341 !important;
        border-radius: 12px !important;
        color: #f5f7fb !important;
        min-height: 48px;
    }

    .stTextInput input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 1px #6366f1 !important;
    }

    /* ==============================
       EXPANDER
    ============================== */

    [data-testid="stExpander"] {
        background: #10141b;
        border: 1px solid #252c38;
        border-radius: 14px;
    }

    /* ==============================
       METRICS
    ============================== */

    [data-testid="stMetric"] {
        background: #11151d;
        border: 1px solid #252c38;
        border-radius: 14px;
        padding: 14px;
    }

    /* ==============================
       ALERTS
    ============================== */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* ==============================
       DIVIDER
    ============================== */

    hr {
        border-color: #202633;
        margin-top: 28px;
        margin-bottom: 28px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "processed" not in st.session_state:
    st.session_state.processed = False

if "filename" not in st.session_state:
    st.session_state.filename = ""

if "chunks" not in st.session_state:
    st.session_state.chunks = 0


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ✦ DocuMind AI")
    st.caption("Agentic document research")

    st.divider()

    st.markdown("**DOCUMENT**")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        help="Upload a PDF to create a searchable knowledge base.",
    )

    if uploaded_file:

        st.success(
            f"📄 {uploaded_file.name}"
        )

        file_size = round(
            uploaded_file.size / 1024,
            1,
        )

        st.caption(f"{file_size} KB")

        if st.button(
            "⚡ Process Document",
            use_container_width=True,
        ):

            with st.spinner(
                "Building document knowledge base..."
            ):

                try:

                    response = requests.post(
                        f"{API_URL}/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                "application/pdf",
                            )
                        },
                        timeout=120,
                    )

                    if response.ok:

                        data = response.json()

                        st.session_state.processed = True

                        st.session_state.filename = data[
                            "filename"
                        ]

                        st.session_state.chunks = data[
                            "chunks"
                        ]

                        st.success(
                            "Document processed successfully."
                        )

                    else:

                        st.error(
                            response.text
                        )

                except requests.exceptions.ConnectionError:

                    st.error(
                        "FastAPI backend is not running."
                    )

                except requests.exceptions.Timeout:

                    st.error(
                        "The backend took too long to respond."
                    )

    # =====================================================
    # STATUS
    # =====================================================

    st.markdown("**STATUS**")

    if st.session_state.processed:

        st.success(
            "Knowledge base ready",
            icon="✅",
        )

        st.caption(
            "Semantic search is available for this document."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Chunks",
                st.session_state.chunks,
            )

        with col2:

            st.metric(
                "Status",
                "Ready",
            )

    else:

        st.info(
            "Upload and process a PDF to begin.",
            icon="📄",
        )

    # =====================================================
    # PIPELINE
    # =====================================================

    st.markdown("**PIPELINE**")

    pipeline = [
        "PDF parsing",
        "Text chunking",
        "Embedding generation",
        "FAISS vector search",
        "Agent decision",
        "Gemini response",
    ]

    for step in pipeline:

        st.caption(
            f"●  {step}"
        )

    st.divider()

    st.caption(
        "FastAPI · LangChain · FAISS · "
        "Hugging Face · Gemini"
    )


# =========================================================
# TOP STATUS
# =========================================================

top_left, top_right = st.columns(
    [5, 1]
)

with top_left:

    st.caption(
        "✦  AI DOCUMENT RESEARCH"
    )

with top_right:

    if st.session_state.processed:

        st.success(
            "Ready",
            icon="✅",
        )

    else:

        st.info(
            "Waiting",
            icon="⏳",
        )


# =========================================================
# HERO
# =========================================================

st.title(
    "Ask your documents."
)

st.markdown(
    "### Get evidence-backed answers."
)

st.write(
    "Upload a PDF and let DocuMind AI decide when "
    "document retrieval is needed. Relevant information "
    "is found through semantic search and answered using Gemini."
)


# =========================================================
# DOCUMENT STATUS
# =========================================================

st.write("")

if not uploaded_file:

    st.info(
        "Start by uploading a PDF from the sidebar.",
        icon="📄",
    )

else:

    st.success(
        f"{uploaded_file.name} is ready to process.",
        icon="✅",
    )


# =========================================================
# FEATURES
# =========================================================

st.write("")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("### 📄")

    st.markdown(
        "**Document Intelligence**"
    )

    st.caption(
        "Convert PDF content into searchable "
        "semantic chunks automatically."
    )


with col2:

    st.markdown("### 🧠")

    st.markdown(
        "**Agentic Reasoning**"
    )

    st.caption(
        "The agent decides whether your question "
        "requires document retrieval."
    )


with col3:

    st.markdown("### 🔎")

    st.markdown(
        "**Semantic Retrieval**"
    )

    st.caption(
        "FAISS finds relevant document chunks "
        "using vector similarity."
    )


# =========================================================
# ASK SECTION
# =========================================================

st.divider()

st.subheader(
    "Ask your document"
)

st.caption(
    "Ask something about your uploaded document, "
    "or ask a general question."
)


question = st.text_input(
    "Question",
    placeholder="What projects are mentioned in my resume?",
    label_visibility="collapsed",
)


ask_clicked = st.button(
    "🚀 Ask Agent",
    use_container_width=True,
)


# =========================================================
# ASK AGENT
# =========================================================

if ask_clicked:

    if not question.strip():

        st.warning(
            "Please enter a question first.",
            icon="⚠️",
        )

    else:

        with st.spinner(
            "Agent is researching..."
        ):

            try:

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question
                    },
                    timeout=120,
                )

                if response.ok:

                    data = response.json()

                    mode = data.get(
                        "mode",
                        "unknown",
                    )

                    answer = data.get(
                        "answer",
                        "",
                    )

                    sources = data.get(
                        "sources",
                        "",
                    )

                    st.write("")

                    # =====================================
                    # MODE
                    # =====================================

                    if mode == "retrieval":

                        st.info(
                            "Retrieval Mode — "
                            "Answer generated using document evidence.",
                            icon="🔎",
                        )

                    else:

                        st.info(
                            "Direct Mode — "
                            "Answer generated without document retrieval.",
                            icon="⚡",
                        )

                    # =====================================
                    # ANSWER
                    # =====================================

                    st.subheader(
                        "AI Response"
                    )

                    with st.container(
                        border=True,
                    ):

                        st.markdown(
                            answer
                        )

                    # =====================================
                    # SOURCES
                    # =====================================

                    if sources:

                        st.write("")

                        st.subheader(
                            "Retrieved Evidence"
                        )

                        st.caption(
                            "Document context used by the agent."
                        )

                        source_blocks = sources.split(
                            "\n\n---\n\n"
                        )

                        with st.expander(
                            "View retrieved sources",
                            expanded=False,
                        ):

                            for index, block in enumerate(
                                source_blocks,
                                start=1,
                            ):

                                lines = block.split(
                                    "\n",
                                    1,
                                )

                                if len(lines) == 2:

                                    page = lines[0]
                                    content = lines[1]

                                else:

                                    page = (
                                        f"Source {index}"
                                    )

                                    content = block

                                st.markdown(
                                    f"**{page}**"
                                )

                                st.caption(
                                    content
                                )

                                if index < len(
                                    source_blocks
                                ):

                                    st.divider()

                else:

                    st.error(
                        response.text
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI backend. "
                    "Make sure uvicorn is running on port 8000."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "DocuMind AI · Agentic RAG · "
    "LangChain · FAISS · Gemini"
)