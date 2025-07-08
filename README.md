# Multi-Agent Router System

A sophisticated AI agent routing system built with LangChain that intelligently routes user queries to specialized agents based on their expertise. Perfect for multi-tenant environments with Kubernetes support.

## Features

- **Intelligent Routing**: Automatically routes queries to the most appropriate specialized agent
- **Multiple LLM Providers**: Supports OpenAI, Anthropic, Google, and OpenRouter
- **Specialized Agents**: Pre-configured agents for Marketing, CRM, Sales, Support, Analytics, and General queries
- **Kubernetes Ready**: Complete deployment configurations for scalable production use
- **FastAPI Backend**: High-performance async API with automatic documentation
- **Multi-tenant Support**: Designed for isolated client environments
- **Health Monitoring**: Built-in health checks and monitoring endpoints

## Architecture

```
User Query → Routing Agent → Specialized Agent → Response
     ↓              ↓              ↓
   FastAPI    →  LangChain   →   LLM Provider
```

## Specialized Agents

1. **Marketing Agent** (OpenAI): Handles marketing campaigns, content creation, brand strategy
2. **CRM Agent** (Anthropic): Manages customer relationships, data analysis, lifecycle management
3. **Sales Agent** (OpenRouter): Handles sales processes, lead generation, revenue optimization
4. **Support Agent** (Google): Provides customer support, troubleshooting, issue resolution
5. **Analytics Agent** (OpenAI): Handles data analysis, reporting, business intelligence
6. **General Agent** (OpenAI): Fallback for queries that don't fit other categories

## Quick Start

### Option 1: Conda Environment (Recommended)

```bash
# Clone the repository
git clone <your-repo-url>
cd multi-agent-router

# Make setup script executable and run
chmod +x setup.sh
./setup.sh

# Edit .env file with your API keys
nano .env

# Activate environment and run
conda activate multi-agent-router
python main.py
```

### Option 2: Docker

```bash
# Build and run with Docker
chmod +x docker-setup.sh
./docker-setup.sh

# Edit docker-secrets.env with your API keys
nano docker-secrets.env

# Run container
docker run --env-file docker-secrets.env -p 8000:8000 multi-agent-router:latest
```

### Option 3: Kubernetes

```bash
# Setup Kubernetes deployment
chmod +x kubernetes-setup.sh
./kubernetes-setup.sh

# Update secrets with your API keys (base64 encoded)
kubectl edit secret api-keys -n multi-agent-router

# Check deployment
kubectl get pods -n multi-agent-router
kubectl get service -n multi-agent-router
```

## API Usage

### Send a Chat Message

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "How can I improve my email marketing campaign?",
    "user_id": "user123",
    "context": {"company": "TechCorp"}
  }'
```

### Python Client Example

```python
import asyncio
from client_example import MultiAgentClient

async def main():
    client = MultiAgentClient("http://localhost:8000")
    
    response = await client.send_message(
        "Help me analyze customer churn rates",
        user_id="user123"
    )
    
    print(f"Agent: {response['agent_used']}")
    print(f"Response: {response['response']}")

asyncio.run(main())
```

## API Endpoints

- `POST /chat` - Send a message to the router
- `GET /health` - Health check endpoint
- `GET /agents` - List all available agents
- `GET /docs` - Interactive API documentation

## Environment Variables

```env
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional Configuration
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
```

## Customization

### Adding New Agents

1. Define agent type in `AgentType` enum
2. Add configuration in `_initialize_agent_configs()`
3. Specify keywords, system prompt, and LLM provider

```python
AgentType.FINANCE: AgentConfig(
    name="Finance Agent",
    description="Handles financial analysis and reporting",
    system_prompt="You are a financial expert...",
    keywords=["finance", "budget", "accounting", "revenue"],
    llm_provider="anthropic"
)
```

### Customizing Routing Logic

The routing system uses a dedicated LLM to make intelligent routing decisions. You can customize the routing prompt in `_create_routing_prompt()` method.

### Adding New LLM Providers

1. Add provider configuration in `_initialize_agents()`
2. Update agent configs to use new provider
3. Add any provider-specific error handling

## Kubernetes Configuration

### Resource Requirements

- **CPU**: 250m request, 500m limit
- **Memory**: 512Mi request, 1Gi limit
- **Replicas**: 3 (configurable)

### Scaling

```bash
# Scale deployment
kubectl scale deployment multi-agent-router --replicas=5 -n multi-agent-router

# Horizontal Pod Autoscaler
kubectl autoscale deployment multi-agent-router --cpu-percent=50 --min=3 --max=10 -n multi-agent-
