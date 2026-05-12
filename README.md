# 🐍 Python Programming Practice — by Mustafa Javed

> A complete collection of Python practice files covering fundamentals to projects, built during my Bachelor's in Computer Science.

---

## 👨‍💻 About Me

Hi! I'm **Mustafa Javed**, a BS Computer Science student who loves learning and implementing programming concepts in a simple and practical way. This repo documents my Python journey — from basics all the way to real mini-projects.

---

## 📁 Repository Structure

```
📦 Python Practice
├── 📄 01_basics_practice.py
├── 📄 02_lists_tuples_sets_practice.py
├── 📄 03_dictionaries_practice.py
├── 📄 04_if_else_practice.py
├── 📄 05_loops_practice.py
├── 📄 06_functions_practice.py
├── 📄 07_fibonacci.py
├── 📄 08_factorial.py
├── 📄 09_palindrome_and_string_reversal.py
├── 📄 10_prime_numbers.py
├── 📄 11_recursion_practice.py
├── 🎮 atm_machine.py
├── 🕐 digital_clock.py
├── 🎯 madlibs_and_number_guessing.py
├── 🏠 rent_calculator.py
├── 🍔 restaurant_ordering_system.py
├── ✊ rock_paper_scissors.py
└── 🔷 shape_patterns.py
```

---

## 📚 Practice Files — Topic by Topic

### 01 · Basics
`01_basics_practice.py`

Covers the core building blocks of Python:
- Variables & data types (`int`, `float`, `str`)
- String slicing & negative indexing
- f-string formatting
- String methods (`replace`, `upper`)
- Boolean values & type casting
- `in` / `not in` operators
- Multi-line strings

---

### 02 · Lists, Tuples & Sets
`02_lists_tuples_sets_practice.py`

- List operations: `insert`, `sort`, `reverse`
- List filtering with loops
- List comprehensions
- Tuple modification (convert → edit → convert back)
- Set membership check
- `is` vs `==` difference
- Doubling list values with comprehension

---

### 03 · Dictionaries
`03_dictionaries_practice.py`

- Creating & accessing dictionaries
- Adding, updating, and removing keys (`pop`, `update`)
- Looping with `.items()`, `.keys()`, `.values()`
- Checking key existence
- Copying dictionaries
- **Nested dictionaries** (cars, family)
- Duplicate keys behavior

---

### 04 · If / Else & Match
`04_if_else_practice.py`

- Basic `if / elif / else`
- Logical operators: `and`, `or`, `not`
- Login system simulation
- Nested if conditions
- Grade checker
- Tax calculator
- Discount system
- Python `match` statement (switch-case style)
- Match with `|` (OR) and guard conditions

---

### 05 · Loops
`05_loops_practice.py`

- `while` loop with `continue`
- `for` loop over tuples
- `break` and `continue` in loops
- `range()` with custom step
- Sum from 1 to 100
- Even numbers 1–50
- Multiplication table
- Positive/negative/zero counter
- **FizzBuzz** (1–30)
- **Prime numbers** (1–100)
- Star triangle pattern
- Vowel counter
- Marks grade loop

---

### 06 · Functions
`06_functions_practice.py`

- Functions with parameters and return values
- Rectangle perimeter & circle area
- Celsius to Fahrenheit converter
- Max of three numbers
- Sum of even numbers in a list
- List to uppercase
- Common elements of two lists
- Numbers above average
- Filter by threshold
- **Lambda functions** (add, subtract, multiply)
- Lambda returning lambda
- `map()` with lambda
- Grade function
- Vowel & consonant counter
- Merge two lists

---

### 07 · Fibonacci
`07_fibonacci.py`

Two approaches to Fibonacci:
- **Recursive** — classic recursive formula
- **Iterative** — builds the sequence using a list

---

### 08 · Factorial
`08_factorial.py`

Three approaches to Factorial:
- **Recursive** — calls itself down to base case
- **Iterative** — uses a for loop
- **From a list** — handles 0 and negative numbers

