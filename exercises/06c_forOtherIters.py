# - When a variable is declared with all caps, it is convention for a Constant variable, a variable that does not change
# - You can multiply string sequences to repeat them. "abc"*3 == "abcabcabc"
HRULE = "="*80

# Here we are printing a header. This is an f-string with the HRULE constant being substituted in.
# We also substitute in the header variable, which we update everytime.
# In between, we also have the escapae sequences "\n" (newline) and "\t" (tab) to make things look
# pretty.
header = "Simple range"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
for num in range(0,10):
    print(num)

header = "Even numbers"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
for even_nums in range(0,10,2):
    print(even_nums)

header = "Character sequences, Strings"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
for char in "Hello, World!":
    print(char)

header = "Lists"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
for ele in ["a", 1, "b", 2, "c", 3]:
    print(ele)

# Zip is a built-in function, it allows you to iterate multiple objects at once.
# In our case, we iterate two lists, each iterable list being assigned to a separate variable.
header = "Two lists at the same time"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
listA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
listB = [1, 2, 3, 4, 5, 6, 7, 8]
for aa, bb in zip(listA, listB):
    print(f"Value from A: {aa}\t Value from B: {bb}")

# The .split() string method will break up a string into an list of sub-strings based on some
# separating character. By default, it is the space character.
# If you have a comma-separted string such as "item1, item2, item3" you can use .split(",")
header = "Splitting up a sentence"
print(f"\n{HRULE}\n\t{header}\n{HRULE}")
for word in "The quick brown fox jumps over the lazy dog".split():
    print(word)