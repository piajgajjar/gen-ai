import streamlit as st
import requests
import streamlit.components.v1 as components

# Set Streamlit page configuration
st.set_page_config(page_title="💬 Money Mentor", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton > button {
        color: white;
        background: linear-gradient(90deg, #4a90e2, #007aff);
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        cursor: pointer;
    }
    input {
        border: 1px solid #e2e8f0;
        padding: 0.75rem;
        border-radius: 8px;
    }
    h1 {
        color: #007aff;
        font-weight: bold;
    }
    h2, h3 {
        color: #4a90e2;
    }
    #wordcloud {
        height: 200px;
        overflow: hidden;
    }
    #motion-container {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 150px;
        background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.5));
        overflow: hidden;
    }
    #motion-content {
        display: flex;
        animation: scroll-left 15s linear infinite;
    }
    @keyframes scroll-left {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create motion container at the top
st.markdown(
    """
    <div id="motion-container">
        <div id="motion-content">
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Investing</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Compound Interest</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Budgeting</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Savings</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">401(k)</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Retirement</span>
            <span style="margin-right: 50px; font-weight: bold; font-size: 16px; color: #007aff;">Cryptocurrency</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("💬 Money Mentor")

# Subtitle
st.subheader("Ask me about financial terms, and I'll provide definitions, explanations, and sources!")

# Word cloud or motion area at the bottom
st.markdown(
    """
    <div id="wordcloud">
        <marquee behavior="scroll" direction="left" style="color: #4a90e2; font-weight: bold; font-size: 14px;">
            Savings | Cryptocurrency | Index Funds | Portfolio Management | Compound Interest | Retirement | Budgeting | Inflation | Investing | Financial Planning
        </marquee>
    </div>
    """,
    unsafe_allow_html=True
)

# User input
query = st.text_input("Enter a financial term:", placeholder="e.g., Compound Interest", help="Type any financial term you want to learn about.")

if st.button("Ask", help="Click to get the response"):
    if query.strip():
        with st.spinner("Thinking..."):
            try:
                response = requests.post("http://localhost:5000/chat", json={"query": query})
                data = response.json()
                
                if "error" in data:
                    st.error("❌ " + data["error"])
                else:
                    st.success("Here are your results! 🎉")
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
st.caption("🌟 Powered by OpenAI & FAISS")
