# TASK 2: Stock Portfolio Tracker
# Intern: FAISUL HAMEER AFANA | ID: CA/DF1/434642

def stock_portfolio():
    # Hardcoded stock prices as per instruction
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "MSFT": 300,
        "AMZN": 3300
    }

    portfolio = {}
    total_value = 0

    print("=== CodeAlpha Stock Portfolio Tracker ===")
    print(f"Available Stocks: {list(stock_prices.keys())}")
    
    while True:
        stock = input("\nEnter Stock Name (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not in price list! Try AAPL, TSLA etc.")
            continue
        
        try:
            qty = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except:
            print("Enter valid number")

    print("\n--- Your Portfolio ---")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_value += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")

    print(f"\nTotal Investment Value: ${total_value}")

    # Optional: save to txt file
    save = input("\nSave to file? (yes/no): ").lower()
    if save == 'yes':
        with open("portfolio.txt", "w") as f:
            f.write(f"Total Investment: ${total_value}\n")
            for s, q in portfolio.items():
                f.write(f"{s}: {q}\n")
        print("Saved as portfolio.txt")

stock_portfolio()
