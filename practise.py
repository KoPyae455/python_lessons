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

        def play_rps(self):
            nonlocal player_wins
            nonlocal python_wins

            playerchoice = input(
                "\nEnter... \n for Rock : 1, \n for Paper : 2, \n for Scissor : 3 "
            )

            if playerchoice not in ["1", "2", "3."]
                print("You must enter 1, 2, or 3.")
                return play_rps()

            player = int(playerchoice)

            computerchoice = random.choice("123")

            computer = int(computerchoice)

            print(f"\n You choose {str(RPS(player)).replace('RPS','').title()}.")

            print(
                f"Python chose {str(RPS(computer)).replace('RPS','').title()}.\n"
            )

            def decide_winner (player, computer):
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 2:
                    player_wins += 1
                    return "!! You Win !!"
                elif player == 2 and computer == 1:
                    player_wins
