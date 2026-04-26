def analysis_agent(analysis_state):

    if not analysis_state["alert"]:
        return analysis_state

    analysis_state["analysis"] = {
        "issue": "High negative feedback compared to order volume",
        "severity": "HIGH",
        "reason": "Repeated customer dissatisfaction signals detected"
    }

    return analysis_state
