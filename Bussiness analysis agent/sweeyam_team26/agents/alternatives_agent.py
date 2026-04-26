def alternatives_agent(analysis_state, vendors_df):
    """
    Suggest alternative vendors without disturbing existing workflow.
    """

    alert = analysis_state.get("alert", {})
    context = analysis_state.get("context", {})

    current_vendor = alert.get("entity_id")
    domain = context.get("service_domain")

    if not current_vendor or "vendor_id" not in vendors_df.columns:
        analysis_state["alternatives"] = []
        return analysis_state

    candidates = vendors_df[
        (vendors_df["vendor_id"] != current_vendor) &
        (vendors_df["domain"] == domain)
    ]

    if candidates.empty:
        analysis_state["alternatives"] = []
        return analysis_state

    ranked = candidates.sort_values(
        by=["avg_rating", "return_rate"],
        ascending=[False, True]
    )

    analysis_state["alternatives"] = ranked.head(3).to_dict(orient="records")
    return analysis_state
