import random
random_number = random.randint(1,3)
# print(random_number)
print("Welcome , This is a Stone Paper Scissor Game")


computer_choice = ""

user_input = input("Enter a number 1 for Stone , 2 for Paper , 3 for Scissor : ")

if random_number == 1:
    computer_choice = "Stone"
elif random_number == 2:
    computer_choice = "Paper"
else:
    computer_choice = "Scissor"

#Converting the user input to numbers 
if user_input == "1":
    user_input = "Stone"
elif user_input == "2":
    user_input = "Paper"
else:
    user_input = "Scissor"


# It's a tie
#This is the condition for the tie this execute when the user and the computer choice is the same
if user_input == computer_choice:
    print("It's a tie")
# User wins
elif user_input == "Stone" and computer_choice == "Scissor":
    print("You Win")
elif user_input == "Paper" and computer_choice == "Stone":
    print("You Win")
elif user_input == "Scissor" and computer_choice == "Paper":
    print("You Win")
# Computer wins
elif user_input == "Stone" and computer_choice == "Paper":
    print("You Lose")
elif user_input == "Paper" and computer_choice == "Scissor":
    print("You Lose")
elif user_input == "Scissor" and computer_choice == "Stone":
    print("You Lose")

