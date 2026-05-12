# ============================================================
# PF Python - Functions Practice Questions
# ============================================================

# Q1: Area of rectangle
def my_function(height, weight):
    height = 2 * height
    weight = 3 * weight
    return height + weight
print(my_function(2, 3))

# Q2: Rectangle perimeter
def rectangular_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter
print("Perimeter:", rectangular_perimeter(5, 3))

# Q3: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
print("Temp in Fahrenheit:", celsius_to_fahrenheit(100))

# Q4: Circle area
def circle_area(radius):
    area = 3.14 * radius ** 2
    return area
print("Area of circle:", circle_area(5))

# Q5: Maximum of three numbers
def max_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return num2
print("Max:", max_three(10, 25, 15))

# Q6: Sum of even numbers in a list
def sum_even():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total_sum = 0
    for x in lst:
        if x % 2 == 0:
            total_sum += x
    return total_sum
print("Sum of even numbers:", sum_even())

# Q7: Convert list items to uppercase
def list_string():
    lst1 = ["my name is mustafa"]
    lst2 = []
    for char in lst1:
        lst2.append(char.upper())
    return lst2
print(list_string())

# Q8: Common elements of two lists
def common_elements():
    list1 = [1, 2, 3, 4]
    list2 = [2, 4]
    list3 = []
    for num in list1:
        if num in list2:
            list3.append(num)
    return list3
print("Common:", common_elements())

# Q9: Numbers above average
def above_average():
    lst = [2, 4, 6]
    lst2 = []
    average = sum(lst) / len(lst)
    for num in lst:
        if num >= average:
            lst2.append(num)
    return lst2
print("Above average:", above_average())

# Q10: Filter numbers greater than threshold
def greater_than(numbers, threshold):
    result = []
    for num in numbers:
        if num > threshold:
            result.append(num)
    return result
print(greater_than([1, 2, 3, 4, 5, 6], 3))

# Q11: Lambda - add, subtract, multiply
add = lambda x, y: x + y
sub = lambda a, b: a - b
mul = lambda h, n: h * n
print(add(2, 3), sub(10, 2), mul(10, 10))

# Q12: Lambda with function returning lambda
def height(length):
    return lambda width: length * width
print(height(3)(10))

# Q13: Map with lambda - double all numbers
nums = [1, 2, 3, 4, 5, 6]
double = list(map(lambda x: x * 2, nums))
print("Doubled:", double)

# Q14: Grade function
def grade(marks, subject):
    if marks > 90:
        print(subject, "GRADE A")
    elif marks > 80:
        print(subject, "GRADE B")
    elif marks > 70:
        print(subject, "GRADE C")
    elif marks > 60:
        print(subject, "GRADE D")
    else:
        print(subject, "FAIL")

grade(85, "MATH")
grade(55, "URDU")

# Q15: Count vowels and consonants
def count_vowels(word):
    vowel = "aeiou"
    count_consonants = 0
    count_vowel = 0
    for char in word.lower():
        if char in vowel:
            count_vowel += 1
        elif char.isalpha():
            count_consonants += 1
    return {'vowels': count_vowel, 'consonants': count_consonants}
print(count_vowels("mustafa"))

# Q16: Merge two lists
def merge_list(list1, list2):
    return list1 + list2
print(merge_list([1, 2, 3], [4, 5, 6]))
