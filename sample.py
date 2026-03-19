from model import Customer, MenuItem, Menu, Order

# ------------------------------------
# 1. Create menu items
# ------------------------------------
burger = MenuItem("Spicy Burger",   9.99, "Mains",    4.5)
soda   = MenuItem("Large Soda",     2.49, "Drinks",   4.0)
fries  = MenuItem("Crispy Fries",   3.99, "Sides",    4.3)
cake   = MenuItem("Chocolate Cake", 5.49, "Desserts", 4.8)
wrap   = MenuItem("Chicken Wrap",   8.49, "Mains",    4.2)

# ------------------------------------
# 2. Build the menu
# ------------------------------------
menu = Menu([burger, soda, fries, cake, wrap])

print("=" * 40)
print("         BYTEBITES MENU")
print("=" * 40)
for item in menu.items:
    print(f"  {item.name:<20} ${item.price:.2f}  [{item.category}]")

# ------------------------------------
# 3. Filter by category
# ------------------------------------
print("\n--- Mains ---")
for item in menu.filter_by_category("Mains"):
    print(f"  {item.name}")

print("\n--- Drinks ---")
for item in menu.filter_by_category("Drinks"):
    print(f"  {item.name}")

# ------------------------------------
# 4. Place an order
# ------------------------------------
order = Order([burger, fries, soda])

# ------------------------------------
# 5. Create a customer and add order
# ------------------------------------
customer = Customer("Paul")
customer.place_order(order)

# ------------------------------------
# 6. Print purchase history
# ------------------------------------
print(f"\n{'=' * 40}")
print(f"  Customer: {customer.name}")
print("=" * 40)
print("\nPurchase History:")
print("-" * 40)
for o in customer.purchase_history:
    print(f"  Date : {o.order_date}")
    for item in o.items:
        print(f"    - {item.name:<20} ${item.price:.2f}")
    print(f"  {'Total':>24} ${o.compute_total():.2f}")
print("-" * 40)
