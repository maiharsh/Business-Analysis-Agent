def surveillance_agent(orders_df, reviews_df, analysis_state):

    if "seller_id" not in orders_df.columns or "rating" not in reviews_df.columns:
        return analysis_state

    total_orders = len(orders_df)
    negative_reviews = reviews_df[reviews_df["rating"] <= 2]
    negative_ratio = len(negative_reviews) / max(total_orders, 1)

    if negative_ratio > 0.25:
        analysis_state["scope"] = "localized"
        analysis_state["alert"] = {
            "entity_id": orders_df["seller_id"].iloc[0],
            "product_or_service": (
                orders_df["product_name"].iloc[0]
                if "product_name" in orders_df.columns
                else "Order Batch"
            ),
            "negative_ratio": round(negative_ratio, 2),
            "orders_analyzed": total_orders
        }

    return analysis_state
