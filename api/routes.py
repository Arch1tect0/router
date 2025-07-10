# =============================================================================
# api/routes.py - API endpoints
# =============================================================================

from fastapi import APIRouter, HTTPException, Depends
from typing import Dict
from models.schemas import AgentRequest, AgentResponse, AgentInfo, HealthResponse
from services.agent_router import get_router
from config.agent_configs import AGENT_CONFIGS, get_available_agents
from config.settings import get_settings
from utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.get("/", tags=["General"])
async def root():
    """Root endpoint with basic information"""
    return {
        "message": "AI Agent Router API",
        "version": "1.0.0",
        "available_agents": list(AGENT_CONFIGS.keys()),
        "docs": "/docs"
    }

@router.get("/agents", response_model=Dict[str, AgentInfo], tags=["Agents"])
async def get_agents_info():
    """Get detailed information about all available agents"""
    agent_router = get_router()
    agent_availability = agent_router.get_available_agents()
    
    agents_info = {}
    for agent_type, config in AGENT_CONFIGS.items():
        agents_info[agent_type] = AgentInfo(
            name=agent_type,
            description=config["system_prompt"].split(".")[0],
            model=config["model"],
            temperature=config["temperature"],
            available=agent_availability[agent_type]
        )
    
    return agents_info

@router.post("/chat", response_model=AgentResponse, tags=["Chat"])
async def chat_with_agent(request: AgentRequest):
    """Main endpoint to chat with specific agents"""
    agent_router = get_router()
    
    try:
        # Process request
        result = await agent_router.process_request(
            agent_type=request.agent_type,
            prompt=request.prompt,
            context=request.context
        )
        
        return AgentResponse(
            agent_type=request.agent_type,
            response=result["response"],
            status=result["status"],
            user_id=request.user_id,
            processing_time=result["processing_time"]
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/chat/{agent_type}", response_model=AgentResponse, tags=["Chat"])
async def chat_with_specific_agent(agent_type: str, request: Dict):
    """Alternative endpoint for specific agent types"""
    agent_request = AgentRequest(
        agent_type=agent_type,
        prompt=request.get("prompt", ""),
        user_id=request.get("user_id"),
        context=request.get("context")
    )
    
    return await chat_with_agent(agent_request)

@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    settings = get_settings()
    agent_router = get_router()
    
    return HealthResponse(
        status="healthy",
        agents_loaded=len(agent_router.agents),
        api_keys_configured={
            key: value is not None
            for key, value in settings.api_keys.items()
        }
    )