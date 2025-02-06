import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="💬 Money Mentor", layout="centered")

# Custom CSS for styling and seamless infinite ticker animation
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 100vh;
        padding: 0;
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
        margin-top: 20px;
    }
    h2, h3 {
        color: #4a90e2;
    }

    /* Ticker Styles */
    .ticker-wrapper {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        background: #fff;
        padding: 8px 0;
    }

    .ticker {
        display: inline-flex;
        flex-wrap: nowrap;
        animation: ticker-animation 10s linear infinite;
    }

    .ticker span {
        font-size: 16px;
        padding: 0 20px;
        font-weight: bold;
        font-family: 'Calibri', sans-serif;
    }

    /* Animation for seamless scrolling */
    @keyframes ticker-animation {
        from { transform: translateX(0%); }
        to { transform: translateX(-100%); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render two tickers with duplicated content for seamless scrolling
st.markdown(
    """
    <div class="ticker-wrapper">
        <div class="ticker">
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
            <!-- Duplicate content -->
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
        <div class="ticker">
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
            <!-- Duplicate content -->
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
