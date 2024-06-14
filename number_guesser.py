import random 
user_wins = 0
computer_wins = 0

options = ["Rock", "Paper","scissors"]

options[0]


while True: 
    user_input = input("Type Rock/Paper/Scissor or Q  to quit ").lower()
    if user_input == "q":
        break

    if user_input in options:
            continue
        
        
        
    random_number = random.radint(0,2)
    #rock 0,  paper 1, sissors:2 
    
    
    computer_pick = options[random_number]
    print("computer picked",  computer_pick + ".")

    if user_input == "rock" or computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" or computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "Scissors" or computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        
    else:
        print("You lost!")
        
        computer_wins += 1
        
        
print("You won, " user_wins, "times")
print("The computer won", computer_wins, "times")
print("Goodbye!")