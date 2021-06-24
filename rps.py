import random
player = None
computer_score = 0
player_score = 0
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = input("rock,paper,scissors?:").lower()
    while player not in choices:
        player = input("rock,paper,scissors?:").lower()
    if player == computer:
            print("computer:",computer)
            print("player:",player)
            print("Tie!!!")
    elif player == "rock":
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("paper covers the rock, so computer won")
            computer_score += 1
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("rock smashes scissors, so player won")
            player_score +=1
    elif player == "paper":
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("scissors cuts the paper, so computer won")
            computer_score += 1
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("paper covers the rock, so player won")
            player_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("rock smashes scissors, so computer won")
            computer_score += 1
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("scissors cuts the paper, so player won")
            player_score += 1
    play_again = input("play again?(yes/no):").lower()
    if play_again != "yes":
        print("final score:")
        print(f"compter score:{computer_score}")
        print(f"player score:{player_score}")
        if computer_score > player_score:
            print("Sooo sad..... Player lost the game:(")
        else:
            print("Congo!! Player won the game")      
        break
print("Thanks for playing.... Have a good day:)")      