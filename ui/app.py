import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="Live News RAG", layout="centered")

st.title("📰 Live News RAG")
st.write("Ask about today’s news and get AI-powered summaries.")

question = st.text_input(
    "Ask a question",
    placeholder="e.g. technology news today"
)

if st.button("Ask"):
    if question.strip():
        with st.spinner("Fetching live news..."):
            response = requests.post(
                API_URL,
                params={"question": question}
            )

            if response.status_code == 200:
                data = response.json()
                st.subheader("Answer")
                st.write(data["answer"])

                st.subheader("Sources")
                for src in data.get("sources", []):
                    st.write(f"• Rank {src['rank']} | Distance {src['distance']:.2f}")
            else:
                st.error("API error")
    else:
        st.warning("Please enter a question")
