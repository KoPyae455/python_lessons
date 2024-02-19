import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            "\nEnter... \n for Rock : 1, \n for Paper : 2, \n for Scissor : 3  "
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n You chose {str(RPS(player)).replace('RPS','').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n"
        )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "!!You Win🥳🎉!!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "!! you win🥳🎉 !!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "!You Win🥳🎉!"
            elif player == computer:
                return ":| 🟰Tie game🟰 !"
            else:
                python_wins += 1
                return ":P 𓆙 Python Wins𓆙!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game Count : {str(game_count)}")
        print(f"\n Player Wins : {str(player_wins)}")
        print(f"\n Python Wins : {str(python_wins)}")

        print("\n Play again?")

        while True:
            playagain = input("\n y for Yes or \n q to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            play_rps()
        else:
            print("\n *******")
            print("🎉🎉Thank you for playing!🎉🎉\n")
            sys.exit("😎👌🔥Bye! Bye!😎👌🔥")

    return play_rps()

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()
