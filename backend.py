# --- 1. Variables & Datatypes ---
cafe_name = "The Cosmic Cafe"
is_ordering = True
tax_rate = 0.08  # 8% Intergalactic tax
customer_wallet = 20.00  # How much money the customer has

# --- 2. Data Structures ---
# Dictionary mapping menu items (Strings) to prices (Floats)
menu = {
    "Nebula Nectar": 4.50,
    "Meteor Meatball Sub": 8.75,
    "Quantum Quiche": 6.20,
    "Void Water": 1.00
}

# List to hold the items the user selects
shopping_cart = []

print(f"Welcome to {cafe_name}!")
print(f"You have ${customer_wallet:.2f} Space Bucks in your wallet.")

# --- 3. Flow Controls ---
while is_ordering:
    print("\n--- MENU ---")
    
    # For loop to display the dictionary items
    for item, price in menu.items():
        print(f"- {item}: ${price:.2f}")
        
    print("-------------")
    choice = input("What would you like to order? (type 'checkout' to pay, or 'exit' to leave): ")
    
    # If/Elif/Else for decision making
    if choice.lower() == 'checkout':
        is_ordering = False
        print("\nProceeding to checkout...")
        
        # Calculate total from the shopping_cart list
        total_cost = 0.0
        for item in shopping_cart:
            total_cost += menu[item]
            
        print("\n=== RECEIPT ===")
        for item in shopping_cart:
            print(f"1x {item}: ${menu[item]:.2f}")
            
        tax_amount = total_cost * tax_rate
        final_total = total_cost + tax_amount
        
        print(f"----------------")
        print(f"Subtotal: ${total_cost:.2f}")
        print(f"Tax (8%): ${tax_amount:.2f}")
        print(f"Total Due: ${final_total:.2f}")
        
        if customer_wallet >= final_total:
            customer_wallet -= final_total
            print(f"\n✅ Payment accepted! Remaining balance in wallet: ${customer_wallet:.2f}")
            print("Enjoy your cosmic meal!")
        else:
            shortage = final_total - customer_wallet
            print(f"\n❌ Insufficient funds. You need ${shortage:.2f} more Space Bucks.")
            print("Please wash dishes in the back to pay off your debt.")
        
    elif choice.lower() == 'exit':
        is_ordering = False
        print("Thanks for stopping by! Fly safe.")
        shopping_cart.clear()
        
    elif choice in menu:
        shopping_cart.append(choice)
        print(f"✅ Added {choice} to your cart!")
        
    else:
        print("❌ Invalid input. We don't serve that in this star system.")