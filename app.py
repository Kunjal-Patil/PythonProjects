import random

print('rock,paper,scissor!!!')
list1 = ['paper', 'scissor', 'rock']
choice_player = input("enter your choice> ")
choice_computer = random.choice(list1)

if choice_player == 'rock':
    if choice_computer == 'paper':
        print("you have lost")
    elif choice_computer == 'scissor':
        print("you have won")
if choice_player == 'paper':
    if choice_computer == 'scissor':
        print("you have lost")
    elif choice_computer == 'rock':
        print("you have won")
if choice_player == 'scissor':
    if choice_computer == 'rock':
        print("you have lost")
    elif choice_computer == 'paper':
        print("you have won")
if choice_player == choice_computer:
    print("its a draw")