---

### 09 · Palindrome & String Reversal
`09_palindrome_and_string_reversal.py`

- Reverse a string character by character (loop)
- Reverse each word in a sentence
- Palindrome check (case-insensitive, ignores spaces)
- Palindrome check from a word list

---

### 10 · Prime Numbers
`10_prime_numbers.py`

- `is_prime()` function using square root optimization
- Find all primes in a given range
- Process a list: primes stay, evens get halved, odds multiply by 3

---

### 11 · Recursion Practice
`11_recursion_practice.py`

- Countdown using recursion
- Count up using recursion
- Recursive factorial
- Recursive Fibonacci
- Countdown with custom step (e.g., 50 → 10)

---

## 🎮 Projects

### 🏧 ATM Machine Simulator
`atm_machine.py`

A PIN-protected ATM with a full menu loop:
- Check balance
- Deposit money
- Withdraw money (with balance check)
- Exit

---

### 🕐 Digital Clock (GUI)
`digital_clock.py`

A live digital clock built with **Tkinter**:
- Shows current time (`HH:MM:SS`)
- Updates every second using `.after()`
- Red background, bold font display

---

### 🎯 Mad Libs + Number Guessing Games
`madlibs_and_number_guessing.py`

Three mini-games in one file:
- **Mad Libs** — fill in the blanks, get a funny story
- **Guess the Number (User guesses)** — computer picks, user tries to find it
- **Computer Guesses (User thinks)** — user thinks of number, computer narrows it down using binary search logic

---

### 🏠 Rent Calculator
`rent_calculator.py`

Splits shared living expenses fairly:
- Takes rent, food, electricity units & rate as input
- Calculates total electricity bill
- Divides grand total by number of persons

---

### 🍔 Restaurant Ordering System
`restaurant_ordering_system.py`

A simple console-based food ordering system:
- Displays a menu with prices
- Takes up to 2 item orders
- Validates items against the menu
- Shows total bill

---

### ✊ Rock Paper Scissors
`rock_paper_scissors.py`

Classic game against the computer:
- Computer picks randomly using `random.choice()`
- All win/lose/tie conditions handled
- Input validation included

---

### 🔷 Shape Patterns
`shape_patterns.py`

Console pattern printer with 3 shapes:
- **Hollow Square** — border of X's, empty inside
- **Triangle** — growing `#` rows
- **Inverted Triangle** — shrinking `*` rows

---

## 🛠️ How to Run

Make sure you have **Python 3.x** installed.

```bash
# Run any file like this:
python 01_basics_practice.py

# For the digital clock (needs tkinter):
python digital_clock.py
```

> **Note:** `digital_clock.py` requires `tkinter` which comes built-in with standard Python on Windows/macOS. On Linux, install it with:
> ```bash
> sudo apt install python3-tk
> ```

---

## 🧠 Concepts Covered

| Topic | Concepts |
|---|---|
| Basics | Variables, types, strings, casting, operators |
| Data Structures | Lists, tuples, sets, dictionaries |
| Control Flow | if/else, match/case, logical operators |
| Loops | for, while, break, continue, range |
| Functions | Parameters, return, lambda, map, filter |
| Algorithms | Fibonacci, Factorial, Prime, Palindrome |
| Recursion | Base case, recursive calls, countdown/up |
| Projects | ATM, Clock, Games, Calculator, Patterns |

---

## 📈 Progress

- [x] Python Basics
- [x] Data Structures
- [x] Control Flow
- [x] Loops
- [x] Functions & Lambdas
- [x] Recursion
- [x] Mini Projects
- [ ] OOP (Coming Soon)
- [ ] File Handling (Coming Soon)
- [ ] Modules & Packages (Coming Soon)

---

## 📬 Connect

Feel free to explore, fork, or give feedback!

**Mustafa Javed** — BS Computer Science Student 🎓

---

*"First, solve the problem. Then, write the code." — John Johnson*
