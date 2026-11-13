# 🛒 Smart Grocery Store Management System

A comprehensive, beginner-friendly console application built in Python to streamline daily retail and grocery store operations. This project serves as a practical demonstration of how **Python Lists and Dictionaries** can be combined to act as an in-memory database for managing product inventories, tracking customer sales, and generating real-time business analytics.

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Folder & File Structure](#-folder--file-structure)
3. [Data Structures & Schema Design](#-data-structures--schema-design)
4. [Variables & Functions Reference Tables](#-variables--functions-reference-tables)
5. [Detailed Feature Breakdown](#-detailed-feature-breakdown)
6. [How to Run the Application](#-how-to-run-the-application)
7. [Sample Console Output](#-sample-console-output)
8. [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

Local grocery stores often struggle with manual record-keeping for stock levels, pricing, and daily revenue. The **Smart Grocery Store Management System** solves this problem by providing an interactive, menu-driven Command Line Interface (CLI) where a store owner or cashier can:
* Maintain a structured catalog of items.
* Prevent human errors such as duplicate Product IDs or selling out-of-stock items.
* Automatically calculate customer bills and update remaining stock in real time.
* Audit store performance via an automated reporting engine.

---

## 📁 Folder & File Structure

```text
Python Lists & Dictionaries/
│
├── grocery_store.py    # Core Python script containing data models, functions, and main menu loop
└── README.md           # Comprehensive project documentation for GitHub
```

---

## 🗄️ Data Structures & Schema Design

This application relies on **Lists of Dictionaries** as its primary in-memory storage mechanism.

### 1. Product Dictionary Schema (`products` list)
Each item in the `products` list is a dictionary representing a single store product:

| Key | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| `"id"` | `int` | Unique numeric identifier for the product | `101` |
| `"name"` | `str` | Display name of the grocery item | `"Milk"` |
| `"category"` | `str` | Department or classification of the product | `"Dairy"` |
| `"price"` | `float` / `int` | Unit selling price of the item | `250` |
| `"stock"` | `int` | Current available quantity in inventory | `20` |

### 2. Sales Record Dictionary Schema (`sales_records` list)
Whenever a customer purchase is completed, a transaction dictionary is appended to `sales_records`:

| Key | Data Type | Description | Example Value |
| :--- | :--- | :--- | :--- |
| `"product_id"` | `int` | ID of the product that was sold | `101` |
| `"product_name"` | `str` | Name of the sold product | `"Milk"` |
| `"quantity_sold"` | `int` | Number of units purchased by the customer | `2` |
| `"total_amount"` | `float` / `int` | Total revenue earned from this transaction (`price * quantity`) | `500` |

---

## 📊 Variables & Functions Reference Tables

### Global & Local Variables

| Variable Name | Scope | Data Type | Purpose |
| :--- | :--- | :--- | :--- |
| `products` | Global | `list[dict]` | Master inventory list storing all product dictionaries. Pre-loaded with 3 sample items. |
| `sales_records` | Global | `list[dict]` | Transaction log storing every completed customer sale dictionary. |
| `choice` | Local (`main`) | `str` | Captures the user's menu selection (`"1"` through `"8"`). |
| `prod_id` | Local | `int` | Stores the Product ID entered by the user during add, update, or sale operations. |
| `existing_product` | Local (`main`) | `dict` / `None` | Holds the result of `find_product_by_id()` to check for duplicate IDs. |
| `quantity_wanted` | Local (`main`) | `int` | Number of units a customer wishes to buy during a sale. |
| `total` | Local (`main`) | `float` / `int` | Calculated bill amount for a single customer transaction. |
| `total_stock` | Local (`generate_report`) | `int` | Accumulator variable summing up stock across all products. |
| `total_revenue` | Local (`generate_report`) | `float` / `int` | Accumulator variable summing up `total_amount` across all sales. |
| `low_stock_found` | Local (`generate_report`) | `bool` | Flag used to track whether any product has fewer than 5 units in stock. |
| `highest` / `lowest` | Local (`generate_report`) | `dict` | Tracks the product dictionaries with the maximum and minimum prices. |

### Custom Functions

| Function Name | Parameters | Return Type | Description |
| :--- | :--- | :--- | :--- |
| `find_product_by_id(prod_id)` | `prod_id` (`int`) | `dict` or `None` | Iterates through the `products` list to locate a matching `"id"`. Returns the product dictionary if found, otherwise `None`. |
| `generate_report()` | None | `None` | Calculates total products, total stock units, total transactions, and total revenue. Identifies low-stock items (`< 5` units) as well as the highest and lowest priced items. |
| `main()` | None | `None` | Runs the continuous `while True` menu loop, handles user input, executes CRUD/sales logic, and controls program exit. |

---

## ⚙️ Detailed Feature Breakdown

1. **Add New Product (Option 1):**
   * Prompts the user for ID, Name, Category, Price, and Initial Stock.
   * Calls `find_product_by_id()` beforehand to ensure duplicate IDs are rejected.
2. **View All Products (Option 2):**
   * Loops through `products` and prints formatted details for every item in stock.
3. **Search Product (Option 3):**
   * Converts user input to lowercase (`.lower()`) to perform a case-insensitive substring search across product names.
4. **Update Product Stock (Option 4):**
   * Allows adding new shipments (positive integers) or deducting damaged/expired goods (negative integers), with a safeguard resetting negative totals to `0`.
5. **Process Customer Sale (Option 5):**
   * Verifies product existence and checks if `quantity_wanted <= item['stock']`.
   * Deducts sold units from inventory, logs the transaction into `sales_records`, and prints a formatted customer receipt.
6. **View Sales Records (Option 6):**
   * Displays a chronological history of all completed sales transactions.
7. **Generate Store Report (Option 7):**
   * Aggregates store-wide metrics and triggers low-stock warnings for items below 5 units.
8. **Exit (Option 8):**
   * Safely breaks out of the `while True` loop to terminate the program.

---

## 🚀 How to Run the Application

### Prerequisites
* **Python 3.6 or higher** installed on your system. No external third-party libraries are required.

### Step-by-Step Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd "Python Lists & Dictionaries"
   ```
3. **Execute the Python script:**
   ```bash
   python grocery_store.py
   ```

---

## 💻 Sample Console Output

```text
====================================
SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice (1-8): 5

--- Process Sale ---
Enter Product ID to sell: 101
Product: Milk | Price: $250 | Available Stock: 20
Enter quantity to buy: 2

--- Receipt ---
Item Sold     : Milk
Quantity      : 2
Total Amount  : $500
Stock Left    : 18
Sale Completed Successfully!
```

---

## 🔮 Future Enhancements
* **Persistent Storage:** Integrate Python's `json` or `csv` module so inventory and sales records are saved permanently to disk between sessions.
* **Exception Handling:** Add `try-except ValueError` blocks around numeric inputs (`int`/`float`) to prevent crashes if letters are entered accidentally.
* **Receipt Export:** Generate `.txt` or `.pdf` invoices for customers after each completed sale.