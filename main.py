# =============================================================================
# main.py - Application entry point
# =============================================================================

from fastapi import FastAPI
from api.routes import router
from config.settings import get_settings
from utils.logger import setup_logging

# Setup logging
setup_logging()

# Initialize settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title="AI Agent Router",
    version="1.0.0",
    description="Multi-agent AI routing system with LangChain integration"
)

# Include routes
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.port)