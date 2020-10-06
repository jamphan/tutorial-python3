original_star_war_movies = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi"
]

# We can access the individual elements of an array through "Indexing"
#       The 'index' refers to the position of an element inside an array
#       By using the syntax: `array_name[idx]` you can access the element
#       at the indexed position
#
#       So... `original_star_war_movies[1]` will return the element at index
#       position 1.
#       This is the 2nd element; this is because arrays are zero-indexed.
#       Meaning, the 1st element has an index of 0.
print("The 1st Star Wars movie is: " + original_star_war_movies[0])
print("The 2nd Star Wars movie is: " + original_star_war_movies[1])
print("The 3rd Star Wars movie is: " + original_star_war_movies[2])


# The list data structure has a set of methods available to it, as an example
# the `.append()` method will add an element to the end of the list.
prequel_star_war_movies = []
prequel_star_war_movies.append("The Phantom Menance")
prequel_star_war_movies.append("Revenge of the Sith")

print("The Prequel Star Wars series include:")
print(prequel_star_war_movies)

print("Woops, we're missing a movie")

# Another method is the `.insert(idx, val)` method which will insert `val` at
# the specified `idx` (index), shifting all elements on the right of the index
prequel_star_war_movies.insert(1, "Attack of the Clones")
print("There, fixed!")
print(prequel_star_war_movies)

# Another method is the `.extend(array)` method, which will add `array` to the
# list
all_star_wars_movies = original_star_war_movies + prequel_star_war_movies
all_star_wars_movies.extend([
    "The Force Awakens",
    "The Last Jedi",
    "The Rise of the Skywalker"
])
print("The saga so far...")
print(all_star_wars_movies)

# You can determine the number of elements in a list (or any sequence) by passing
# it to the len() function.

# Here, is an example of why we would use `.methods` and `functions()`.
# Because the len() function is more 'generic' it should not be unique to lists only
# That is, we can determine the len() of many things (like strings). Having to implement
# a `.len()` for each data type/structure is tedious, instead we make a generic len() function.
n_movies = len(all_star_wars_movies)
print("There are " + str(n_movies) + " movies in total")

idx_force_awakens = all_star_wars_movies.index("The Force Awakens")
print("The Force Awakens is the " + str(idx_force_awakens + 1) + "th movie in the series")
