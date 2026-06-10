stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 420,
    "TSLA": 200,
    "AMZN": 190
}

def main():
    portfolio = {}
    total_value = 0

    print("=" * 50)
    print("         STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : ${price}")

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Invalid stock symbol. Please try again.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_value += value

        print(
            f"Stock: {stock} | "
            f"Quantity: {quantity} | "
            f"Price: ${stock_prices[stock]} | "
            f"Value: ${value}"
        )

    print("-" * 50)
    print(f"Total Portfolio Value: ${total_value}")
    print("=" * 50)

    save = input("\nDo you want to save the report? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio_report.txt", "w") as file:
            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("=" * 50 + "\n")

            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity

                file.write(
                    f"Stock: {stock} | "
                    f"Quantity: {quantity} | "
                    f"Price: ${stock_prices[stock]} | "
                    f"Value: ${value}\n"
                )

            file.write("-" * 50 + "\n")
            file.write(f"Total Portfolio Value: ${total_value}\n")

        print("Portfolio report saved as portfolio_report.txt")

if __name__ == "__main__":
    main()