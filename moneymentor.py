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
    #ticker-container {
        position: relative;
        overflow: hidden;
        white-space: nowrap;
        height: 50px;
        margin: 20px 0;
    }
    #ticker-1, #ticker-2 {
        display: inline-block;
        white-space: nowrap;
        animation-timing-function: linear;
        font-size: 16px;
        animation-duration: 20s;
    }
    #ticker-1 {
        animation-name: scroll-left;
        animation-duration: 25s;
    }
    #ticker-2 {
        animation-name: scroll-right;
        animation-duration: 30s;
    }
    #ticker-1 span, #ticker-2 span {
        margin-right: 30px;
        font-weight: bold;
        color: #4a90e2;
        font-family: 'Arial', sans-serif;
        display: inline-block;
        white-space: nowrap;
    }
    #ticker-1 span:nth-child(odd), #ticker-2 span:nth-child(even) {
        color: #007aff;
    }
    @keyframes scroll-left {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    @keyframes scroll-right {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create two scrolling tickers at the top
st.markdown(
    """
    <div id="ticker-container">
        <div id="ticker-1">
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
            <span>Tax Efficiency</span>
            <span>Debt Reduction</span>
        </div>
        <div id="ticker-2">
            <span>Risk Assessment</span>
            <span>Portfolio Diversification</span>
            <span>Financial Freedom</span>
            <span>Real Estate Investments</span>
            <span>Expense Tracking</span>
            <span>Retirement Accounts</span>
            <span>Dividend Stocks</span>
            <span>Insurance Planning</span>
            <span>Long-Term Savings</span>
            <span>401(k) Management</span>
            <span>Asset Allocation</span>
            <span>Wealth Building</span>
            <span>Tax Planning</span>
            <span>Expense Optimization</span>
            <span>Financial Goals</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("💬 Money Mentor")

# Subtitle
st.subheader("Ask me about financial terms, and I'll provide definitions, explanations, and sources!")

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
