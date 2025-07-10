from fastapi import APIRouter, HTTPException
from models import ChatRequest, ChatResponse
from ai_service import process_chat
from config import AGENT_CONFIGS, API_KEYS
import os

router = APIRouter()

@router.get("/agents")
async def list_agents():
    """List all available agents"""
    return {
        agent: {"description": config["description"]} 
        for agent, config in AGENT_CONFIGS.items()
    }

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Route chat request to specified agent"""
    try:
        result = await process_chat(request.agent, request.prompt, request.model)
        
        return ChatResponse(
            agent=request.agent,
            response=result["response"],
            model=request.model,
            tokens_used=result["tokens_used"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api-keys/{provider}")
async def set_api_key(provider: str, api_key: str):
    """Set API key for a provider"""
    API_KEYS[provider] = api_key
    os.environ[f"{provider.upper()}_API_KEY"] = api_key
    return {"message": f"API key set for {provider}"}

@router.get("/health")
async def health_check():
    """Health check"""
    return {"status": "healthy", "agents": len(AGENT_CONFIGS)}
