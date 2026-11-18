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

## API Pricing References

- [Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Groq API Pricing and Models](https://console.groq.com/docs/model/openai/gpt-oss-20b)

Check the official pricing pages for the latest rates.

## Error Handling

If Gemini is temporarily unavailable, the program displays an error message and continues to the Groq provider.

## Author

Ezza Saeed

Software Engineering Student
