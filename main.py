# Prices per 1M tokens (example values)
prices = {
    "input": 0.10,
    "output": 0.40
}

# Cost calculation function
def cost(tokens, price_per_million):
    return tokens * price_per_million / 1_000_000


# Calculate total cost
total = cost(2000, prices["input"]) + cost(500, prices["output"])

# Display result
print(f"Cost per call: ${total:.6f}")