def infer_context(reviews_df, analysis_state):
    text_blob = " ".join(
        reviews_df.astype(str).values.flatten()
    ).lower()

    context = {
        "service_domain": "generic",
        "entity_type": "provider",
        "risk_dimensions": ["quality", "reliability"]
    }

    if any(k in text_blob for k in ["food", "restaurant", "delivery", "biryani"]):
        context.update({
            "service_domain": "food delivery",
            "entity_type": "restaurant",
            "risk_dimensions": ["food quality", "delivery delay", "hygiene"]
        })

    elif any(k in text_blob for k in ["driver", "ride", "cab"]):
        context.update({
            "service_domain": "transport",
            "entity_type": "driver",
            "risk_dimensions": ["safety", "behavior", "pricing"]
        })

    elif any(k in text_blob for k in ["lab", "test", "report"]):
        context.update({
            "service_domain": "healthcare",
            "entity_type": "service provider",
            "risk_dimensions": ["accuracy", "timeliness"]
        })

    analysis_state["context"] = context
    return analysis_state
