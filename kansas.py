
#############################################33

from random import choice

capital = "Gothem City"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the range"

def randomfunfact():
    funfacts = [
        "superheros are helping people and building justice!",
        "Superman is from Kryptonite, he gain his power from yellow sun.",
        "Batman is one of a kind of modern assassin and he was just a human build with flash and bond.",
        "Justice league has existed because of their faith for true justice, both Superman and batman are mighty."
    ]

    index = choice ("0123")

    print(funfacts[int(index)])

if __name__ == "__main__":
    randomfunfact()


################################################
