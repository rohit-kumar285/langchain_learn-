from langchain_openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

llms = OpenAI(model="gpt-3.5-turbo-instruct-0914")
result = llms.invoke("what is the capital of India ?")
print(result)

