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

questions_text = ["can you reliably commute to colchester 3 days per week", "do you have commercial experience with blazor", "do you have full right to work in the uk"]

prompt = f"""You are helping someone apply for a remote software developer job in the UK.
Answer each yes/no question below. Reply ONLY with a JSON array of answers like: ["yes", "no", "yes"]

Rules:
- If asked about technical experience, respond with = yes
- If asked about commuting, respond with = no (I am seeking a fully remote position and am unable to commute.)
- If asked about legal qualifications to work, respond with = yes (I am legally qualified to work in the UK)

Questions:
{questions_text}

Reply with ONLY a JSON array, nothing else. Example: ["yes", "no", "yes"]"""

# Step 4 — Send a simple test prompt
messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print("\nTest response:", response.choices[0].message.content)
