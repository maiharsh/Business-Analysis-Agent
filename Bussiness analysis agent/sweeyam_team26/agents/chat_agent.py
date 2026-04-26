def chat_agent(user_message, state):
    """
    Conversational Decision Analyst.
    Responds in business language using Observation → Impact → Recommendation.
    """

    msg = user_message.lower()

    # ---------------- Inventory ----------------
    if any(k in msg for k in ["stock", "inventory", "out of stock"]):
        alerts = state.get("inventory_alerts", [])

        if not alerts:
            return (
                "All monitored products currently have sufficient inventory levels. "
                "No immediate stock-related action is required."
            )

        responses = []
        for a in alerts:
            responses.append(
                f"{a['product']} is running low on inventory with only "
                f"{a['stock_left']} units remaining. "
                "If unaddressed, this may lead to stock-out and lost sales. "
                "I recommend sourcing inventory from an alternate vendor immediately."
            )

        return " ".join(responses)

    # ---------------- Demand ----------------
    if any(k in msg for k in ["demand", "fast", "selling", "popular"]):
        fast = [
            d["product"]
            for d in state.get("demand_insights", [])
            if d["demand_type"] == "FAST_MOVING"
        ]

        if not fast:
            return (
                "No products are currently experiencing unusually high demand. "
                "Sales velocity remains within expected limits."
            )

        return (
            f"High demand has been detected for {', '.join(fast)}. "
            "These products are selling faster than average. "
            "I recommend monitoring inventory levels closely and ensuring vendor readiness."
        )

    # ---------------- Vendor / Pricing ----------------
    if any(k in msg for k in ["vendor", "seller", "price", "cheaper"]):
        opts = state.get("vendor_optimizations", [])

        if not opts:
            return (
                "Current vendor pricing is competitive. "
                "No immediate cost optimization opportunities have been identified."
            )

        responses = []
        for v in opts:
            responses.append(
                f"For {v['product']}, {v['recommended_seller']} offers a more cost-effective option "
                "without compromising quality. Switching vendors could reduce procurement costs."
            )

        return " ".join(responses)

    # ---------------- Decision ----------------
    if any(k in msg for k in ["decision", "action", "what should i do", "recommend"]):
        return (
            state.get("business_summary")
            or "No immediate corrective action is required at this time."
        )

    # ---------------- Risk / Urgency ----------------
    if any(k in msg for k in ["risk", "urgent", "serious"]):
        if state.get("alert"):
            return (
                "The situation requires attention. "
                "Multiple risk signals indicate potential impact on operations or customer satisfaction. "
                "Timely intervention is recommended to prevent escalation."
            )
        return "No critical risks are currently affecting operations."

    # ---------------- Default ----------------
    return (
        "I can assist with:\n"
        "• Inventory risks\n"
        "• Demand trends\n"
        "• Vendor decisions\n"
        "• Recommended actions\n\n"
        "What would you like to review?"
    )
