def build_chat_context(analysis_state):
    context = {}

    alert = analysis_state.get("alert", {})
    decision = analysis_state.get("decision", {})
    scope = analysis_state.get("scope", "unknown")

    context["entity"] = alert.get("entity_id", "Not identified")
    context["product_or_service"] = alert.get("product_or_service", "Not specified")
    context["negative_ratio"] = alert.get("evidence", {}).get("negative_ratio", "N/A")
    context["order_volume"] = alert.get("evidence", {}).get("order_volume", "N/A")
    context["return_ratio"] = alert.get("evidence", {}).get("return_ratio", "N/A")

    context["scope"] = scope
    context["recommended_action"] = decision.get(
        "recommended_action", "No action determined"
    )
    context["confidence"] = decision.get("confidence", "N/A")

    return context
