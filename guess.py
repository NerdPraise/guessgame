# guess number (three guesses)
# set level easy, med or hard
# easy 1-10, med 1-20, hard 1-50
# game over after three guesses
import random


def user_input(comp_guess, count):
    print(f"You have {count} guesses to work with")
    try:
        user_guess = int(input("What is your guess?\n> "))
        count -= 1
        while count !=0 and user_guess != comp_guess:
            print(f"You have {count} guesses left")
            try:
                user_guess = int(input("That was wrong, try again\n> "))
            except ValueError:
                print("You should have a number put in there ")   
            count -= 1  
        else:
            if count==0 and user_guess != comp_guess:
                print("You ran out of guesses")
                print(f"Actual number is {comp_guess}\n\t\tGAME OVER")
            elif user_guess == comp_guess:
                print("You got it right ")
    except ValueError:
        print("You should have a number put in there ")
    should_continue()
        
def should_continue():
    response = input("(P)lay again or (N)ot ").lower()
    if response == "p":
        play_game()
    elif response == "n":
        pass
    else:
        print("Invalid key, bye bye")
    return 0
    
def choose_level():
    user_level = input("(E)asy\n(M)edium\n(H)ard\nOther keys to quit\n").lower()
    if user_level == "e":
        comp_guess = random.randint(1, 10)
        count = 6
    elif user_level == "m":
        comp_guess = random.randint(1, 20)
        count = 4
    elif user_level == "h":
        comp_guess = random.randint(1, 50)
        count = 3
    else:
        print("Other keys, bye bye")
        return 
    user_input(comp_guess, count)
    

def play_game():
    print("\t\t Welcome to Praise Guessing game")    
    print("What level are you willing to play")
    choose_level()

play_game()