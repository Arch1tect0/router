File Structure:
project/
├── main.py          # FastAPI app entry point
├── routes.py        # API endpoints
├── models.py        # Request/response models
├── config.py        # Agent configs and API keys
├── ai_service.py    # AI processing logic
├── requirements.txt # Dependencies
└── .env            # Environment variables
Setup:

Install dependencies: pip install -r requirements.txt
Set up your .env file with API keys
Run: python main.py

Usage:
bash# List agents
curl http://localhost:8000/agents

# Chat with marketing agent
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"agent": "marketing", "prompt": "Create a campaign for a new app"}'

# Set API key
curl -X POST http://localhost:8000/api-keys/openai \
  -H "Content-Type: application/json" \
  -d '"your_api_key_here"'
