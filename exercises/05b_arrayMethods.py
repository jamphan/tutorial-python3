original_star_war_movies = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi"
]

print("The 1st Star Wars movie is: " + original_star_war_movies[0])
print("The 2nd Star Wars movie is: " + original_star_war_movies[1])
print("The 3rd Star Wars movie is: " + original_star_war_movies[2])

prequel_star_war_movies = []
prequel_star_war_movies.append("The Phantom Menance")
prequel_star_war_movies.append("Revenge of the Sith")

print("The Prequel Star Wars series include:")
print(prequel_star_war_movies)

print("Woops, we're missing a movie")

prequel_star_war_movies.insert(1, "Attack of the Clones")
print("There, fixed!")
print(prequel_star_war_movies)

all_star_wars_movies = original_star_war_movies + prequel_star_war_movies
all_star_wars_movies.extend([
    "The Force Awakens",
    "The Last Jedi",
    "The Rise of the Skywalker"
])
print("The saga so far...")
print(all_star_wars_movies)

n_movies = len(all_star_wars_movies)
print("There are " + str(n_movies) + " movies in total")

idx_force_awakens = all_star_wars_movies.index("The Force Awakens")
print("The Force Awakens is the " + str(idx_force_awakens + 1) + "th movie in the series")
