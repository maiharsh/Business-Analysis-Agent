def assess_scope(orders_df, reviews_df, analysis_state):
    vendors_impacted = reviews_df[reviews_df["rating"] <= 2]["vendor_id"].nunique()
    total_vendors = reviews_df["vendor_id"].nunique()

    if vendors_impacted / total_vendors > 0.4:
        scope = "domain wide"
    else:
        scope = "localized"

    analysis_state["scope"] = scope
    analysis_state["summary"]["scope"] = scope

    return analysis_state
