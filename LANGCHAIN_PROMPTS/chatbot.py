from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
import os 

load_dotenv()

hf_token = os.environ['HUGGINGFACEHUB_API_TOKEN']
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-3B-Instruct",task="text-generation",huggingfacehub_api_token=hf_token)
model = ChatHuggingFace(llm=llm)


## Creating Chat History : 
chat_history = []
while True:
    user_input = input("You : ")
    chat_history.append(user_input)
    if user_input=="exit":
        print(":) Thank You :)")
        break
    else:
        result = model.invoke(chat_history)
        chat_history.append(result.content)
        print("AI: ",result.content)

print(chat_history)