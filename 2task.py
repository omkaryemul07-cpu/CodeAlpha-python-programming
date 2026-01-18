# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from available stocks.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock},{quantity},{value}\n")
        file.write(f"Total Investment,{total_investment}\n")

    print("Portfolio saved to portfolio.txt")
