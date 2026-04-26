def init_analysis_state():
    return {
        "context": {
            "service_domain": "",
            "entity_type": "",
            "risk_dimensions": []
        },

        "scope": "stable",

        "alert": {
            "entity_id": "",
            "product_or_service": "",
            "evidence": {
                "negative_ratio": 0.0,
                "order_volume": 0,
                "return_ratio": 0.0
            }
        },

        "decision": {
            "recommended_action": "",
            "confidence": 0.0
        },

        "business_summary": ""
    }
