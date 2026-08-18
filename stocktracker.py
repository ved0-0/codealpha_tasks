def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180.00,
        "TSLA": 250.00,
        "GOOGL": 140.00,
        "MSFT": 330.00,
        "AMZN": 135.00
    }

    portfolio = {}

    print("Welcome to the Stock Portfolio Tracker!")
    print("-" * 40)
    print("Available stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")

    while True:
        stock = input("\nEnter stock ticker (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found. Please try again.")
            continue

        quantity = input("Enter number of shares: ")

        if not quantity.isdigit():
            print("Please enter a valid number.")
            continue

        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"Added {quantity} shares of {stock}.")

    total_investment = 0

    print("\n" + "=" * 35)
    print("PORTFOLIO SUMMARY")
    print("=" * 35)

    if not portfolio:
        print("Your portfolio is empty.")
    else:
        for stock, quantity in portfolio.items():
            value = quantity * stock_prices[stock]
            total_investment += value

            print(f"{stock}: {quantity} shares × "
                  f"${stock_prices[stock]:.2f} = ${value:.2f}")

        print("-" * 35)
        print(f"Total Investment: ${total_investment:.2f}")


if __name__ == "__main__":
    stock_portfolio_tracker()