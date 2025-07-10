from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks import get_openai_callback
from config import API_KEYS, AGENT_CONFIGS

def get_llm(model_name: str = "gpt-3.5-turbo"):
    """Initialize LangChain model"""
    if model_name.startswith("gpt"):
        return ChatOpenAI(
            model_name=model_name,
            openai_api_key=API_KEYS["openai"],
            temperature=0.7
        )
    else:
        raise ValueError(f"Unsupported model: {model_name}")

async def process_chat(agent: str, prompt: str, model: str = "gpt-3.5-turbo"):
    """Process chat request through specified agent"""
    if agent not in AGENT_CONFIGS:
        raise ValueError(f"Unknown agent: {agent}")
    
    # Get LLM instance
    llm = get_llm(model)
    
    # Prepare messages
    system_message = SystemMessage(content=AGENT_CONFIGS[agent]["system_prompt"])
    human_message = HumanMessage(content=prompt)
    
    # Get response with token tracking
    with get_openai_callback() as cb:
        response = await llm.agenerate([[system_message, human_message]])
        response_text = response.generations[0][0].text
        tokens_used = cb.total_tokens
    
    return {
        "response": response_text,
        "tokens_used": tokens_used
    }
