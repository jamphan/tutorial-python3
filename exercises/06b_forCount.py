# ==================================================================================================
"""
Ex. 06: For Loops

Summary:
    - We look at a particular use case for for-loops, counting
    - We look at the conventional "throwaway" variable (_)
    - We look at string formatting

Explaination:
    - This is similar to the previous exercise with some differences

    - `n_movies += 1` (Line 48)
            The `+=` is known as the iadd() operator, short for "in-place add".
            Other languages may call this an 'increment'.
            This is simply syntactical sugar for `n_movies = n_movies + 1`
            i.e. just a convenience for the programmer.

    - `for _ in` (Line 47)
            The "_" variable is just like any other variable. This one just so happens to look unique
            with a single underscore character as its name.
            By convention, this variable is the "throw-away" variable, where we know we don't actually
            need to use the value of the variable. In this case, we just want to count the number of times
            the for-loop iterates, and never use the variable.

    - f"there are {n_movies}" (Line 50)
            This is called a "f-string" as seen with the leading 'f' character before the opening quotation.
            This provides an easy way to substitute expressions/variables into strings without having to use
            clunky concatenation/formatting. You simply specify a variable to "format into" a string by using
            curly braces. Remember, this can only be done if the 'f' character precedes the string.
"""
# ==================================================================================================

all_star_war_movies = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi",
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith",
    "The Force Awakens",
    "The Last Jedi",
    "The Rise of the Skywalker"
]

n_movies = 0
for _ in all_star_war_movies:
    n_movies += 1

print(f"There are {n_movies} star-wars movies in total")