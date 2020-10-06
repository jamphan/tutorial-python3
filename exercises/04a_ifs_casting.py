# ==================================================================================================
"""
Ex. 04a

Summary:
    - We capture user input from the terminal
    - We determine the user entered a number (using .isnumeric())
    - If the user entered a number, then we return the square of that number
    - Else we tell the user that they did NOT enter a number

Explaination:
    - Line 15: the input() function polls the user to enter text
      the string in-between the paranthesis is called an argument of the function
      For this particular function, the argument is the prompt a user will see before
      the program asks them to enter a value

    - line 22: Because there is a chance of a non-valid input (not a number) we
      need to check if the input is valid before we decide to do any work on it.
      That is, there are two possible pathways we want our program to take.
            If the input is a number --> Do the work
            Else                     --> Do nothing (to avoid errors)

    - line 22: The `.isnumeric()` is called a method. These are similar to functions
      except they are unique to the particular object you are using them on; only
      String objects have the special `.isnumeric()` function.

    - Line 35: Because we now know the input is indeed a number, we need to convert
      the inputted String to an Integer so we can perform mathematical operations
      on it. To do this, we 'cast' the String into an Integer with the int() function
      Note that this cast operation will cause an error if the string does not
      contain a valid numeric value

    - Line 42: Because we want to display the output , we need to cast the Integer
      back as a string

"""
# ==================================================================================================

user_number = input("Enter a number >> ")

if (user_number.isnumeric() == True):
    user_number = int(user_number)**2
    print("The square of your number is: " + str(user_number))
else:
    print("That isn't a number")

