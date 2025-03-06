

## Portfolio Management Script

The Portfolio Management Script is a script designed for creating and managing simulated share market portfolios. It enables users to allocate investment amounts equally or specify allocations manually. The program fetches real-time share prices using the yfinance library, providing an efficient way to monitor and analyze investments and trades. Share prices are displayed in ₹ (Indian Rupees), intended for Indian users. However, displaying prices in other currencies might be updated in future.

**Features**

 1. Create Portfolios: Allocate funds equally or manually set investment
    amounts.
 2. Track Performance: Fetch the latest share prices in real-time (not a continuous live feed).
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
    
    `git clone https://github.com/skylib11/Portfolio_Creator

     cd Portfolio_Creator


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
The script will ask 
"Do you want to split the investment amount equally or enter details manually?
1. Split equally
2. Enter manually
Enter your choice (1/2):"

**1. Split equally:** The program will automatically distribute your total investment equally across the shares.

**2. Enter manually:** Specify the amount to invest in each stock.


You will be prompted to enter share market company symbols (e.g., RELIANCE.NS for Reliance Industries Limited, TCS.NS for Tata Consultancy Services Limited). Enter the symbols

	
After entering the share symbols and allocation, you will be prompted with:

> Do you want to save this portfolio? (y/n):

 - y: Saves the portfolio to a file.
 - n: The data will not be saved.

	  
**Option 2: Show Portfolio**
  Displays the existing portfolio. Then, you will be prompted with:

> Do you want to view it with recent prices and profit calculations? (y/n):

 - y: Displays the portfolio with real-time stock prices and calculates the profit/loss for each stock.
 - n: Shows just the portfolio data without the current prices or profit/loss calculations.	
	  
**Option 3: Delete Portfolio**
	 If you want to delete an existing portfolio, select this option. You will be shown a list of portfolios and prompted:
 
> Enter your choice:
	  
**Option 4: Exit**
Exits the program.

![Screenshot from 2025-03-06 18-53-27](https://github.com/user-attachments/assets/cf4b251e-b509-44c4-9278-7f71e357a700)

![Screenshot from 2025-03-06 18-55-13](https://github.com/user-attachments/assets/e86703df-cec9-4315-ade5-1eb078ceac9f)

![Screenshot from 2025-03-06 18-56-34](https://github.com/user-attachments/assets/6a165ba5-04e0-4931-82da-0f7f713e7e75)

  
**Monitor Output:**
        ◦ Log and portfolio details are saved in the respective folders (logs/, Portfolio_List/, etc.).

The following folders and files are excluded from version control:
/data/
/logs/
/Portfolio_List/


**License**

Copyright (c) 2025

Permission is hereby granted, free of charge, to any individual to use, copy, and distribute this software **for personal and commercial purposes**, subject to the following conditions:

1. The software **must not** be resold, sublicensed, or used as part of a commercial product or service.
2. The software **must not** be modified and redistributed.
3. Attribution to the original creator must be included in any copies or distributions.
4. The software is provided "as is," without warranty of any kind. The author is not responsible for any consequences arising from its use.
5. Companies or organizations must obtain explicit permission before using, modifying, or using these scripts.



---

This project and scripts were generated with the assistance of **ChatGPT**.

**Acknowledgments**
    • Yahoo Finance for financial data.
    • Developers and contributors to the yfinance library.

*README generated with ChatGPT (OpenAI).*
