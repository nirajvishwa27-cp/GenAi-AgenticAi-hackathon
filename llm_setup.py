import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
 
def call_llm(prompt: str):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Simple test to verify it works when you run this file directly
if __name__ == "__main__":
    try:
        print("Testing Real LLM Connection...")
        response = call_llm("Say 'Hello Hackathon' if you can hear me.")
        print(f"✅ Success! LLM Said: {response}")
    except Exception as e:
        print(f"❌ Error: {e}")