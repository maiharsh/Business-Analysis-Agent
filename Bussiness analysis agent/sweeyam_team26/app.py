import streamlit as st
import pandas as pd

from workflow.orchestrator import run_workflow
from agents.chat_agent import chat_agent

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Agentic Business Intelligence System",
    layout="wide"
)

st.title("🧠 Agentic Business Intelligence System")
st.markdown(
    "Upload operational data and interact with AI agents that act as "
    "**business decision analysts**, not dashboards."
)

st.divider()

# ============================================================
# Helper Formatters (CRITICAL FIX)
# ============================================================

def format_risk_alert(alert: dict) -> str:
    if not alert:
        return "No significant operational risks were detected."

    return (
        f"Risk detected for **{alert.get('entity_id', 'Unknown Entity')}** "
        f"involving **{alert.get('product_or_service', 'Unknown Product')}**. "
        f"Approximately **{int(alert.get('negative_ratio', 0) * 100)}%** of "
        f"{alert.get('orders_analyzed', 0)} analyzed orders show negative signals."
    )


def format_decision(decision: dict) -> str:
    if not decision:
        return "No corrective action is required at this time."

    return (
        f"**Recommended Action:** {decision.get('action', 'No action')}  \n"
        f"**Confidence Level:** {int(decision.get('confidence', 0) * 100)}%"
    )


def format_list_insights(items, title, empty_msg):
    st.subheader(title)
    if not items:
        st.info(empty_msg)
        return
    for i in items:
        line = ", ".join([f"**{k.replace('_',' ').title()}**: {v}" for k, v in i.items()])
        st.markdown(f"- {line}")


# ============================================================
# File Upload Section
# ============================================================
st.header("📂 Upload Data Sources")

col1, col2 = st.columns(2)
with col1:
    orders_file = st.file_uploader("Orders Data (orders.csv)", type=["csv"])
    inventory_file = st.file_uploader("Inventory Data (inventory.csv)", type=["csv"])

with col2:
    reviews_file = st.file_uploader("Reviews Data (reviews.csv)", type=["csv"])
    sellers_file = st.file_uploader("Sellers Data (sellers.csv)", type=["csv"])

st.divider()

# ============================================================
# Run Analysis
# ============================================================
if st.button("🚀 Run Agentic Analysis"):

    if not all([orders_file, reviews_file, sellers_file, inventory_file]):
        st.error("Please upload **all required CSV files**.")
        st.stop()

    orders_df = pd.read_csv(orders_file)
    reviews_df = pd.read_csv(reviews_file)
    sellers_df = pd.read_csv(sellers_file)
    inventory_df = pd.read_csv(inventory_file)

    with st.spinner("Running multi-agent intelligence workflow..."):
        state = run_workflow(
            orders_df,
            reviews_df,
            sellers_df,
            inventory_df
        )

    st.session_state.state = state
    st.success("Analysis completed successfully.")

# ============================================================
# Display Results (ONLY IF AVAILABLE)
# ============================================================
if "state" in st.session_state:
    state = st.session_state.state

    st.divider()
    st.header("📊 Executive Business Summary")
    st.markdown(state.get("business_summary", "No summary generated."))

    st.divider()
    st.header("⚠️ Risk Surveillance")
    st.markdown(format_risk_alert(state.get("alert", {})))

    st.divider()
    st.header("🧠 Decision Recommendation")
    st.markdown(format_decision(state.get("decision", {})))

    st.divider()
    format_list_insights(
        state.get("demand_insights", []),
        "📈 Demand Intelligence",
        "No fast or slow moving products detected."
    )

    st.divider()
    format_list_insights(
        state.get("inventory_alerts", []),
        "📦 Inventory Alerts",
        "No stock-out risks detected."
    )

    st.divider()
    format_list_insights(
        state.get("vendor_optimizations", []),
        "💰 Vendor Optimization",
        "No vendor optimization opportunities found."
    )

    # ========================================================
    # Conversational Decision Analyst (FINAL FIX)
    # ========================================================
    st.divider()
    st.header("💬 Business Decision Analyst")

    user_query = st.text_input(
        "Ask a business question (example: 'What should I do if stock runs out?')"
    )

    if user_query:
        with st.spinner("Analyzing from a business decision perspective..."):
            response = chat_agent(user_query, state)

        st.markdown(response)

    # ========================================================
    # Optional Debug (Hidden by default)
    # ========================================================
    with st.expander("🔎 View Full Agent State (Debug)"):
        st.json(state)
