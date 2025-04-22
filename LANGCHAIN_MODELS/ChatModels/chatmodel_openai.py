from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model= "gpt-4o-mini",temperature=1.6)
result = llm.invoke("write a poem for me ?")
print(result.content)
