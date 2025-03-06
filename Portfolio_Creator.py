"""
Author: S.T.Sathish (SKYLIB)
Email: skylib.stsathish@gmail.com
Website: https://beacons.ai/skylib
Date Created: 11-December-2024
Description: Portfolio Management Script

Program Generated with: ChatGPT (OpenAI)

Copyright (c) [2025] S.T.Sathish (SKYLIB)
"""

import os
import csv
import yfinance as yf
import logging
from datetime import datetime

# 1. Ensure the directory for portfolios, logs, and data exists
portfolio_dir = "Portfolio_List"
data_dir = "data"
log_dir = "log"

# 2. Create directories if they don't exist
os.makedirs(portfolio_dir, exist_ok=True)
os.makedirs(data_dir, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

# 3. Define data and log file paths
data_file = os.path.join(data_dir, "portfolio_data.txt")
log_file = os.path.join(log_dir, "portfolio_log.log")

# 4. Set up logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Log all events
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# 5. Log initial message
logging.info("Portfolio Management System started.")

# 6. Ensure the data file exists and initialize if not
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        f.write("number = 1\nportfolios = []\n")
    logging.info(f"Created new data file at {data_file}.")

# 7. Load the portfolio data
def load_portfolio_data():
    global number, portfolios
    with open(data_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("number"):
                number = int(line.split("=")[1].strip())
            elif line.startswith("portfolios"):
                portfolios = eval(line.split("=")[1].strip())  # Convert string list to actual list
    logging.info(f"Loaded portfolio data: number={number}, portfolios={portfolios}")

# 8. Save the portfolio data
def save_portfolio_data(number, portfolios):
    with open(data_file, "w") as f:
        f.write(f"number = {number}\nportfolios = {portfolios}\n")
    logging.info(f"Saved portfolio data: number={number}, portfolios={portfolios}")

# 9. Fetch the current price of a stock
def fetch_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        company_name = stock.info.get('longName', 'Unknown Company')
        price = stock.history(period="1d")['Close'].iloc[-1]  # Last close price
        logging.info(f"Fetched current price for {symbol}: {price}")
        return price, company_name
    except Exception as e:
        logging.error(f"Error fetching current price for {symbol}: {e}")
        print(f"Error fetching current price for {symbol}: {e}")
        return None

# Limit the company name to a specific number of characters
def get_short_company_name(company_name, max_length=15):
    if len(company_name) > max_length:
        return company_name[:max_length] + "..."  # Truncate and append '...'
    else:
        return company_name  # Return as is if within the length limit

# 10. Create a new portfolio
def create_portfolio():
    load_portfolio_data()

    portfolio_name = f"Portfolio_{number}.csv"
    file_path = os.path.join(portfolio_dir, portfolio_name)

    print("\nDo you want to split the investment amount equally or enter details manually?")
    print("1. Split equally")
    print("2. Enter manually")
    choice = input("Enter your choice (1/2): ").strip()

    investments = []

    if choice == "1":  # Equal Split
        while True:  # Start a loop to validate user input
            try:
                total_amount = float(input("Enter the total investment amount in INR: "))
                if total_amount > 0:
                    break  # Exit the loop if a valid number is entered
                else:
                    print("Amount must be greater than zero. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        print("Enter the company symbols (one per line). Type 'done' when finished.")
        symbols = []
        while True:
            symbol = input("Enter Company Symbol (Yahoo Finance): ").strip()
            if symbol.lower() == 'done':
                break
            symbols.append(symbol)

        if not symbols:
            print("No symbols entered. Aborting portfolio creation.")
            logging.warning("No symbols entered. Aborting portfolio creation.")
            return

        amount_per_company = total_amount / len(symbols)
        for symbol in symbols:
            current_price, company_name = fetch_current_price(symbol)
            
            if current_price is None:
                print(f"Could not fetch price for {symbol}. Skipping...")
                logging.error(f"Could not fetch price for {symbol}. Skipping...")
                continue

            shares = int(amount_per_company // current_price)  # Calculate maximum shares purchasable
            total_cost = shares * current_price
            investments.append([company_name, symbol, round(current_price, 2), shares, round(total_cost, 2)])

    elif choice == "2":  # Manual Input
        print("\nEnter investment details (one by one). Type 'done' to finish.")
        while True:
            symbol = input("Enter Company Symbol (Yahoo Finance): ").strip()
            if symbol.lower() == 'done':
                break

            current_price, company_name = fetch_current_price(symbol)
            if current_price is None:
                print(f"Could not fetch price for {symbol}. Skipping...")
                logging.error(f"Could not fetch price for {symbol}. Skipping...")
                continue

            try:
                total_shares = int(input(f"Enter Total Shares for {company_name}: "))
                total_cost = current_price * total_shares
                investments.append([company_name, symbol, round(current_price, 2), total_shares, round(total_cost, 2)])
            except ValueError:
                print("Invalid input. Please try again.")

    else:
        print("Invalid choice. Aborting portfolio creation.")
        logging.warning("Invalid choice for portfolio creation.")
        return

    # 11. Display the portfolio before saving
    print("\nPortfolio Details (Not Saved Yet):")
    print(f"{'Company Name':<20}{'Symbol':<15}{'Price/Share (₹)':<20}{'Shares':<10}{'Total Cost (₹)'}")
    print("-" * 65)

    for row in investments:
        company_name, symbol, price_per_share, shares, total_cost = row
        short_company_name = get_short_company_name(company_name, max_length=15)

        print(f"{short_company_name:<20}{symbol:<15}₹{price_per_share:<21}{shares:<10}₹{total_cost:<21}")

    # 12. Ask user if they want to save the portfolio
    save_choice = input("\nDo you want to save this portfolio? (y/n): ").strip().lower()
    if save_choice == "y":
        # Save investments to CSV
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Portfolio Created On", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])  # Add creation date to header
            writer.writerow(["Company Name", "Symbol", "Price per Share", "Shares", "Total Cost"])
            writer.writerows(investments)

        # 13. Update portfolio data
        portfolios.append(portfolio_name)
        save_portfolio_data(number + 1, portfolios)

        print(f"\nPortfolio '{portfolio_name}' has been created and saved in '{portfolio_dir}'.")
        logging.info(f"Portfolio '{portfolio_name}' has been created and saved in '{portfolio_dir}'.")

    else:
        print("\nPortfolio not saved.")
        logging.info("Portfolio creation was aborted.")

# 14. Show an existing portfolio
def show_portfolio():
    load_portfolio_data()

    if not portfolios:
        print("No portfolios exist. Please create one first.")
        logging.warning("No portfolios exist. Please create one first.")
        return

    print("\nExisting Portfolios:")
    for i, name in enumerate(portfolios):
        print(f"{i + 1}. {name}")

    try:
        choice = int(input("Enter the number of the portfolio to view: ")) - 1
        if choice < 0 or choice >= len(portfolios):
            print("Invalid selection.")
            logging.warning("Invalid portfolio selection.")
            return
    except ValueError:
        print("Invalid input.")
        logging.warning("Invalid input for portfolio selection.")
        return

    file_path = os.path.join(portfolio_dir, portfolios[choice])

    # 15. Ask user if they want to display with current prices and profit/loss
    display_choice = input("Do you want to display with current prices and profit/loss? (y/n): ").strip().lower()

    # 16. Read the portfolio content
    print("\nPortfolio Details:")
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header1 = next(reader)  # First header contains the creation date
        header2 = next(reader)  # Second header contains column names
        rows = list(reader)

        creation_date = header1[1]  # Retrieve creation date from the first header row
        print(f"Portfolio created on: {creation_date}\n")  # Display creation date

    total_investment = 0
    total_current_cost = 0

    if display_choice == "y":
        print(f"{'Company Name':<20}{'Symbol':<15}{'Price/Share (₹)':<20}{'Shares':<10}{'Total Cost (₹)':<20}{'Current Price (₹)':<20}{'Current Cost (₹)':<20}{'Profit/Loss (₹)':<20}")
        print("-" * 140)

        for row in rows:
            company_name, symbol, price_per_share, shares, total_cost = row
            current_price, company_name = fetch_current_price(symbol)
            short_company_name = get_short_company_name(company_name, max_length=15)

            if current_price:
                shares = int(shares)
                total_cost = float(total_cost)
                current_cost = current_price * shares
                profit_loss = current_cost - total_cost

                # 17. Print row data with current prices and profit/loss
                print(f"{short_company_name:<20}{symbol:<15}₹{price_per_share:<19}{shares:<10}₹{total_cost:<19.2f}₹{current_price:<19.2f}₹{current_cost:<19.2f}₹{profit_loss:<19.2f}")

                # 18. Totals
                total_investment += total_cost
                total_current_cost += current_cost
            else:
                print(f"{symbol:<15} Data not available.")
        
        print("-" * 140)
        print(f"{'TOTALS':<35}{'':<20}{'':<10}₹{total_investment:<19.2f}{'':<20}₹{total_current_cost:<19.2f}₹{total_current_cost - total_investment:<19.2f}")
    else:
        print(f"{'Company Name':<20}{'Symbol':<15}{'Price/Share (₹)':<20}{'Shares':<10}{'Total Cost (₹)'}")
        print("-" * 78)

        for row in rows:
            company_name, symbol, price_per_share, shares, total_cost = row
            short_company_name = get_short_company_name(company_name, max_length=15)

            print(f"{short_company_name:<20}{symbol:<15}₹{price_per_share:<19}{shares:<10}₹{total_cost:<19}")

        print("-" * 78)

# 19. Delete a portfolio
def delete_portfolio():
    load_portfolio_data()

    if not portfolios:
        print("No portfolios exist. Please create one first.")
        logging.warning("No portfolios exist. Please create one first.")
        return

    print("\nExisting Portfolios:")
    for i, name in enumerate(portfolios):
        print(f"{i + 1}. {name}")

    try:
        choice = int(input("Enter the number of the portfolio to delete: ")) - 1
        if choice < 0 or choice >= len(portfolios):
            print("Invalid selection.")
            logging.warning("Invalid portfolio selection.")
            return
    except ValueError:
        print("Invalid input.")
        logging.warning("Invalid input for portfolio selection.")
        return

    # 20. Delete the selected portfolio
    file_path = os.path.join(portfolio_dir, portfolios[choice])
    os.remove(file_path)

    # 21 Update portfolio data
    deleted_portfolio = portfolios.pop(choice)
    save_portfolio_data(number, portfolios)

    print(f"Portfolio '{deleted_portfolio}' has been deleted.")
    logging.info(f"Portfolio '{deleted_portfolio}' has been deleted.")

# 22. Main Menu
def main():
    while True:
        print("\nPortfolio Management System")
        print("1. Create Portfolio")
        print("2. Show Portfolio")
        print("3. Delete Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            create_portfolio()
        elif choice == "2":
            show_portfolio()
        elif choice == "3":
            delete_portfolio()
        elif choice == "4":
            print("Exiting. Thank you!")
            logging.info("Exiting Portfolio Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
            logging.warning("Invalid menu choice.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully...")
        logging.info("Process interrupted by user. Exiting gracefully.")
