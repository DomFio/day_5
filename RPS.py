import random
from turtle import clear
from IPython.display import clear_output

def game():
    game_list = ['rock', 'paper', 'scissors']
    game_list2 = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    name = input("What is your name? ")
    game_type = input("Which game would you like to play? (Classic 'c', Lizard, Spock 'ls', or Quit 'q' )")

    computer_points = 0
    user_points = 0

    if game_type.lower() == 'c':
        while True:
        # clear_output()
                computer = random.choice(game_list)
                weapon = input("\nWhat do you choose? 🤘🧻 ✂  (press 'q' to quit.)")
                clear_output()
                if weapon.lower() == 'q':
                    print("\nThank you for playing!")
                    break
                if weapon.lower() not in game_list:
                    print("\nNot an option... Choose Rock, Paper, or Scissors.\n")
                if computer == weapon.lower():
                    print("\nYou Tied.\n")
                elif computer == 'rock' and weapon.lower() == 'scissors':
                    computer_points += 1
                    print("\nRock smashes Scissors!\n-=Computer Wins!=-\n")
                elif computer == 'paper' and weapon.lower() == 'rock':
                    computer_points += 1
                    print("\nPaper covers Rock!\n-=Computer Wins!=-\n")
                elif computer == 'scissors' and weapon.lower() == 'paper':
                    computer_points += 1
                    print("\nScissors cuts Paper!\n-=Computer Wins!=-\n")
                elif computer == 'scissors' and weapon.lower() == 'rock':
                    user_points += 1
                    print(f"\nRock smashes scissors!\n-={name.title()} Wins!=-\n")
                elif computer == 'rock' and weapon.lower() == 'paper':
                    user_points += 1
                    print(f"\nPaper covers Rock!\n-={name.title()} Wins!=-\n")
                elif computer == 'paper' and weapon.lower() == 'scissors':
                    user_points += 1
                    print(f"\nScissors cuts Paper!\n-={name.title()} Wins!=-\n")
                print("--------Score--------")
                print(f"Computer: {computer_points} | {name.title()}: {user_points}\n")
    elif game_type.lower() == 'q':
        print("You're fun at parties...")

# Lizard Spock game
    if game_type.lower() == 'ls':
        while True:
        # clear_output()
                computer = random.choice(game_list2)
                weapon = input("\nWhat do you choose? 🤘🧻 ✂ 🦎 🖖 (press 'q' to quit.)")
                clear_output()
                if weapon.lower() == 'q':
                    print("\nThank you for playing!")
                    break
                if weapon.lower() not in game_list2:
                    print("\nNot an option... Choose Rock, Paper, Scissors, Lizard, or Spock.\n")
                if computer == weapon.lower():
                    print("\nYou Tied.\n")
                    #Computer wins
                elif computer == 'rock' and weapon.lower() == 'scissors':
                    computer_points += 1
                    print("\nRock destroys Scissors!\nComputer Wins!\n")
                elif computer == 'paper' and weapon.lower() == 'rock':
                    computer_points += 1
                    print("\nPaper covers Rock!\n-=Computer Wins!=-\n")
                elif computer == 'scissors' and weapon.lower() == 'paper':
                    computer_points += 1
                    print("\nScissors cuts Paper!\n-=Computer Wins!=-\n")
                elif computer == 'lizard' and weapon.lower() == 'spock':
                    computer_points += 1
                    print("\nLizard poisons Spock!\n-=Computer Wins!=-\n")
                elif computer == 'lizard' and weapon.lower() == 'paper':
                    computer_points += 1
                    print("\nLizard eats Paper!\n-=Computer Wins!=-\n")
                elif computer == 'spock' and weapon.lower() == 'scissors':
                    computer_points += 1
                    print("\nSpock smashes Scissors!\n-=Computer Wins!=-\n")
                elif computer == 'spock' and weapon.lower() == 'rock':
                    computer_points += 1
                    print("\nSpock vaporizes Rock!\n-=Computer Wins!=-\n")
                elif computer == 'rock' and weapon.lower() == 'lizard':
                    computer_points += 1
                    print("\nRock crushes Lizard!\n-=Computer Wins!=-\n")
                elif computer == 'scissors' and weapon.lower() == 'lizard':
                    computer_points += 1
                    print("\nScissors decapitates Lizard!\n-=Computer Wins!=-\n")
                elif computer == 'paper' and weapon.lower() == 'spock':
                    computer_points += 1
                    print("\nPaper disproves Spock\n-=Computer Wins!=-\n")

                    #user wins
                elif computer == 'scissors' and weapon.lower() == 'rock':
                    user_points += 1
                    print(f"\nRock smashes Scissors!\n-={name.title()} Wins!=-\n")
                elif computer == 'rock' and weapon.lower() == 'paper':
                    user_points += 1
                    print(f"\nPaper covers Rock!\n-={name.title()} Wins!=-\n")
                elif computer == 'paper' and weapon.lower() == 'scissors':
                    user_points += 1
                    print(f"\nScissors cuts Paper!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'lizard' and computer == 'spock':
                    user_points += 1
                    print(f"\nLizard poisons Spock!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'lizard' and computer == 'paper':
                    user_points += 1
                    print(f"\nLizard eats Paper!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'spock' and computer == 'scissors':
                    user_points += 1
                    print(f"\nSpock smashes Scissors!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'spock' and computer == 'rock':
                    user_points += 1
                    print(f"\nSpock vaporizes Rock!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'rock' and computer == 'lizard':
                    user_points += 1
                    print(f"\nRock crushes Lizard!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'scissors' and computer == 'lizard':
                    user_points += 1
                    print(f"\nScissors decapitates Lizard!\n-={name.title()} Wins!=-\n")
                elif weapon.lower() == 'paper' and computer == 'spock':
                    user_points += 1
                    print(f"\nPaper disproves Spock\n-={name.title()} Wins!=-\n")
                print("--------Score--------")
                print(f"Computer: {computer_points} | {name.title()}: {user_points}\n")

game()

