import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK =1
            PAPER = 2
            SCISSORS = 3
            
        playerchoice = input(f"\n{name}, Please enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors \n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')} . ")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}. ")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} you win!! 🥳"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} you win!! 🥳"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name} you win!! 🥳"
            elif player == computer:
                return "Tie game!"
            else :
                python_wins += 1
                return f"🐍 Python wins!!\nSorry, {name}..😢"
            
        game_result = decide_winner (player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print (f"\nGame count: {game_count}")
        print (f"\n{name} count: {player_wins}")
        print (f"\nPython count: {python_wins}")

        print(f"\nPlay Again, {name}?")

        while True:
            playagain = input("\nY for yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\nThank you for playing!!! See you next time.🎉🙌")
            sys.exit(f"Bye {name}!!")
    return play_rps
    
if __name__ == "__main__":
    import argparse  #Commond line option and argument parsing library

    parser = argparse.ArgumentParser(description = "Provides a personal game experience.")
    #add arguments to the parser object, in this case we have one required positional argument (name) that takes no additional parameters

    parser.add_argument(
         "-n", "--name", metavar = "name",  #-n and --name is short for name and metavar is also a name
        required = True, help = "The name of the person playing the game."
        )

    args= parser.parse_args()  #method on parser (we called that)
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()