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