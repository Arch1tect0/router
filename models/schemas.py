# =============================================================================
# models/schemas.py - Pydantic models
# =============================================================================

from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class AgentRequest(BaseModel):
    agent_type: str = Field(..., description="Type of agent to use")
    prompt: str = Field(..., description="User prompt/query")
    user_id: Optional[str] = Field(None, description="User identifier")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    
    class Config:
        schema_extra = {
            "example": {
                "agent_type": "marketing",
                "prompt": "Create a social media campaign for a new fitness app",
                "user_id": "user123",
                "context": {"target_audience": "young adults", "budget": "low"}
            }
        }

class AgentResponse(BaseModel):
    agent_type: str
    response: str
    status: str
    user_id: Optional[str] = None
    processing_time: Optional[float] = None
    
    class Config:
        schema_extra = {
            "example": {
                "agent_type": "marketing",
                "response": "Here's your social media campaign...",
                "status": "success",
                "user_id": "user123",
                "processing_time": 1.23
            }
        }

class AgentInfo(BaseModel):
    name: str
    description: str
    model: str
    temperature: float
    available: bool

class HealthResponse(BaseModel):
    status: str
    agents_loaded: int
    api_keys_configured: Dict[str, bool]