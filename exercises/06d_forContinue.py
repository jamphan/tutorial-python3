
star_wars_original = [
    "A New Hope",
    "The Empire Strikes Back",
    "Return of the Jedi"
]

star_wars_prequel = [
    "The Phantom Menace",
    "Attack of the Clones",
    "Revenge of the Sith"
]

star_wars_sequel = [
    "The Force Awakens",
    "The Last Jedi",
    "The Rise of the Skywalker"
]

for mv in (star_wars_original + star_wars_prequel + star_wars_sequel):

    if mv in star_wars_prequel:
        continue

    print(mv)