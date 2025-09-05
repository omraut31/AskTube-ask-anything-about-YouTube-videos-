import os
import streamlit as st
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# ---------------------------
# Setup
# ---------------------------
load_dotenv()
DEFAULT_MODEL = "gemini-1.5-flash"

st.title("🎥 AskTube 📺 (ask anything about YouTube videos)")

# ---------------------------
# Step 1: Input YouTube link
# ---------------------------
yt_url = st.text_input("Paste YouTube URL:", value="https://www.youtube.com/watch?v=Gfr50f6ZBvo")

def get_video_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        return parsed.path[1:]
    if parsed.hostname in {"www.youtube.com", "youtube.com"}:
        return parse_qs(parsed.query).get("v", [None])[0]
    return None

video_id = get_video_id(yt_url)

# ---------------------------
# Step 2: Fetch Transcript
# ---------------------------
if st.button("📜 Fetch Transcript"):
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id, languages=["en"])
        raw_transcript = fetched.to_raw_data()
        transcript = " ".join(entry["text"] for entry in raw_transcript)

        # Save transcript in session
        st.session_state.transcript = transcript

        st.success("Transcript fetched successfully!")
        with st.expander("Show Transcript"):
            st.write(transcript)

    except TranscriptsDisabled:
        st.error("❌ No captions available for this video.")
    except NoTranscriptFound:
        st.error("❌ No transcript found in the requested language.")
    except VideoUnavailable:
        st.error("❌ The video is unavailable.")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {str(e)}")

# ---------------------------
# Step 3–5: Process & Ask
# ---------------------------
if "transcript" in st.session_state:
    transcript = st.session_state.transcript

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])

    # Embeddings + Vector Store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    # LLM
    llm = ChatGoogleGenerativeAI(model=DEFAULT_MODEL, temperature=0.2)

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer ONLY from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    st.subheader("❓ Ask a Question")
    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        docs = retriever.invoke(question)
        context = "\n\n".join([d.page_content for d in docs])

        if context.strip():
            response = llm.invoke(prompt.format(context=context, question=question))
            st.markdown("### 📌 Answer")
            st.write(response.content)

            with st.expander("🔎 Retrieved Context"):
                st.write(context)
        else:
            st.warning("No relevant transcript chunks found. Try rephrasing your question.")
