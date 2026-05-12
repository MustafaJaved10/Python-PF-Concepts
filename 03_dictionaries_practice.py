# ============================================================
# PF Python - Dictionaries Practice Questions
# ============================================================

# Q1: Basic dictionary access
car = {
    "brand": "honda",
    "model": "civic",
    "register": 2006
}
print(car["brand"])
print(car["model"])

# Q2: Add new items
car["color"] = "white"
car["speed"] = 58
car["location"] = "pakistan"
for key, value in car.items():
    print(key, "=", value)

# Q3: Get all keys and values
print("Keys:", car.keys())
print("Values:", car.values())

# Q4: Check if key exists with condition
if "model" in car and car["model"] == "civic":
    print("Yes it exists")
else:
    print("Not found")

# Q5: Update and remove items
car["speed"] = 70
car.update({"model": "corolla"})
print("After update:", car["model"])
car.pop("location")
print("After pop:", car)

# Q6: Copy a dictionary
data = car.copy()
for x, y in data.items():
    print(x, "=", y)

# Q7: Nested dictionary
cars = {
    "honda": {"price": 5000, "color": "red", "model": 2005},
    "toyota": {"price": 3000, "color": "blue", "model": 2020},
    "bugatti": {"price": 6000, "color": "white", "model": 2040}
}
print(cars["toyota"]["price"])

for x, z in cars.items():
    print(x)
    for y in z:
        print(y + ":", z[y])

# Q8: Nested family dictionary
family = {
    "Child1": {"name": "Hamza", "age": 20},
    "Child2": {"name": "Saboor", "age": 22},
    "Child3": {"name": "Yunus", "age": 25}
}
print(family["Child2"]["name"])

for x, y in family.items():
    print(x)
    for z, e in y.items():
        print(z, ":", e)

# Q9: School dictionary with duplicate key (last wins)
school = {
    "name": "Mustafa",
    "Id": 2023,
    "marks": 50,
    "marks": 100,      # duplicate key - 100 will be stored
    "answer": False,
    "classes": ("one", "two", "three")
}
print(school)
print(school.get("marks"))  # gets value by key
