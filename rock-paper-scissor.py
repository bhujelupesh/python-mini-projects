import random

options = ["rock","paper","scissor"]

computer_score = 0
user_score = 0

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == 'q':
        print("Quit")
        break
    
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    
    print(f"Computer says: {computer_pick}")
    
    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_score += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_score += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_score += 1  
    elif computer_pick == user_input:
        print("Draw")
    else:
        print("Computer won!")
        computer_score += 1
    
    print(f"Current score: You - {user_score}, Computer - {computer_score}")

print("You won", user_score, "times.")
print("The computer won", computer_score, "times.")
print("Goodbye!")