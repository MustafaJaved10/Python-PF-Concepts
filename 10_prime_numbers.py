# ============================================================
# PF Python - Prime Number Programs
# ============================================================

import math

# --- Check if a single number is prime ---
def is_prime(num):
    """Returns True if num is prime."""
    if num <= 1:
        return False
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))

# --- Find all primes in a range ---
def check_prime_range(start, end):
    """Returns list of prime numbers between start and end."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("Primes 20-40:", check_prime_range(20, 40))
print("Primes 1-100:", check_prime_range(1, 100))

# --- Process a list: prime stays, even becomes half, odd multiplied by 3 ---
num_list = [2, 3, 4, 7, 9, 10, 13]
result = []
for num in num_list:
    if num <= 0:
        continue
    if is_prime(num):
        result.append(num)
    elif num % 2 == 0:
        result.append(num // 2)
    else:
        result.append(num * 3)

print("Processed list:", result)
