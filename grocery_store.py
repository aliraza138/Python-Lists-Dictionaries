# ==========================================
# SMART GROCERY STORE MANAGEMENT SYSTEM
# ==========================================

# 1. Store our products in a list of dictionaries
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 3},
    {"id": 103, "name": "Eggs", "category": "Dairy", "price": 300, "stock": 15}
]

# Store completed sales records
sales_records = []


# ==========================================
# CUSTOM FUNCTIONS
# ==========================================

def find_product_by_id(prod_id):
    """
    Custom Function 1: Searches for a product using its ID.
    Returns the product dictionary if found, otherwise returns None.
    """
    for item in products:
        if item["id"] == prod_id:
            return item
    return None


def generate_report():
    """
    Custom Function 2: Calculates and displays the store summary report
    using simple loops and counters.
    """
    print("\n--- STORE MANAGEMENT REPORT ---")
    
    total_products = len(products)
    if total_products == 0:
        print("No products in inventory.")
        return

    # Calculate total stock and revenue using loops
    total_stock = 0
    for item in products:
        total_stock = total_stock + item["stock"]

    total_transactions = len(sales_records)
    
    total_revenue = 0
    for sale in sales_records:
        total_revenue = total_revenue + sale["total_amount"]

    # Find products with low stock (less than 5 units)
    print(f"Total Products in Store : {total_products}")
    print(f"Total Stock Units Left  : {total_stock}")
    print(f"Total Sales Made        : {total_transactions}")
    print(f"Total Revenue Generated : ${total_revenue}")

    print("\n[ Low Stock Alert (< 5 units) ]")
    low_stock_found = False
    for item in products:
        if item["stock"] < 5:
            print(f"- {item['name']} (ID: {item['id']}) has only {item['stock']} left!")
            low_stock_found = True
    if not low_stock_found:
        print("All products have sufficient stock.")

    # Find highest and lowest priced items simply
    highest = products[0]
    lowest = products[0]
    for item in products:
        if item["price"] > highest["price"]:
            highest = item
        if item["price"] < lowest["price"]:
            lowest = item

    print(f"\nHighest Priced Item : {highest['name']} (${highest['price']})")
    print(f"Lowest Priced Item  : {lowest['name']} (${lowest['price']})")
    print("-------------------------------")


# ==========================================
# MAIN PROGRAM LOOP
# ==========================================

def main():
    while True:
        # Display the Menu
        print("\n====================================")
        print("SMART GROCERY STORE SYSTEM")
        print("====================================")
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product Stock")
        print("5. Process Customer Sale")
        print("6. View Sales Records")
        print("7. Generate Store Report")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        # --- OPTION 1: ADD NEW PRODUCT ---
        if choice == '1':
            print("\n--- Add New Product ---")
            prod_id = int(input("Enter Product ID (e.g., 104): "))
            
            # Check if product ID already exists
            existing_product = find_product_by_id(prod_id)
            if existing_product != None:
                print("Error: A product with this ID already exists!")
            else:
                name = input("Enter Product Name: ")
                category = input("Enter Category: ")
                price = float(input("Enter Price: "))
                stock = int(input("Enter Initial Stock: "))
                
                # Create dictionary for the new product
                new_product = {
                    "id": prod_id,
                    "name": name,
                    "category": category,
                    "price": price,
                    "stock": stock
                }
                
                # Add to our products list
                products.append(new_product)
                print(f"Success! '{name}' was added.")

        # --- OPTION 2: VIEW ALL PRODUCTS ---
        elif choice == '2':
            print("\n--- All Products ---")
            if len(products) == 0:
                print("No products available.")
            else:
                for item in products:
                    print(f"ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Price: ${item['price']} | Stock: {item['stock']}")

        # --- OPTION 3: SEARCH PRODUCT ---
        elif choice == '3':
            print("\n--- Search Product ---")
            search_name = input("Enter product name to search: ").lower()
            
            found = False
            for item in products:
                if search_name in item['name'].lower():
                    print(f"\nFound It!")
                    print(f"ID       : {item['id']}")
                    print(f"Name     : {item['name']}")
                    print(f"Category : {item['category']}")
                    print(f"Price    : ${item['price']}")
                    print(f"Stock    : {item['stock']}")
                    found = True
            
            if found == False:
                print("No product found with that name.")

        # --- OPTION 4: UPDATE PRODUCT STOCK ---
        elif choice == '4':
            print("\n--- Update Stock ---")
            prod_id = int(input("Enter Product ID to update: "))
            item = find_product_by_id(prod_id)
            
            if item == None:
                print("Error: Product not found.")
            else:
                print(f"Current stock for {item['name']} is {item['stock']}.")
                add_stock = int(input("Enter quantity to add (use negative number to reduce): "))
                
                item['stock'] = item['stock'] + add_stock
                if item['stock'] < 0:
                    item['stock'] = 0 # Prevent negative stock
                
                print(f"Stock updated successfully! New stock is {item['stock']}.")

        # --- OPTION 5: PROCESS CUSTOMER SALE ---
        elif choice == '5':
            print("\n--- Process Sale ---")
            prod_id = int(input("Enter Product ID to sell: "))
            item = find_product_by_id(prod_id)
            
            if item == None:
                print("Error: Product not found.")
            else:
                print(f"Product: {item['name']} | Price: ${item['price']} | Available Stock: {item['stock']}")
                quantity_wanted = int(input("Enter quantity to buy: "))
                
                if quantity_wanted > item['stock']:
                    print("Sale Failed! Not enough stock available.")
                elif quantity_wanted <= 0:
                    print("Error: Please enter a valid quantity greater than 0.")
                else:
                    # Calculate total price
                    total = quantity_wanted * item['price']
                    
                    # Deduct stock
                    item['stock'] = item['stock'] - quantity_wanted
                    
                    # Save the sale record
                    sale_info = {
                        "product_id": item['id'],
                        "product_name": item['name'],
                        "quantity_sold": quantity_wanted,
                        "total_amount": total
                    }
                    sales_records.append(sale_info)
                    
                    print("\n--- Receipt ---")
                    print(f"Item Sold     : {item['name']}")
                    print(f"Quantity      : {quantity_wanted}")
                    print(f"Total Amount  : ${total}")
                    print(f"Stock Left    : {item['stock']}")
                    print("Sale Completed Successfully!")

        # --- OPTION 6: VIEW SALES RECORDS ---
        elif choice == '6':
            print("\n--- Sales Records ---")
            if len(sales_records) == 0:
                print("No sales made yet.")
            else:
                for sale in sales_records:
                    print(f"ID: {sale['product_id']} | Item: {sale['product_name']} | Qty Sold: {sale['quantity_sold']} | Total: ${sale['total_amount']}")

        # --- OPTION 7: GENERATE STORE REPORT ---
        elif choice == '7':
            generate_report()

        # --- OPTION 8: EXIT ---
        elif choice == '8':
            print("\nThank you for using the system. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please choose a number between 1 and 8.")

# Run the program
if __name__ == "__main__":
    main()