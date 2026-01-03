# Bus Ticket Purchase Project (COMP10121)

## Overview
This project provides a command-line interface (CLI) for browsing bus ticket categories and their top-up types from a CSV file. Users can purchase one or more top-ups per session, view a cart with totals, and save/load purchases across runs.

## Features
- Load categories and top-ups from `data/mobile_products.csv`
- Menu-based browsing: Categories → TopUps → Details
- Purchase flow with quantity (1..99)
- Cart view with line totals and overall total
- Save purchases to `purchases.csv` and load them on startup
- Input validation and error handling (prevents crashes)

## Folder Structure
- `main.py` : Main Windows entry point (CLI, purchase flow)
- `models.py` : `Category`, `TopUp` classes
- `file_handler.py` : CSV loading logic
- `purchases.py` : Save/load purchases via CSV
- `data/mobile_products.csv` : Data source
- `purchases.csv` : Generated saved purchases (not committed)

## How to Run (Windows)
1. Ensure the CSV file exists:
   `data/mobile_products.csv`
2. Open Terminal/PowerShell in the project folder and run:
   ```bash
   python main.py


## Use Cases

### UC1: View Categories
The user runs the program and sees a list of ticket categories loaded from the CSV file.
The user selects a category by entering its number.

### UC2: View TopUps
After selecting a category, the user sees all top-ups related to that category with their prices.

### UC3: Purchase a TopUp
The user selects a top-up, confirms the purchase, and enters a quantity.
The selected item is added to the cart.

### UC4: View Cart
The user can view all purchased items and see the total price.

### UC5: Save and Load Purchases
When the user exits the program, purchases are saved to a file.
When the program is run again, saved purchases are loaded automatically.


## Testing

- Entered letters instead of numbers → program did not crash.
- Entered out-of-range numbers → program asked again.
- Purchased multiple items → totals calculated correctly.
- Closed and reopened the program → purchases were loaded successfully.


## Critique

### What worked well
- Clear menu system and user flow.
- CSV file loaded correctly.
- Purchases were saved and loaded successfully.

### What could be improved
- Add the ability to edit or delete items from the cart.
- Improve the user interface for better usability.# bus-ticket-project
