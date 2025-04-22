from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

hf_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

template = load_prompt('promptTemplate.json')
prompt = template.invoke({
    "paper_input":"Attention is all you need",
    "style_input":"code_heavy",
    "length_input":"medium"
})

llm = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation",huggingfacehub_api_token=hf_token)
model = ChatHuggingFace(llm=llm)

result = model.invoke(prompt)
print(result.content)