import os
import requests
from dotenv import load_dotenv

# Load .env values
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = os.getenv("OPENROUTER_API_URL")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct",  # <-- corrected ID
    "messages": [
        {"role": "user", "content": "What's a fun fact about Linux?"}
    ]
}

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("✅ Response from Mistral:")
    print(reply)
else:
    print(f"❌ Error {response.status_code}: {response.text}")
