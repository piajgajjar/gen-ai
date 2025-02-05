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
        height: 60px;
        margin: 20px 0;
        overflow: hidden;
    }
    #ticker-1, #ticker-2 {
        display: inline-block;
        animation-timing-function: linear;
        font-size: 14px;
        animation-duration: 30s;
        white-space: nowrap;
        font-family: 'Courier New', monospace;
    }
    #ticker-1 {
        animation-name: scroll-left;
        animation-duration: 40s;
    }
    #ticker-2 {
        animation-name: scroll-right;
        animation-duration: 50s;
    }
    #ticker-1 span, #ticker-2 span {
        margin-right: 20px;
        font-weight: bold;
        display: inline-block;
        white-space: nowrap;
        color: #333;
    }
    #ticker-1 span:nth-child(1), #ticker-2 span:nth-child(1) { color: #FF5733; }
    #ticker-1 span:nth-child(2), #ticker-2 span:nth-child(2) { color: #33FF57; }
    #ticker-1 span:nth-child(3), #ticker-2 span:nth-child(3) { color: #3357FF; }
    #ticker-1 span:nth-child(4), #ticker-2 span:nth-child(4) { color: #F3FF33; }
    #ticker-1 span:nth-child(5), #ticker-2 span:nth-child(5) { color: #FF33A6; }
    #ticker-1 span:nth-child(6), #ticker-2 span:nth-child(6) { color: #33FFF1; }
    #ticker-1 span:nth-child(7), #ticker-2 span:nth-child(7) { color: #FF8C33; }
    #ticker-1 span:nth-child(8), #ticker-2 span:nth-child(8) { color: #8C33FF; }
    #ticker-1 span:nth-child(9), #ticker-2 span:nth-child(9) { color: #33FF8C; }
    #ticker-1 span:nth-child(10), #ticker-2 span:nth-child(10) { color: #FF3333; }
    /* Repeat color styles to ensure all words get a unique color */
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
            <span>Risk Assessment</span>
            <span>Portfolio Diversification</span>
            <span>Real Estate Investments</span>
            <span>Expense Tracking</span>
            <span>Retirement Accounts</span>
            <span>Dividend Stocks</span>
            <span>Insurance Planning</span>
            <span>Long-Term Savings</span>
            <span>401(k) Management</span>
            <span>Asset Allocation</span>
        </div>
        <div id="ticker-2">
            <span>Wealth Building</span>
            <span>Tax Planning</span>
            <span>Expense Optimization</span>
            <span>Financial Goals</span>
            <span>Capital Gains</span>
            <span>Estate Planning</span>
            <span>Hedge Funds</span>
            <span>Social Security</span>
            <span>Financial Independence</span>
            <span>Investment Banking</span>
            <span>Corporate Bonds</span>
            <span>Day Trading</span>
            <span>Passive Income</span>
            <span>Cash Flow Management</span>
            <span>Health Savings Accounts</span>
            <span>Economic Indicators</span>
            <span>Stock Options</span>
            <span>Interest Rates</span>
            <span>Financial Planning</span>
            <span>Monetary Policy</span>
            <span>Angel Investing</span>
            <span>Private Equity</span>
            <span>Venture Capital</span>
            <span>Startup Funding</span>
            <span>Financial Risk</span>
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
