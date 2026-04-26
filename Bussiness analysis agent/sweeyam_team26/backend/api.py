from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
import io
import logging
from typing import Optional, List
import os

from workflow.orchestrator import run_workflow

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Agentic Business Surveillance API",
    description="AI-powered decision intelligence system",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# Data Models
# ============================================================

class MessageRequest(BaseModel):
    message: str
    analysis_state: Optional[dict] = None

class AnalysisResponse(BaseModel):
    status: str
    alert: dict
    analysis: dict
    alternatives: list
    decision: dict
    business_summary: str
    demand_insights: list
    inventory_alerts: list
    vendor_optimizations: list

class ChatResponse(BaseModel):
    response: str
    confidence: float = 0.85

class HealthResponse(BaseModel):
    status: str
    message: str

# ============================================================
# Helper Functions
# ============================================================

async def read_csv_file(file: UploadFile) -> pd.DataFrame:
    """Read CSV file and return DataFrame"""
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read {file.filename}: {str(e)}")

# ============================================================
# API Routes
# ============================================================

@app.get("/api/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Agentic Business Surveillance API is running"
    }

@app.post("/api/analysis/run", response_model=AnalysisResponse)
async def run_analysis(
    orders_file: UploadFile = File(...),
    reviews_file: UploadFile = File(...),
    sellers_file: UploadFile = File(...),
    inventory_file: UploadFile = File(...)
):
    """
    Run comprehensive business analysis on uploaded data
    
    Expected CSV columns:
    - Orders: order_id, customer_id, product_id, order_date, amount, status
    - Reviews: review_id, product_id, rating, review_text, review_date
    - Sellers: seller_id, seller_name, rating, price, delivery_time
    - Inventory: product_id, stock_level, reorder_level, last_updated
    """
    try:
        logger.info("Starting analysis with uploaded files")
        
        # Read all CSV files
        orders_df = await read_csv_file(orders_file)
        reviews_df = await read_csv_file(reviews_file)
        sellers_df = await read_csv_file(sellers_file)
        inventory_df = await read_csv_file(inventory_file)
        
        logger.info(f"Orders shape: {orders_df.shape}")
        logger.info(f"Reviews shape: {reviews_df.shape}")
        logger.info(f"Sellers shape: {sellers_df.shape}")
        logger.info(f"Inventory shape: {inventory_df.shape}")
        
        # Run the workflow
        analysis_result = run_workflow(orders_df, reviews_df, sellers_df, inventory_df)
        
        logger.info("Analysis completed successfully")
        
        return {
            "status": "completed",
            "alert": analysis_result.get("alert", {}),
            "analysis": analysis_result.get("analysis", {}),
            "alternatives": analysis_result.get("alternatives", []),
            "decision": analysis_result.get("decision", {}),
            "business_summary": analysis_result.get("business_summary", ""),
            "demand_insights": analysis_result.get("demand_insights", []),
            "inventory_alerts": analysis_result.get("inventory_alerts", []),
            "vendor_optimizations": analysis_result.get("vendor_optimizations", [])
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: MessageRequest):
    """
    Chat with AI business advisor about analysis results
    """
    try:
        if not request.message:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        logger.info(f"Chat message: {request.message}")
        
        # Import chat agent
        from agents.chat_agent import chat_agent
        
        # Get response from chat agent
        response = chat_agent(
            message=request.message,
            state=request.analysis_state or {}
        )
        
        # Extract response text and confidence
        if isinstance(response, dict):
            response_text = response.get("response", str(response))
            confidence = response.get("confidence", 0.85)
        else:
            response_text = str(response)
            confidence = 0.85
        
        logger.info(f"Chat response generated with confidence: {confidence}")
        
        return {
            "response": response_text,
            "confidence": confidence
        }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Chat error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")

@app.get("/api/analysis/example")
async def get_example_analysis():
    """
    Get example analysis response structure
    """
    return {
        "status": "completed",
        "alert": {
            "risk_level": "MEDIUM",
            "risks": ["Inventory below threshold", "Vendor quality issues"]
        },
        "analysis": {
            "trend": "Upward",
            "key_metrics": {"growth": "15%", "retention": "85%"}
        },
        "alternatives": [
            {"id": 1, "name": "Increase prices", "impact": "High"},
            {"id": 2, "name": "Expand inventory", "impact": "Medium"}
        ],
        "decision": {
            "recommended_action": "Increase inventory for high-demand products",
            "priority": "High"
        },
        "business_summary": "Overall business is healthy with strong growth trends",
        "demand_insights": [
            "Peak demand on weekends",
            "Product X shows 20% growth YoY"
        ],
        "inventory_alerts": [
            {"product": "Product A", "message": "Stock below reorder level"},
            {"product": "Product B", "message": "Excess inventory detected"}
        ],
        "vendor_optimizations": [
            {"vendor": "Vendor A", "recommendation": "Increase order volume for better pricing"}
        ]
    }

# ============================================================
# Exception Handlers
# ============================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

# ============================================================
# Startup/Shutdown Events
# ============================================================

@app.on_event("startup")
async def startup_event():
    logger.info("API startup")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("API shutdown")

# Run with: uvicorn api:app --reload --host 0.0.0.0 --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
