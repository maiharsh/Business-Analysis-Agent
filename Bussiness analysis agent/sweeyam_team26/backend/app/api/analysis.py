from fastapi import APIRouter, UploadFile, File
import pandas as pd

from app.services.workflow_service import run_analysis

router = APIRouter(tags=["Analysis"])


@router.post("/analyze")
async def analyze_business(
    orders: UploadFile = File(...),
    reviews: UploadFile = File(...),
    sellers: UploadFile = File(...),
    inventory: UploadFile = File(...)
):
    orders_df = pd.read_csv(orders.file)
    reviews_df = pd.read_csv(reviews.file)
    sellers_df = pd.read_csv(sellers.file)
    inventory_df = pd.read_csv(inventory.file)

    result = run_analysis(
        orders_df,
        reviews_df,
        sellers_df,
        inventory_df
    )

    return {
        "summary": result["business_summary"],
        "alert": result["alert"],
        "decision": result["decision"],
        "demand_insights": result["demand_insights"],
        "inventory_alerts": result["inventory_alerts"],
        "vendor_optimizations": result["vendor_optimizations"],
    }
