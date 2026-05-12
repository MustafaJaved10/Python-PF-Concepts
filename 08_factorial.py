# ============================================================
# PF Python - Factorial (Recursion & Iterative)
# ============================================================

# --- Method 1: Recursive Factorial ---
def factorial_recursive(n):
    """Returns factorial of n using recursion."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print("Recursive factorial of 5:", factorial_recursive(5))
print("Recursive factorial of 0:", factorial_recursive(0))

# --- Method 2: Iterative Factorial ---
def factorial_iterative(n):
    """Returns factorial of n using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Iterative factorial of 5:", factorial_iterative(5))
print("Iterative factorial of 7:", factorial_iterative(7))

# --- Method 3: Factorial from a list of numbers ---
numbers = [5, 3, 0, 7]
for num in numbers:
    if num < 0:
        print(f"Error: Factorial not defined for negative number: {num}")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        f = 1
        for i in range(1, num + 1):
            f *= i
        print(f"Factorial of {num} is {f}")
