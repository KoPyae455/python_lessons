import random

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissor? please enter the showing 3 variables:").lower()

    if player == computer:
        print("Computer:",computer)
        print("Player : ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose")
        if computer == "scissor":
            print("Computer : ", computer)
            print("Player :", player)
            print("Congrat! You win.")

    elif player == "scissor":
        if computer == "rock":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose")
        if computer == "paper":
            print("Computer : ", computer)
            print("Player :", player)
            print("Congrat! You win.")

    elif player == "paper":
        if computer == "scissor":
            print("Computer : ", computer)
            print("Player : ", player)
            print("You lose")
        if computer == "rock":
            print("Computer : ", computer)
            print("Player :", player)
            print("Congrat! You win.")

    play_again = input("play again? (yes/no) : ").lower()

    if play_again != "yes":
        break

print("What a Great Game!, bye!")
