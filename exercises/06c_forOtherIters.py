# - When a variable is declared with all caps, it is convention for a Constant variable, a variable that does not change
# - You can multiply string sequences to repeat them. "abc"*3 == "abcabcabc"
HRULE = "="*80

# Here we are printing a header. This is an f-string with the HRULE constant being substituted in.
# We also substitute in the header variable, which we update everytime.
# In between, we also have the escapae sequences "\n" (newline) and "\t" (tab) to make things look
# pretty.
header = "Simple range"
print(f"{HRULE}\n\t{header}\n{HRULE}")
for num in range(0,10):
    print(num)

header = "Even numbers"
print(f"{HRULE}\n\t{header}\n{HRULE}")
for even_nums in range(0,10,2):
    print(even_nums)

header = "Character sequences, Strings"
print(f"{HRULE}\n\t{header}\n{HRULE}")
for char in "Hello, World!":
    print(char)

header = "Lists"
print(f"{HRULE}\n\t{header}\n{HRULE}")
for ele in ["a", 1, "b", 2, "c", 3]:
    print(ele)