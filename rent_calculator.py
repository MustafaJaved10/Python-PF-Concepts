# ============================================================
# PF Python - Project: Rent Calculator (Per Person)
# ============================================================

print("=" * 40)
print("       RENT CALCULATOR")
print("=" * 40)

total_rent = int(input("Enter total rent amount: Rs."))
food = int(input("Enter food expense: Rs."))
electricity_units = int(input("Enter total electricity units used: "))
charge_per_unit = int(input("Enter rate per unit: Rs."))
persons = int(input("Enter total number of persons living: "))

total_electricity = electricity_units * charge_per_unit
grand_total = total_rent + food + total_electricity
per_person = grand_total // persons

print("=" * 40)
print(f"Total Electricity Bill: Rs.{total_electricity}")
print(f"Grand Total: Rs.{grand_total}")
print(f"Each person pays: Rs.{per_person}")
print("=" * 40)
