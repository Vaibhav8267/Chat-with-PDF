
import streamlit as st
from pdf_utils import extract_text_from_pdf
from text_splitter import split_text
from embedder import get_embeddings
from vector_store import store_embeddings, retrieve_similar_chunks
from chat_engine import ask_question

st.title("📄 Chat with your PDF")

pdf_file = st.file_uploader("Upload your PDF", type=["pdf"])
query = st.text_input("Ask a question about the PDF:")

if pdf_file:
    text = extract_text_from_pdf(pdf_file)
    chunks = split_text(text)
    embeddings = get_embeddings(chunks)
    store_embeddings(chunks, embeddings)

    if query:
        results = retrieve_similar_chunks(query)
        answer = ask_question(query, results)
        st.markdown("### 💬 Answer:")
        st.write(answer)
