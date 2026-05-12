# ============================================================
# PF Python - Project: Restaurant Ordering System
# ============================================================

menu = {
    "pizza": 100,
    "burger": 200,
    "shawarma": 300,
    "drink": 100,
}

print("=" * 35)
print("   WELCOME TO OUR RESTAURANT")
print("=" * 35)
print("MENU:")
for item, price in menu.items():
    print(f"  {item.capitalize()}: Rs.{price}")
print("=" * 35)

total_bill = 0

item_1 = input("Enter the item you want: ").lower()

if item_1 in menu:
    total_bill += menu[item_1]
    print(f"'{item_1}' added to your order.")
else:
    print(f"Sorry, '{item_1}' is not in our menu.")

another_order = input("Do you want to add another item? (yes/no): ").lower()

if another_order == "yes":
    item_2 = input("Enter another item: ").lower()
    if item_2 in menu:
        total_bill += menu[item_2]
        print(f"'{item_2}' added to your order.")
    else:
        print(f"Sorry, '{item_2}' is not available.")

print("=" * 35)
print(f"TOTAL AMOUNT: Rs.{total_bill}")
print("=" * 35)
