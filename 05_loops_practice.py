# ============================================================
# PF Python - Loops Practice Questions
# ============================================================

# Q1: while loop with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue   # skip 3
    print(i)

# Q2: for loop over tuple
age = (1, 2, 3, 4, 5)
for x in age:
    print(x)

# Q3: for loop with break
ages = (12, 14, 15, 16)
for x in ages:
    if x == 14:
        continue  # skip 14
    print(x)

# Q4: range with step
for i in range(2, 30, 3):   # from 2 to 30, step 3
    print(i)

# Q5: Sum 1 to 100
total_sum = 0
for x in range(1, 101):
    total_sum += x
print("Sum 1-100:", total_sum)

# Q6: Print even numbers 1 to 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Q7: Multiplication table of 6
number = 6
for i in range(0, 11):
    print(f"{number} * {i} = {number * i}")

# Q8: Positive and negative numbers in list
numbers = [1, 2, 3, 4, -1, -2, -3, -4, 0]
positive = 0
negative = 0
zero = 0
for num in numbers:
    if num > 0:
        positive += num
    elif num < 0:
        negative += num
    elif num == 0:
        zero += 1
print(f"Sum of positives: {positive}")
print(f"Sum of negatives: {negative}")
print(f"Zero count: {zero}")

# Q9: FizzBuzz 1 to 30
for x in range(1, 31):
    if x % 3 == 0 and x % 5 == 0:
        print("FIZZBUZZ")
    elif x % 3 == 0:
        print("FIZZ")
    elif x % 5 == 0:
        print("BUZZ")

# Q10: Print prime numbers between 1 and 100
print("Prime numbers between 1 and 100:")
for n in range(2, 101):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

# Q11: Star pattern (triangle)
rows = 5
for x in range(1, rows + 1):
    print('*' * x)

# Q12: Vowel counter in a string
string = "mustafa javed"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{string}': {vowel_count}")

# Q13: Marks grade loop
marks = [85, 45, 90, 56, 20]
for num in marks:
    if num >= 75:
        print("DISTINCTION")
    elif num >= 45:
        print("PASS")
    else:
        print("FAIL")
