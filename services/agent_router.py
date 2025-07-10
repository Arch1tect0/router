# =============================================================================
# services/agent_router.py - Core routing logic
# =============================================================================

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from typing import Dict, Optional
import time
from config.settings import get_settings
from config.agent_configs import AGENT_CONFIGS, get_agent_config
from utils.logger import get_logger

logger = get_logger(__name__)

class AgentRouter:
    def __init__(self):
        self.settings = get_settings()
        self.agents: Dict[str, ChatOpenAI] = {}
        self._initialize_agents()
    
    def _initialize_agents(self):
        """Initialize all agents with their configurations"""
        for agent_type, config in AGENT_CONFIGS.items():
            try:
                if config["model"].startswith("gpt") and self.settings.openai_api_key:
                    self.agents[agent_type] = ChatOpenAI(
                        model=config["model"],
                        temperature=config["temperature"],
                        max_tokens=config.get("max_tokens", 2000),
                        openai_api_key=self.settings.openai_api_key
                    )
                    logger.info(f"Initialized {agent_type} agent with {config['model']}")
                else:
                    logger.warning(f"Cannot initialize {agent_type} agent - missing API key")
            except Exception as e:
                logger.error(f"Failed to initialize {agent_type} agent: {str(e)}")
    
    def is_agent_available(self, agent_type: str) -> bool:
        """Check if an agent is available"""
        return agent_type in self.agents
    
    def get_available_agents(self) -> Dict[str, bool]:
        """Get list of all agents and their availability status"""
        return {
            agent_type: self.is_agent_available(agent_type)
            for agent_type in AGENT_CONFIGS.keys()
        }
    
    async def process_request(self, agent_type: str, prompt: str, context: Optional[Dict] = None) -> Dict:
        """Process a request through the appropriate agent"""
        start_time = time.time()
        
        # Validate agent type
        if agent_type not in AGENT_CONFIGS:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        # Check if agent is available
        if not self.is_agent_available(agent_type):
            raise RuntimeError(f"Agent {agent_type} is not available")
        
        try:
            # Get agent configuration
            agent_config = get_agent_config(agent_type)
            
            # Prepare messages
            messages = [
                SystemMessage(content=agent_config["system_prompt"]),
                HumanMessage(content=prompt)
            ]
            
            # Add context if provided
            if context:
                context_msg = f"Additional context: {context}"
                messages.insert(1, HumanMessage(content=context_msg))
            
            # Get response from agent
            agent = self.agents[agent_type]
            response = agent(messages)
            
            processing_time = time.time() - start_time
            
            return {
                "response": response.content,
                "processing_time": processing_time,
                "status": "success"
            }
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Error processing request for {agent_type}: {str(e)}")
            return {
                "response": f"Error processing request: {str(e)}",
                "processing_time": processing_time,
                "status": "error"
            }

# Singleton pattern for router
_router = None

def get_router() -> AgentRouter:
    global _router
    if _router is None:
        _router = AgentRouter()
    return _router