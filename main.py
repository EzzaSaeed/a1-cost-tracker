# Prices per 1M tokens (example values)

from dotenv import load_dotenv
from google import genai
from groq import Groq

load_dotenv()

# Model names
GEMINI_MODEL = "gemini-4-hydrogen"
GROQ_MODEL = "openai/gpt-oss-20b"

# Same prompt for both providers
PROMPT = "Explain tokens in one simple sentence."

# Paid prices per 1 million tokens (USD)
prices = {
    "gemini": {
        "input": 1.50,
        "output": 7.50
    },
    "groq": {
        "input": 0.075,
        "output": 0.30
    }
}


# Cost calculation function
def calculate_cost(input_tokens, output_tokens, provider_prices):

    input_cost = cost(
        input_tokens,
        provider_prices["input"]
    )

    output_cost = cost(
        output_tokens,
        provider_prices["output"]
    )

    return input_cost + output_cost


def cost(tokens, price_per_million):
    return tokens * price_per_million / 1_000_000


# Display results
def show_result(provider, reply, input_tokens, output_tokens):

    total_cost = calculate_cost(
        input_tokens,
        output_tokens,
        prices[provider]
    )

    print(f"\n--- {provider.upper()} RESULTS ---")
    print("Reply:", reply)
    print("Input Tokens:", input_tokens)
    print("Output Tokens:", output_tokens)
    print(f"Estimated paid-price cost: ${total_cost:.8f}")



# Gemini API call
try:
    print("\nConnecting to Gemini...")

    gemini_client = genai.Client()

    gemini_response = gemini_client.models.generate_content(
        model=GEMINI_MODEL,
        contents=PROMPT
    )

    show_result(
        "gemini",
        gemini_response.text,
        gemini_response.usage_metadata.prompt_token_count,
        gemini_response.usage_metadata.candidates_token_count
    )

except Exception as e:
    print("\n--- GEMINI ERROR ---")
    print("Gemini is temporarily unavailable.")
    print("Error:", e)




# Groq API call
groq_client = Groq()

groq_response = groq_client.chat.completions.create(
    model=GROQ_MODEL,
    messages=[
        {"role": "user", "content": PROMPT}
    ]
)

show_result(
    "groq",
    groq_response.choices[0].message.content,
    groq_response.usage.prompt_tokens,
    groq_response.usage.completion_tokens
)
