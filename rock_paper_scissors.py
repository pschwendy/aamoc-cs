import random
import time

def print_choices():
    print("Please choose an option")
    print("-----------------------")
    print("r - rock")
    print("p - paper")
    print("s - scissors")
    print("q - quit")
    print("-----------------------")

def check_input(rps: str):
    return rps in ["r", "p", "s", "q"]

def generate_play():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def print_play(computer_rps: str):
    print("Rock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print(f"Shoot! I play {computer_rps}\n")

def choose_winner(user: str, computer: str):
    if user == "r":
        if computer == "rock":
            print("We tied...")
        elif computer == "paper":
            print("Hahaha, I won!")
        else:
            print("You won!")
    elif user == "p":
        if computer == "rock":
            print("You won!")
        elif computer == "paper":
            print("We tied...")
        else:
            print("Hahaha, I won!")
    else:
        if computer == "rock":
            print("Hahaha, I won!")
        elif computer == "paper":
            print("You won!")
        else:
            print("We tied...")
    print("")
    
def main():
    print("Let's play Rock, Paper, Scissors!\n")
    while True:
        print_choices()
        user = input("Rock, paper, scissors? ")
        if not check_input(user):
            continue
        if user == "q":
            print("Thank you for playing!")
            break

        computer = generate_play()
        print_play(computer)
        choose_winner(user, computer)
        
        time.sleep(1)
        print("Should we play again?")

main()

    