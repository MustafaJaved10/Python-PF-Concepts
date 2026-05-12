# ============================================================
# PF Python - If/Else & Match Practice Questions
# ============================================================

# Q1: Basic if-else
a = 200
b = 100
if a == b:
    print("Equal")
elif a < b:
    print("A is smaller")
else:
    print("A is bigger than B")

# Q2: and / or / not
x = 9
print(x > 10 and x < 15)          # False
print(not (x > 5 and x < 15))     # False (reversed)
print(x > 5 and x < 15)           # True

# Q3: Login system
username = "Mustafa"
password = 1256
is_verified = True
if username and password and is_verified:
    print("You are logged in")

# Q4: Nested if - Grade check
score = 80
attendance = 100
submitted = False
if score > 50:
    if attendance > 50:
        if submitted:
            print("PASS")
        else:
            print("Pass - Assignment is missing")
    else:
        print("Low attendance")
else:
    print("Fail")

# Q5: Marks grader
marks = 85
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# Q6: Tax calculator (without input)
income = 75000
if income <= 50000:
    tax = income * 0.10
elif 50000 < income <= 100000:
    tax = 5000 + (income - 50000) * 0.20
else:
    tax = 15000 + (income - 100000) * 0.30
print(f"Your tax is {tax}")

# Q7: Discount system
bill = 350
membership = "yes"
discount = 0
if membership == "yes":
    if bill < 100:
        discount = 0.05
    elif 100 <= bill <= 500:
        discount = 0.10
    else:
        discount = 0.15
final_amount = bill - (bill * discount)
print(f"Final amount after discount: {final_amount:.2f}")

# Q8: match statement
day = 4
match day:
    case 1:
        print("Monday")
    case 4:
        print("Thursday")
    case _:
        print("Other day")

# Q9: match with OR conditions
age = 5
match age:
    case 1 | 2 | 3 | 5:
        print("Reached")
    case 6:
        print("Over")

# Q10: match with guard (if condition inside case)
age2 = 10
height = 5
match age2:
    case 1 | 2 | 3 | 4 | 5 | 10 if height == 9:
        print("Good")
    case 1 | 2 | 3 | 5 if height > 4:
        print("Also good")
    case _:
        print("Bye")
