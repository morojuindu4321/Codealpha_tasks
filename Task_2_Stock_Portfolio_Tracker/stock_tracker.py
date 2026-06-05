stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 420,
    "TSLA": 200,
    "AMZN": 190
}

def main():
    portfolio_value = 0

    print("=== Stock Portfolio Tracker ===")

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol.")
            continue

        quantity = int(input("Enter quantity: "))

        value = stock_prices[stock] * quantity
        portfolio_value += value

        print(f"{stock} | Quantity: {quantity} | Value: ${value}")

    print("\nTotal Portfolio Value: $", portfolio_value)

if __name__ == "__main__":
    main()
