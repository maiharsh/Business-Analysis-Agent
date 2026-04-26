def inventory_alert_agent(orders_df, inventory_df):
    alerts = []

    order_counts = (
        orders_df.groupby("product")
        .size()
        .reset_index(name="order_count")
    )

    merged = order_counts.merge(
        inventory_df,
        on="product",
        how="left"
    )

    for _, row in merged.iterrows():
        if row["stock_left"] < row["reorder_threshold"]:
            alerts.append({
                "product": row["product"],
                "stock_left": int(row["stock_left"]),
                "risk": "OUT_OF_STOCK_SOON",
                "recommended_action": "Source alternate vendor immediately"
            })

    return alerts
