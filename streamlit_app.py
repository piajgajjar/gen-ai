import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="💬 Finance Chatbot", layout="centered")
st.title("💬 Finance Chatbot")
st.write("Ask me any financial term, and I'll provide definitions, explanations, and sources!")

# User input
query = st.text_input("Enter a financial term:")

if st.button("Ask"):
    if query.strip():
        with st.spinner("Thinking..."):
            try:
                response = requests.post("http://localhost:5000/chat", json={"query": query})
                data = response.json()
                
                if "error" in data:
                    st.error("❌ " + data["error"])
                else:
                    st.subheader("📘 Concise Definition")
                    st.write(data.get("concise_definition", "No definition found."))
                    
                    st.subheader("🔍 Simplified Explanation")
                    st.write(data.get("simplified_explanation", "No explanation available."))
                    
                    st.subheader("📚 Recommended Sources")
                    st.write(data.get("sources", "No sources found."))
            except requests.exceptions.RequestException as e:
                st.error("❌ Failed to connect to backend. Make sure your API is running.")
    else:
        st.warning("⚠️ Please enter a financial term.")

st.markdown("---")
st.caption("Powered by OpenAI & FAISS 🚀")

