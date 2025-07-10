from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

chain = llm | StrOutputParser()

result = chain.invoke("Tell me a joke about dogs.")
print(result)

