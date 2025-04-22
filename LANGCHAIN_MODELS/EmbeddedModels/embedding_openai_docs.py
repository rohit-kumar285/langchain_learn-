from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = ["Delhi is the capital of India","Narendra Modi is the PM of India ",
             "Holi is the festival of colours","Diwali is the festival of lights"]

result = embedding.embed_documents(documents)
print(result)