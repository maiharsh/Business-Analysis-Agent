# agents/business_analysis_agent.py

def business_analysis_agent(state: dict) -> str:
    """
    Generates a PURE TEXT executive summary.
    Absolutely no dicts, lists, or state references returned.
    """

    alert = state.get("alert", {})
    decision = state.get("decision", {})

    if not alert or not decision:
        return "No significant business risks detected. System operating normally."

    entity = alert.get("entity_id", "Unknown Entity")
    product = alert.get("product_or_service", "Unknown Product")
    confidence = decision.get("confidence", 0)

    action = decision.get("action", "No action recommended")

    summary = (
        f"Risk detected for {entity} involving {product}. "
        f"Recommended action: {action} "
        f"(confidence {int(confidence * 100)}%)."
    )

    return summary
