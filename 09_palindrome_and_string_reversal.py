# ============================================================
# PF Python - Palindrome Check & String Reversal
# ============================================================

# --- Reverse a string using loop ---
def reverse_word(sentence):
    """Reverses a string character by character."""
    new_sentence = ""
    for char in sentence:
        new_sentence = char + new_sentence
    return new_sentence

print("Reversed 'mustafa':", reverse_word("mustafa"))

# --- Reverse each word in a sentence ---
sentence = "Hello World from Mustafa"
words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = " ".join(reversed_words)
print("Each word reversed:", reversed_sentence)

# --- Palindrome check (ignores spaces, case-insensitive) ---
def check_palindrome(word):
    """Returns True if the word is a palindrome."""
    word = ''.join(word.lower().split())
    return word == word[::-1]

print("'race car' palindrome:", check_palindrome("race car"))    # True
print("'race cars' palindrome:", check_palindrome("race cars"))  # False
print("'madam' palindrome:", check_palindrome("madam"))          # True

# --- Palindrome check from a list of words ---
words_list = ['madam', 'racecar', 'python', 'level', 'hello']
for word in words_list:
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is NOT a palindrome")
