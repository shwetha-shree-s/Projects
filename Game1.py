import random
def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors:)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, and computer chose {computer}.")
    if player == computer:
        return "Its a tie!"
    elif player == "rock":
        if computer == "paper":
            return "Papers defeats rock!! You lose."
        else:
            return "Rock destroys scissors!! You Win!!"
    elif player == "paper":
        if computer == "rock":
            return "Papers defeats rock!! You Win!!"
        else:
            return "scissors cuts paper!! You lose."
    elif player == "scissors":
        if computer == "rock":
            return "Rock defeats scissors!! You lose."
        else:
            return "Scissors cut paper!! You Win!!"       

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
