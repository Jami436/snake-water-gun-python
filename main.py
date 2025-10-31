# importing random to get a random choice for the opponent

import random

Opponent = random.choice(['0', '1', '2'])

# Taking input from the user
your_choice = input("Enter your choice(0, 1, 2):")

# Mapping the choices to their respective names
dict = {'S': 0, 'W': 1, "G": 2}
reversed_dict = {0: 'S', 1: 'W', 2: 'G'}

# Displaying the choices
print(f'Your choice:{reversed_dict[int(your_choice)]} and Opponent choice:{reversed_dict[int(Opponent)]}')

# Checking the conditions for win, lose or draw
if your_choice == Opponent:
    print("Match Drawn!")
else:
    if(your_choice == '0' and Opponent == '2'):
        print("You Win!")
    elif(your_choice == '1' and Opponent == '0'):
        print("You Win!")
    elif(your_choice == '2' and Opponent == '1'):
        print("You Win!")
    else:
        print("You Lose!")