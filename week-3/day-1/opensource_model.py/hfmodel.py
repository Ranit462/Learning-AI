
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)
