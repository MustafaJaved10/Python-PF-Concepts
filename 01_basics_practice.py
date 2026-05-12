# ============================================================
# PF Python - Basics Practice Questions
# ============================================================

# Q1: Variables and Data Types
x = str(3)
y = float(4)
z = int(6)
print(type(x), type(y), type(z))

# Q2: String slicing
b = "HELLO WORLD"
print(b[2:5])   # index 2 to 4
print(b[:5])    # first 5 chars
print(b[1:])    # from index 1 to end

# Q3: f-string formatting
y = 12
x = f"My work is done by {y}"
print(x)

# Q4: String replace
b = "Assalam mu alikum"
print(b.replace("l", "M"))

# Q5: Boolean check
c = "Mustafa"
print(bool(c))   # True because non-empty string

# Q6: Casting
x = float(1)    # int to float
print(x)
x = int(1.9)    # float to int (truncates)
print(x)

# Q7: Check substring in string
txt = "my name is mustafa"
if "name" in txt:
    print("Yes it exists")
else:
    print("No, it does not exist")

# Q8: not in operator
a = "hello mustafa"
if "ahmed" not in a:
    print("No, not here")

# Q9: Negative indexing
a = "mustafa javed"
print(a[-5:-2])
print(a[-7:-1])

# Q10: Multi-line string
a = '''My name is Mustafa. I am a good person.
You have any issue then come to me.
I am free now.'''
print(a)
