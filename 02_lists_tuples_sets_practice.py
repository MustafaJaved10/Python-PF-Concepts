# ============================================================
# PF Python - Lists, Tuples & Sets Practice Questions
# ============================================================

# Q1: List operations
fruits = ["mango", "banana", "apple", "kiwi"]
fruits.insert(1, "strawberry")
print(fruits)

# Q2: List filtering - items containing 'a'
new = []
for x in fruits:
    if "a" in x:
        new.append(x)
print("Fruits with 'a':", new)

# Q3: List comprehension
lst = [x for x in range(10) if x < 7]
print(lst)

# Q4: Convert list to uppercase using comprehension
l = ["a", "b", "c"]
n = [i.upper() for i in l]
print(n)

# Q5: Sort list ascending and descending
numbers = [100, 200, 150, 600, 250]
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

# Q6: List reverse
lst2 = [1, 2, 3, 4, 5, 6]
lst2.reverse()
print("Reversed:", lst2)

# Q7: Tuple - convert to list, modify, convert back
x = ("apple", "mango", "banana")
y = list(x)
y[1] = "Strawberry"
x = tuple(y)
print(x)

# Q8: Set operations
school_set = {"hamza", "yahya", "fraud"}
print(school_set)
print("hamza" in school_set)

# Q9: is vs ==
list_a = ["ahmed", "shah", "ali"]
list_b = ["ahmed", "shah", "ali"]
list_c = list_a
print("is same object:", list_a is list_c)   # True
print("is same object:", list_a is list_b)   # False
print("equal values:", list_a == list_b)     # True

# Q10: List comprehension with condition
numbers2 = [1, 2, 3, 4, 5, 6]
double = [x * 2 for x in numbers2]
print("Doubled:", double)
