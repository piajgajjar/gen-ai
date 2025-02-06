import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="💬 Money Mentor", layout="centered")

# Apply native Streamlit styling instead of direct CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
        min-height: 100vh;
        padding: 20px;
    }

    /* Centered Content */
    .stTextInput {
        width: 60% !important;
    }

    /* Styled Button */
    .stButton > button {
        background: linear-gradient(90deg, #4a90e2, #007aff);
        color: white;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 16px;
        transition: 0.3s ease-in-out;
    }
    .stButton > button:hover {
        background: #005bb5;
        transform: scale(1.05);
    }

    /* Answer Box */
    .answer-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    /* Space Below Subtitle */
    .extra-space {
        margin-bottom: 40px;
    }

    /* Ticker Styles */
    .ticker-wrapper {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        background: #fff;
        padding: 8px 0;
        margin-bottom: 10px;
    }

    .ticker {
        display: inline-block;
        min-width: 200%;
    }

    .ticker-1 {
        animation: ticker-left 70s linear infinite;
        color: #3c19a2;
        font-weight: bold;
    }

    .ticker-2 {
        animation: ticker-right 70s linear infinite;
        color: #820b5c;
        font-weight: bold;
    }

    .ticker span {
        font-size: 16px;
        padding: 0 20px;
        font-family: 'Calibri', sans-serif;
    }

    @keyframes ticker-left {
        from { transform: translateX(-50%); }
        to { transform: translateX(0%); }
    }

    @keyframes ticker-right {
        from { transform: translateX(0%); }
        to { transform: translateX(-50%); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the tickers
st.markdown(
    """
    <div class="ticker-wrapper">
        <div class="ticker ticker-1">
            <span>Investing Strategies</span>
            <span>Retirement Planning</span>
            <span>Compound Interest</span>
            <span>Stock Market</span>
            <span>Wealth Management</span>
            <span>Cryptocurrency Basics</span>
            <span>Index Funds</span>
            <span>Mutual Funds</span>
            <span>Budgeting Tips</span>
            <span>Emergency Fund</span>
            <span>Financial Literacy</span>
            <span>Credit Card Management</span>
            <span>Inflation Protection</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("💬 Money Mentor")

# Subtitle with extra spacing
st.subheader("Ask me about financial terms, and I'll provide definitions, explanations, and sources!")
st.markdown("<div class='extra-space'></div>", unsafe_allow_html=True)  # Adds more spacing

# Centering input & button properly using Streamlit columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
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

                        # Display answer in a nicely formatted box
                        st.markdown('<div class="answer-box">', unsafe_allow_html=True)
                        
                        st.subheader("📘 Concise Definition")
                        st.write(data.get("concise_definition", "No definition found."))

                        st.subheader("🔍 Simplified Explanation")
                        st.write(data.get("simplified_explanation", "No explanation available."))

                        st.subheader("📚 Recommended Sources")
                        st.write(data.get("sources", "No sources found."))
                        
                        st.markdown("</div>", unsafe_allow_html=True)

                except requests.exceptions.RequestException as e:
                    st.error("❌ Failed to connect to backend. Make sure your API is running.")
        else:
            st.warning("⚠️ Please enter a financial term.")

st.markdown("---")
st.caption("🌟 Powered by OpenAI & FAISS")
