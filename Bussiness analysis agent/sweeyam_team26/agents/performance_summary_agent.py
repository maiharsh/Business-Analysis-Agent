def performance_summary_agent(analysis_state):
    context = analysis_state["context"]
    scope = analysis_state["scope"]
    alert = analysis_state.get("alert", {})
    decision = analysis_state.get("decision", {})

    if scope == "stable":
        return f"""
### 🧾 Surveillance Report

✅ **System Status: STABLE**

No significant risk patterns detected in the
**{context['service_domain']}** domain.
"""

    if scope == "localized":
        return f"""
### 🧾 Surveillance Report — Localized Risk

⚠️ Risk detected for a specific {context['entity_type']}.

- Domain: {context['service_domain']}
- Affected Entity: {alert['entity_id']}
- Service/Product: {alert['product_or_service']}
- Risk Dimensions: {", ".join(context['risk_dimensions'])}

**Recommended Action:**  
{decision['recommended_action']}
"""

    return f"""
### 🧾 Surveillance Report — Domain Risk

🚨 Multiple entities show elevated risk indicators
across the **{context['service_domain']}** domain.

**Recommended Action:**  
{decision['recommended_action']}
"""
