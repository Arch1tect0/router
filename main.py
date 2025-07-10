from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import os

# ----- 1. Load API keys from env vars -----

marketing_api_key = os.environ.get("MARKETING_API_KEY", "")
crm_api_key = os.environ.get("CRM_API_KEY", "")
user_profile_api_key = os.environ.get("USER_PROFILE_API_KEY", "")
app_builder_api_key = os.environ.get("APP_BUILDER_API_KEY", "")

# ----- 2. Define each agent -----

marketing_llm = ChatOpenAI(
    api_key=marketing_api_key,
    model="gpt-4"
)

crm_llm = ChatOpenAI(
    api_key=crm_api_key,
    model="gpt-4"
)

user_profile_llm = ChatOpenAI(
    api_key=user_profile_api_key,
    model="gpt-3.5-turbo"
)

app_builder_llm = ChatOpenAI(
    api_key=app_builder_api_key,
    model="gpt-4"
)

marketing_chain = marketing_llm | StrOutputParser()
crm_chain = crm_llm | StrOutputParser()
user_profile_chain = user_profile_llm | StrOutputParser()
app_builder_chain = app_builder_llm | StrOutputParser()

# ----- 3. Define routing logic -----

def router_fn(input_text: str):
    lower = input_text.lower()

    if "marketing" in lower:
        return marketing_chain
    elif "crm" in lower:
        return crm_chain
    elif "profile" in lower:
        return user_profile_chain
    elif "build app" in lower:
        return app_builder_chain
    else:
        return marketing_chain  # fallback

# ----- 4. Run -----

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    selected_chain = router_fn(user_input)
    result = selected_chain.invoke(user_input)
    print("Response:", result)

