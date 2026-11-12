


import os
import requests
from dotenv import load_dotenv

load_dotenv()

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

url = "https://router.huggingface.co/v1/models"

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

print("\nAVAILABLE TEXT GENERATION MODELS:\n")

for model in data.get("data", []):
    for provider in model.get("providers", []):
        if provider.get("status") == "live":
            print("Model:", model.get("id"))
            print("Provider:", provider.get("provider"))
            print("Free:", provider.get("is_free", "Not specified"))
            print("Pricing:", provider.get("pricing", "Not specified"))
            print("-" * 50)
