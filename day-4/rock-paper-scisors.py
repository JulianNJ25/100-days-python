import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())

pc_choice = rand.randint(0,2)

if choice == 0:
    print(rock)
if choice == 1:
    print(paper)
if choice == 2:
    print(scissors)

print("Computer  chose:")

if pc_choice == 0:
    print(rock)
if pc_choice == 1:
    print(paper)
if pc_choice == 2:
    print(scissors)


if choice == 1 and pc_choice == 1 or choice == 2 and pc_choice == 2 or choice == 0 and pc_choice == 0:
    print ("It's a draw")
elif choice == 1 and pc_choice == 2 or choice == 2 and pc_choice == 0 or choice == 0 and pc_choice == 1:
    print("You lose")
elif choice == 1 and pc_choice == 0 or choice == 2 and pc_choice == 1 or choice == 0 and pc_choice == 2:
    print("You win")