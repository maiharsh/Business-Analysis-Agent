def rag_intelligence_agent(orders_df, reviews_df):
    """
    Aggregates large-scale order & review data into
    compact, agent-consumable business signals.
    """

    # --- Identify entity column ---
    possible_entity_cols = [
        "seller_id",
        "restaurant_id",
        "driver_id",
        "lab_id",
        "provider_id"
    ]

    entity_col = next(
        (c for c in possible_entity_cols if c in orders_df.columns),
        None
    )

    if entity_col is None:
        raise ValueError("No valid entity identifier in orders data")

    # --- Aggregate order metrics ---
    order_metrics = orders_df.groupby(entity_col).agg(
        total_orders=("order_id", "count"),
        cancelled_orders=("is_cancelled", "sum"),
        returned_orders=("is_returned", "sum")
    )

    order_metrics["cancel_rate"] = (
        order_metrics["cancelled_orders"] / order_metrics["total_orders"]
    )

    order_metrics["return_rate"] = (
        order_metrics["returned_orders"] / order_metrics["total_orders"]
    )

    # --- Aggregate review metrics ---
    reviews_df["is_negative"] = reviews_df["rating"] <= 2

    review_metrics = reviews_df.groupby(entity_col).agg(
        total_reviews=("rating", "count"),
        negative_reviews=("is_negative", "sum")
    )

    review_metrics["bad_review_ratio"] = (
        review_metrics["negative_reviews"] / review_metrics["total_reviews"]
    )

    # --- Merge metrics ---
    intelligence = order_metrics.join(
        review_metrics, how="left"
    ).fillna(0)

    return intelligence.reset_index()
