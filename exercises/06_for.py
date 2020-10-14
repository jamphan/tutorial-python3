# ==================================================================================================
"""
Ex. 06: For Loops

Summary:
    - We introduce a new control structure, the for-loop
    - We are using Python's 'in' keyword to loop through a list

Explaination:
    - line 20: We define a simple list of star wars movies
    - Line 33: Read aloud: "For every element in the all_star_war_movies list, assign it to the
        loop variable 'mv' and perform the functions in the subsequent block".
    - Line 34: the "\t" is called an "escape sequence". When python sees the slash it knows to treat
        the following charater different. In this case, it knows that the programmar does not want
        to use the literal "t" character, instead they want the escaped tab character.

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

print("The Star Wars saga include the movies:")
for mv in all_star_war_movies:
    print("\t" + mv)