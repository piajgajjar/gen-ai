import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="💬 Money Mentor", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        min-height: 100vh;
        padding: 0 20px;
    }
    .stButton > button {
        color: white;
        background: linear-gradient(90deg, #4a90e2, #007aff);
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
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
        margin: 10px 0;
    }
    h2, h3 {
        color: #4a90e2;
        margin: 5px 0;
    }
    
    /* Spacing between subtitle and input */
    .extra-space {
        margin-bottom: 30px;
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
        animation: ticker-left 45s linear infinite;
        color: #3c19a2;
        font-weight: bold;
    }

    .ticker-2 {
        animation: ticker-right 45s linear infinite;
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
    </div>
    <div class="ticker-wrapper">
        <div class="ticker ticker-2">
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

# Subtitle with added spacing
st.subheader("Ask me about financial terms, and I'll provide definitions, explanations, and sources!")
st.markdown("<div class='extra-space'></div>", unsafe_allow_html=True)  # Adds spacing below subtitle

# Input field
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
