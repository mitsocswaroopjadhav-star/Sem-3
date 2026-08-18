filename = "file.txt"

# 1. Write data into file
with open(filename, "w") as file:
    file.write("I am learning Advance python.\n")
    file.write("Python is a programming language.\n")
    file.write("File handling is an important concept in Python.\n")
    file.write("Python is easy to learn.")

print("Data written successfully.\n")


# 2. Read the file
with open(filename, "r") as file:
    data = file.read()

print("File Contents:")
print(data)


# 3. Count lines, words and characters
lines = data.splitlines()
words = data.split()
characters = len(data)

print("\nNumber of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)


# 4. Append new data
with open(filename, "a") as file:
    file.write("\nThis is an appended line.")

print("\nData appended successfully.")


# 5. Search for a word
word = input("\nEnter a word to search: ")

with open(filename, "r") as file:
    data = file.read()

if word.lower() in data.lower():
    print("Word found in the file.")
else:
    print("Word not found in the file.")


#output
''''File Contents:
Python is a programming language.
File handling is an important concept in Python.
Python is easy to learn.

Number of lines: 3
Number of words: 18
Number of characters: 107

Data appended successfully.

Enter a word to search: python
Word found in the file.'''

