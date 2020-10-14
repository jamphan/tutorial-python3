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

    - `..."There are {:d}...` (Line 50)
            The "{:d}" is a placeholder; whenever you see something like "{:}", you know it is a placeholder.
            The "d" character here tells Python that its holding a place for a "digit" (Integer).
            We then substitute the value into the string with the `.format()` method.
            This is called String-Formatting.
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

string_format = "There are {:d} star-wars movies in total"
print(string_format.format(n_movies))