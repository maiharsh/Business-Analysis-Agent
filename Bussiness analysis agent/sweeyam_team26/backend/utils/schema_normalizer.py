def normalize_orders_schema(df):
    mapping = {
        "product": ["product", "product_name", "item", "item_name", "sku"],
        "seller_id": ["seller_id", "seller", "vendor_id"]
    }

    for canonical, variants in mapping.items():
        for col in variants:
            if col in df.columns:
                df = df.rename(columns={col: canonical})
                break

    if "product" not in df.columns:
        raise ValueError("Orders CSV must contain a product column")

    return df


def normalize_sellers_schema(df):
    mapping = {
        "seller_id": ["seller_id", "vendor_id", "seller"],
        "product": ["product", "product_name", "item"],
        "price": ["price", "unit_price", "cost"],
        "rating": ["rating", "avg_rating"]
    }

    for canonical, variants in mapping.items():
        for col in variants:
            if col in df.columns:
                df = df.rename(columns={col: canonical})
                break

    return df


def normalize_inventory_schema(df):
    mapping = {
        "product": ["product", "product_name", "item"],
        "stock_left": ["stock_left", "inventory", "quantity"],
        "reorder_threshold": ["reorder_threshold", "min_stock"]
    }

    for canonical, variants in mapping.items():
        for col in variants:
            if col in df.columns:
                df = df.rename(columns={col: canonical})
                break

    return df
