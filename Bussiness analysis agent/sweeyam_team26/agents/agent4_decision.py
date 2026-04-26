def decision_agent(analysis_state):

    if not analysis_state["alert"]:
        analysis_state["decision"] = {
            "action": "No action required",
            "confidence": 0.9
        }
        return analysis_state

    analysis_state["decision"] = {
        "action": "Suspend seller and promote best alternative",
        "confidence": 0.92
    }

    return analysis_state
