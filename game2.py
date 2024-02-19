import sys
import random
from enum import Enum

def rps(name='PlayeOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        playerchoice = input(
            f"\n{name}, please enter... \n for Rock : 1, \n for Paper : 2, \n for Scissor : 3  "
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please must enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n"
        )
#the cornor/  Apphrodite
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, !!You Win🥳🎉!!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, !!You Win🥳🎉!!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name}, !!You Win🥳🎉!!"
            elif player == computer:
                return ":| 🟰Tie game🟰 !"
            else:
                python_wins += 1
                return f":P 𓆙 Python Wins𓆙!\nSorry, {name} ..🥺🥺🥺"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game Count : {game_count}")
        print(f"\n{name}'s Wins : {player_wins}")
        print(f"\n Python Wins : {python_wins}")

        print(f"\n Play again, {name}?")

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
            sys.exit(f"😎👌🔥Bye! Bye!😎👌 {name}🔥")

    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a Personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
