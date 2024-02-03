# ROCK,PAPER , SCISSORS
import random

def game():
    user = input("Choose rock, paper, or scissors: ")
    user = user.lower()
    if user == "quit":
        print("Game Over")
    else:
        options = ["rock", "paper", "scissors"]
        computer = random.choice(options)
        print("Computer chose: ", computer)
        if user == computer:
            print("It's a tie!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cut paper! You lose.")
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cut paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        print("\n")
        game()

game()