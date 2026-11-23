import random as rand

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = input()

pc_choice = rand.randint(1,3)

if choice == 1 and pc_choice == 1:
elif choice == 1 and pc_choice == 2:
    print("You lose")
elif choice == 1 and pc_choice == 0:
    print("You lose")