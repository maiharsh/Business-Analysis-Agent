from agents.agent1_surveillance import surveillance_agent
from agents.agent2_analysis import analysis_agent
from agents.agent3_alternatives import alternatives_agent
from agents.agent4_decision import decision_agent
from agents.business_analysis_agent import business_analysis_agent

from agents.demand_intelligence_agent import demand_intelligence_agent
from agents.inventory_alert_agent import inventory_alert_agent
from agents.vendor_price_optimization_agent import vendor_price_optimization_agent

from utils.schema_normalizer import (
    normalize_orders_schema,
    normalize_sellers_schema,
    normalize_inventory_schema
)


def run_workflow(orders_df, reviews_df, sellers_df, inventory_df):

    # 🔐 Normalize all schemas ONCE
    orders_df = normalize_orders_schema(orders_df)
    sellers_df = normalize_sellers_schema(sellers_df)
    inventory_df = normalize_inventory_schema(inventory_df)

    state = {
        "alert": {},
        "analysis": {},
        "alternatives": [],
        "decision": {},
        "business_summary": "",
        "demand_insights": [],
        "inventory_alerts": [],
        "vendor_optimizations": []
    }

    state = surveillance_agent(orders_df, reviews_df, state)
    state = analysis_agent(state)
    state = alternatives_agent(state, sellers_df)
    state = decision_agent(state)
    state = business_analysis_agent(state)

    state["demand_insights"] = demand_intelligence_agent(orders_df)
    state["inventory_alerts"] = inventory_alert_agent(orders_df, inventory_df)
    state["vendor_optimizations"] = vendor_price_optimization_agent(
        orders_df, sellers_df
    )

    return state
