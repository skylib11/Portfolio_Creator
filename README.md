

## Portfolio Management Program

The Portfolio Management Program is a script designed for creating and managing simulated stock portfolios. It enables users to allocate investment amounts equally or specify allocations manually. The program fetches real-time stock prices and company information using the yfinance library, providing an efficient way to monitor and analyze investments. Stock prices are displayed in ₹ (Indian Rupees), intended for Indian users. However, displaying prices in other currencies will be updated in future versions.

**Features**

 1. Create Portfolios: Allocate funds equally or manually set investment
    amounts.
 2. Track Performance: Monitor real-time stock prices and company
    details.
 3. Folder Structure: Automatically organizes logs, portfolio data, and
    other files into appropriate directories.

**Requirements**
    • Python 3.7 or higher
    • Libraries:
        ◦ yfinance
        ◦ pandas
        ◦ numpy
	
**Install** the required libraries using pip:

    pip install yfinance pandas numpy

 
**Folder Structure**
    • data/ : Stores simulation data files.
    • logs/ : Contains log files for program activity.
    • Portfolio_List/ : Holds files related to created portfolios.
    
**Usage**
    **1. Clone the Repository:**
    
    `git clone <repository-url>

     cd <repository-folder>`


   **2. Run the Program:**
        python3 portfolio_manager.py


  **3. Main Menu Options:**
	Upon running the program, you'll see the following menu options:

**Main Menu:**
 1. Create Portfolio
 2. Show Portfolio
 3. Delete Portfolio
 4. Exit
	
**Option 1: Create Portfolio**
You will be prompted to enter stock symbols (e.g., AAPL for Apple, GOOGL for Google). You can:

 **Allocate funds equally:** The program will automatically distribute your total investment equally across the stocks.

**Manually allocate funds:** Specify the amount to invest in each stock.
	
After entering the stock symbols and allocation, you will be prompted with:

> Do you want to save this portfolio? (y/n):

 - y: Saves the portfolio to a file.
 - n: The data will not be saved.

	  
**Option 2: Show Portfolio**
	Displays the saved portfolio. After saving the portfolio, you will be prompted with:

> Do you want to view it with current prices and profit calculations? (y/n):

 - y: Displays the portfolio with real-time stock prices and calculates the profit/loss for each stock.
 - n: Shows just the portfolio data without the current prices or profit/loss calculations.	
	  
**Option 3: Delete Portfolio**
	 If you want to delete an existing portfolio, select this option. You will be shown a list of portfolios and prompted:
 
> Enter your choice:
	  
**Option 4: Exit**
Exits the program. If there is any unsaved data, you will be prompted to confirm whether you want to save the portfolio before exiting:
	 
**Monitor Output:**
        ◦ Log and portfolio details are saved in the respective folders (logs/, Portfolio_List/, etc.).
.gitignore Configuration
The following folders and files are excluded from version control:
/data/
/logs/
/Portfolio_List/
Ensure the .gitignore file is present in the root directory to avoid tracking these files.

**Contributing**
Contributions are welcome! Please follow these steps:
    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Commit your changes and submit a pull request.

**License**
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for details.

**Acknowledgments**
    • Yahoo Finance for financial data.
    • Developers and contributors to the yfinance library.

*README generated with ChatGPT (OpenAI).*
