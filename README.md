# Credit Card Reader and Validator 
A Python-based application that reads credit card data from CSV files and classifies them using the Chain of Responsibility design pattern.
## Features

- Validates credit card numbers from CSV input
- Supports Visa, MasterCard, Amex, Discover
- Writes validation results to output file
- Demonstrates Chain of Responsibility pattern
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thuyluu9595/CMPE202-Individual-Project-Python.git
   cd CMPE202-Individual-Project-Python
2. Generate sample data file
    ```bash
    python sample_generator.py
3. Run the program
    ```bash
    python main.py sample_credit_cards.csv