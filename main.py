from dotenv import load_dotenv
import os
from openai import OpenAI

# Step 1 — Load .env file
load_dotenv(override=True)

# Step 2 — Get the API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"✅ OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("❌ OpenAI API Key not set - please check your .env file")

# Step 3 — Initialize the OpenAI client
openai = OpenAI()

# Step 4 — Send a simple test prompt
messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 2+2?"}]
response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print("\nTest response:", response.choices[0].message.content)
