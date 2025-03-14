import random

def fun_game():
    print("Welcome to the fun game !")
    print("You have to guess the number between 1 to 10.")
    print("Let's start the game.")
    print()
    secret_number = random.randint(1, 10)
    guess_count = 0
    chances = 5
    print("You have 5 chances to guess the number.")
    print()

    while guess_count < chances:    
        guess = int(input("Enter your guess:"))
        guess_count += 1
        
        match guess:
            case _ if secret_number == guess:
                print("Congratulations, you guessed it!")
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
        print('Guess count:', guess_count)
        print()
    else:
        print("Sorry, you have exhausted all the chances.")
        print("The secret number was:", secret_number)
           
    response = input("Do you want to play again? (yes/no):").lower()
    if response == "yes":
        fun_game()
    else:
        print("Game over!")
fun_game()