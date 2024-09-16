from stocks_m.stock import Stock

# Create an instance of Stock with "Edison" as the company name
edison_stock = Stock(stock_price=100.0, company_name="Edison", std=0.02, mean=0.01, description="Energy company", actives="Shares")

# Display initial stock information
print(f"Initial Stock Price for {edison_stock.get_company_name()}: ${edison_stock.get_stock_price()}")

# Update the stock price with a 5% change
edison_stock.update_stock_price(5.0)

# Display the new stock price after the update
print(f"Updated Stock Price after 5% increase: ${edison_stock.get_stock_price()}")

# Display the recorded percentage change
print(f"Percentage Change: {edison_stock.get_percentage()}%")

# Generate initial stock data for 30 days
edison_stock.generate_initial_stock_data(num_days=60)

# Display stored stock variation data
print(f"Stock Variation Data: {edison_stock.get_stock_variation()}")

# Plot the candlestick chart
edison_stock.candlestick()
