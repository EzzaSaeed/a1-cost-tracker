
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "openai/gpt-oss-20b"

client = Groq()

resp = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Explain tokens in one simple sentence."
        }
    ]
)

print("Groq Reply:")
print(resp.choices[0].message.content)

print("Input Tokens:", resp.usage.prompt_tokens)
print("Output Tokens:", resp.usage.completion_tokens)
