import json

MV_DB = "movies.json"

def main():

    try:
        mvdb = get_movies()
    except FileNotFoundError:
        print("File does not exit")
        mvdb = {}
        with open(MV_DB, 'w') as fd:
            json.dump(mvdb, fd)

    if len(mvdb) > 0:
        print(mvdb)

    # Get user input
    choices = {
        1: "Add movie",
        2: "Edit movie"
    }
    if (user_choice := get_user_action(choices)) == 1:
        mv = input("Movie name: ").strip()
        director = input("Director: ").strip()
        rating = input("Your rating 1-5: ").strip()

        add_movie(mvdb, mv, director, rating)

def add_movie(mvdb, mv, director, rating):

    if mv not in mvdb:
        mvdb[mv] = {"director": director, "rating": rating}

    with open(MV_DB, 'w') as fd:
        json.dump(mvdb, fd, indent=4)

def get_user_action(choices: dict) -> int:
    for k,v in choices.items(): print("\t[{:d}]: {:s}".format(k, v))
    print("Choose action:")

    while True:
        choice = input("[1-{:d}]: ".format(len(choices))).strip()

        if not(choice.isnumeric()) or not(1 <= int(choice) <= len(choices)):
            print("Choice must be between 1-2")
        else:
            break

    return int(choice)

def get_movies():

    with open(MV_DB, 'r') as fd:
        mvs = json.load(fd)

    return mvs

if __name__ == '__main__':
    main()