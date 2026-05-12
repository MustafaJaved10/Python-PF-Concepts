# ============================================================
# PF Python - Project: Shape Patterns
# ============================================================

# --- Hollow Square Pattern ---
def hollow_square(n):
    """Prints a hollow square of size n using X."""
    for i in range(n):
        if i == 0 or i == n - 1:
            print("X " * n)
        else:
            print("X " + "  " * (n - 2) + "X")

print("Hollow Square (size 5):")
hollow_square(5)

# --- Triangle Pattern ---
def triangle(n):
    """Prints a triangle of # symbols."""
    for i in range(1, n + 1):
        print('#' * i)

print("\nTriangle (5 rows):")
triangle(5)

# --- Inverted Triangle ---
def inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

print("\nInverted Triangle (5 rows):")
inverted_triangle(5)
