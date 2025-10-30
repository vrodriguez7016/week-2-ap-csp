
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
# greeting = "Hello"
# name = "World"

# # ----------------------------------------
# # Basic String Operations
# # ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "Alexandre"

# Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Lowercase:", name.lower())

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("Uppercase:", name.upper())
print("Uppercase:", name.capitalize())

# Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Uppercase?", name.isupper()) # Output: True


# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14
phrase = "We hold these truths to be self-evident, that alll men are equal, that they are endowed, by their Creator, with certain unalienable rights, that among these are life, liberty, and the pursuit of happiness."
print(len(phrase))


 # ----------------------------------------
 # 3. Indexing and Slicing
 # ----------------------------------------
chicago_mayor = "Johnson"
# print the first letter of mayor
# last character is always -1, first is 0
print(chicago_mayor[0])
print(chicago_mayor[-1])
print(chicago_mayor[4])

print(chicago_mayor[ 4 :])
# the first number is slicing is inclusing
# the second number is excluding a character
print(chicago_mayor[ 0 : 4])
print(chicago_mayor [1:5])
# when we get one character/letter
# its called string indexing
# when we get a chunk of letters
# from a string, its called
# string slicing

phrase3 = supercalifragilistic
print(phrase.upper(supercalifragilistic))
cut = phrase3[0:5]

# Indexing: Access characters by position (0-based index)
print("First character:", chicago_mayor[0])  # Output: J
print("Last character:", chicago_mayor[-1])  # Output: n

# Slicing: Get a range of characters (start inclusive, end exclusive)
print("Characters 1 to 4:", chicago_mayor[0:4])  # Output: John
# first letter is inclusive, next is exclusive
print("Characters 4 to 7:", chicago_mayor[-3:]) # Output: son

last_name = "lastname"
print ("First letter of last name:", last_name[0])

poopins = "supercalifragilisticexpialidocious"
print("last set of letters in poopins:", poopins[-7:])
print(len(poopins))

doi = "WHEN in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature’s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
print(len(doi))
# Example combining everything:
print("Formatted Example:", (phrase + " " + name + "!").upper())
# Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
words2 = sentence.join()
print(words2)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
