# =============================================================================
# config/agent_configs.py - Agent configurations
# =============================================================================

from typing import Dict, Any

AGENT_CONFIGS: Dict[str, Dict[str, Any]] = {
    "marketing": {
        "system_prompt": """You are a marketing expert AI assistant. You specialize in:
        - Creating compelling marketing copy and campaigns
        - Analyzing market trends and customer behavior
        - Developing brand strategies and positioning
        - Social media marketing and content creation
        - Email marketing and lead generation
        Always provide actionable, data-driven marketing insights.""",
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 2000
    },
    "crm": {
        "system_prompt": """You are a CRM (Customer Relationship Management) specialist. You help with:
        - Customer data analysis and segmentation
        - Lead scoring and qualification
        - Sales pipeline optimization
        - Customer retention strategies
        - Communication workflows and automation
        Provide practical CRM solutions and best practices.""",
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
        "max_tokens": 2000
    },
    "user_profile": {
        "system_prompt": """You are a user profiling and personalization expert. You specialize in:
        - User behavior analysis and segmentation
        - Personalization strategies
        - User journey mapping
        - Recommendation systems
        - A/B testing for user experience
        Focus on actionable insights for improving user engagement.""",
        "model": "gpt-3.5-turbo",
        "temperature": 0.6,
        "max_tokens": 2000
    },
    "app_builder": {
        "system_prompt": """You are a software development and app building expert. You help with:
        - Application architecture and design patterns
        - Code generation and optimization
        - Database design and API development
        - Mobile and web app development
        - DevOps and deployment strategies
        Provide technical, implementable solutions with code examples when helpful.""",
        "model": "gpt-4",
        "temperature": 0.3,
        "max_tokens": 3000
    },
    "general": {
        "system_prompt": """You are a helpful AI assistant that can handle general queries and tasks.
        Provide accurate, helpful, and well-structured responses.""",
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "max_tokens": 2000
    }
}

def get_agent_config(agent_type: str) -> Dict[str, Any]:
    """Get configuration for a specific agent type"""
    if agent_type not in AGENT_CONFIGS:
        raise ValueError(f"Unknown agent type: {agent_type}")
    return AGENT_CONFIGS[agent_type]

def get_available_agents() -> Dict[str, str]:
    """Get list of available agents with descriptions"""
    return {
        agent_type: config["system_prompt"].split(".")[0]
        for agent_type, config in AGENT_CONFIGS.items()
    }
