def demand_intelligence_agent(orders_df):
    insights = []

    demand = (
        orders_df.groupby("product")
        .size()
        .reset_index(name="orders")
    )

    for _, row in demand.iterrows():
        insights.append({
            "product": row["product"],
            "demand_type": "FAST_MOVING" if row["orders"] >= 10 else "SLOW_MOVING"
        })

    return insights
