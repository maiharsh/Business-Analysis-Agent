def vendor_price_optimization_agent(orders_df, sellers_df):
    recommendations = []

    if "price" not in sellers_df.columns:
        return recommendations

    grouped = sellers_df.groupby("product")

    for product, group in grouped:
        best = group.sort_values("price").iloc[0]
        recommendations.append({
            "product": product,
            "recommended_seller": best["seller_id"],
            "price": best["price"]
        })

    return recommendations
