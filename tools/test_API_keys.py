from dotenv import load_dotenv
import os

load_dotenv()  # this loads variables from .env into environment variables

google_api_key = os.getenv("GOOGLE_API_KEY")
print("Google API Key:", google_api_key)

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
print("OpenRouter API Key:", openrouter_api_key)
