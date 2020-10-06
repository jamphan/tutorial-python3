# ==================================================================================================
"""
Ex. 05: Sequences

Summary:
    - We introduce a new type of data container, sequences (in particular a list)
    - Sequences are NOT data types, they are data STRUCTURES
    - They contain a 'sequence' of data (in our case a sequence of Strings)
    - The program asks the user to enter a movie title
    - It checks if the movie is an avengers movie or not.

Explaination:
    - Line 27: Lists are created with the square braces ('[]'), the whitespace (newline and spaces)
      after the opening brace is optional, and usually done for readability. You can instead type
      it as "avengers_movies = ["The Avengers", "Avengers: Age of Ultron" ...] all on one line.

    - Line 34: `.strip()` is a string method which removes any whitespace before or after the string
      This is done for consistency and to avoid cases where a user enters "The Avengers   " (with
      spaces after).

    - Line 36: The 'in' keyword checks for membership. It checks if the value on the left is a
      member of the sequence on the right.

"""
# ==================================================================================================

avengers_movies = [
    "The Avengers",
    "Avengers: Age of Ultron",
    "Avengers: Infinity War",
    "Avengers: Endgame"
]

user_movie = input("Enter a movie title: ").strip()

if (user_movie in avengers_movies):
    print("This is an Avengers movie!")
else:
    print("This is NOT an Avengers movie")
    print("Here are a list of Avengers movies:")
    print(avengers_movies)