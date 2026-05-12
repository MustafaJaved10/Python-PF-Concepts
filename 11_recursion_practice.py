# ============================================================
# PF Python - Recursion Practice
# ============================================================

# --- Countdown using recursion ---
def count_down(n):
    if n <= 0:
        print("Achieved!")
    else:
        print(n)
        count_down(n - 1)

count_down(7)

# --- Count up using recursion (print after recursive call) ---
def count_up(n):
    if n <= 1:
        print("Over")
    else:
        count_up(n - 1)
        print(n)

count_up(9)

# --- Recursive factorial ---
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

print("Factorial of 5:", fact(5))

# --- Recursive Fibonacci ---
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("9th Fibonacci:", fibonacci(9))

# --- Recursive countdown with custom step ---
def age_countdown(a):
    if a == 10:
        print("Reached")
    else:
        print(a)
        age_countdown(a - 5)

age_countdown(50)
