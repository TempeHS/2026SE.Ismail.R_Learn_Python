# Put your name
user = input("Enter your name: ")
def player_choice():

choice = input("Enter your choice: ")
    if choice == "rock":
        print("rock"):
    elif choice == "paper":
        print("paper")
    elif choice == "scissors":
        print("scissors")
            else:
        print("choice not valid")

# Computer choice
def computer_choice():
    return random.choice("rock", "paper", "scissors")