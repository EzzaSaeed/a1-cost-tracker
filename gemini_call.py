
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.8-flash"

client = genai.Client()

resp = client.models.generate_content(
    model=MODEL,
    contents="Explain tokens in one simple sentence."
)

print("Gemini Reply:")
print(resp.text)

print("Input Tokens:", resp.usage_metadata.prompt_token_count)
print("Output Tokens:", resp.usage_metadata.candidates_token_count)

