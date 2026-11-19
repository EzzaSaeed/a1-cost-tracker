# Two Provider Cost Tracker

## Project Overview

Two Provider Cost Tracker is a Python-based project that compares two AI providers: Google Gemini and Groq.

It sends the same prompt to both providers and displays their generated responses, input tokens, output tokens, and estimated API cost per call.

The project also demonstrates how to work with API keys securely using environment variables.

## Technologies Used

- Python
- UV (Python package and project manager)
- Google Gemini API
- Groq API
- python-dotenv
- Git and GitHub

## Project Structure

```text
a1-cost-tracker/
│
├── main.py
├── gemini_call.py
├── groq_call.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/EzzaSaeed/a1-cost-tracker.git
```

2. Navigate to the project directory:

```bash
cd a1-cost-tracker
```

3. Install project dependencies:

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root directory and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder values with your own API keys.

**Important:** Never upload your `.env` file or expose your API keys publicly.

## Run the Project

Execute the main script:

```bash
uv run main.py
```

The script sends the same prompt to both providers and displays their responses and token usage.

## Cost Calculation

The project calculates estimated costs using the following formula:

```text
Cost = (Input Tokens × Input Price
      + Output Tokens × Output Price) / 1,000,000
```

Costs are calculated using standard paid API prices per one million tokens. For free-tier API calls, the displayed amount represents a hypothetical paid-price estimate, not an actual charge.
## Sample Output

The following output was generated during a successful test run. Token counts and AI responses may vary between requests.

```text
Connecting to Gemini...

--- GEMINI RESULTS ---
Reply: In AI, tokens are the small chunks of text—like words, parts of words, or punctuation—that language models use to read and generate language.
Input Tokens: 38
Output Tokens: 35
Estimated paid-price cost: $0.00031950

--- GROQ RESULTS ---
Reply: Tokens are the small pieces of text—such as words or subwords—that a language model reads, processes, and learns from.
Input Tokens: 78
Output Tokens: 111
Estimated paid-price cost: $0.00003915
```

### Pricing Used

| Provider | Model | Input / 1M tokens | Output / 1M tokens |
|---|---|---:|---:|
| Google Gemini | gemini-4-hydrogen | $1.50 | $7.50 |
| Groq | openai/gpt-oss-20b | $0.075 | $0.30 |

These are estimated standard paid prices. Actual charges depend on the provider's pricing tier and account usage.


## API Pricing References

- [Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Groq API Pricing and Models](https://console.groq.com/docs/model/openai/gpt-oss-20b)


## Author

Ezza Saeed

Software Engineering Student
