# ==============================================================================
# Variables & Data Types
# ==============================================================================

# Variable naming rules:
#       - Must only contain alphanumeric + underscores ([a-zA-Z0-9_]
#       - Cannot have spaces
#       - Must start with a letter or underscore
#       - Names are case-sensitive
#       - Cannot be a duplicate of a reserved keyword (e.g. 'print', 'if')

# Variables are declared like so:
# Read-out loud:
#   "Create a container to store data labelled 'my_number' and assign it the
#   value 10"
my_number = 10

# If you use the assign ('=') operator on a previously assigned varaible, the
# value will be overwritten
my_number = "Hello"

# There are different types of data you can use (data types):
a_integer_variable = 10
a_string_variable = "Hello world"
a_boolean_variable = True

# Each data type responds differently to operations.
# For example, adding two integers will give you the mathematical sum of the two:
adding_two_integers = 10 + 20                       # Result = 30
adding_two_strings = "Hello" + ', ' + 'World!'      # Result = "Hello, World!"

# You cannot mix two different data types
will_raise_an_error = 10 + "Hello"

# ==============================================================================
# Booleans Extended
# ==============================================================================

# Booleans are the standard way we communicate "Yes" and "No" with a machine
# They appear when we ask the computer questions
# Read out-loud:
    # "Is the Integer 10 greater than the Integer 5? Store the boolean result
    # in the variable called 'example_boolean'"
example_boolean = 10 > 5

# The ">" is called a conditional operator, some more:
# NB. Paranthesis are optional and only for readiability here
equal_or_less_than = (10 <= 5)      # False
equal_or_greater_than = (10 >= 5)   # True
equal_to = ("Hello" == "hello")     # False
equal_to = ("Hello" == "Hello")     # True
not_equal_to = (10 != 10)           # False
not_equal_to = (False != True)      # True