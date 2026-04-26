def alternatives_agent(analysis_state, sellers_df):

    if not analysis_state["alert"]:
        return analysis_state

    flagged = analysis_state["alert"]["entity_id"]

    if "seller_id" not in sellers_df.columns:
        return analysis_state

    alternatives = sellers_df[sellers_df["seller_id"] != flagged]

    if "avg_rating" in alternatives.columns:
        alternatives = alternatives.sort_values(
            by="avg_rating", ascending=False
        )

    analysis_state["alternatives"] = alternatives.head(2).to_dict(orient="records")
    return analysis_state
