# AI Agent Router

Multi-agent AI routing system with LangChain integration.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your API keys
4. Run: `python main.py`

## API Endpoints

- `GET /` - Basic info
- `GET /agents` - List available agents
- `POST /chat` - Chat with agents
- `GET /health` - Health check

## Available Agents

- **marketing** - Marketing campaigns and strategies
- **crm** - Customer relationship management
- **user_profile** - User behavior analysis
- **app_builder** - Software development
- **general** - General purpose assistant
