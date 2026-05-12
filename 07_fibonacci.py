# ============================================================
# PF Python - Fibonacci Sequence (Recursion & Iterative)
# ============================================================

# --- Method 1: Recursive Fibonacci ---
def fibonacci_recursive(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Recursive - 9th Fibonacci number:", fibonacci_recursive(9))

# --- Method 2: Iterative Fibonacci (returns sequence) ---
def fibonacci_sequence(n):
    """Returns Fibonacci sequence up to n terms."""
    fib_seq = [0, 1]
    if n == 1:
        return [0]
    for x in range(2, n):
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    return fib_seq[:n]

print("Iterative - First 8 terms:", fibonacci_sequence(8))
print("Iterative - First 5 terms:", fibonacci_sequence(5))
print("Iterative - First 6 terms:", fibonacci_sequence(6))
