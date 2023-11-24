def main():
    print("Welcome to the Number Guessing Game!")
    game = "Guessing Game"
    print(game)
    run_game()
    play_again()
def run_game():
    import random
    number=random.randint(1,10)
    tries=0
    unname=input("Enter your Name:")
    unname=unname.strip()
    print("Hello!",unname)
    print("Would you like to Play the game:")
    print("1) Yes")
    print("2) No")
    option=input("Select your option:")
    option=int(option)
    if option==1:
           print("You have to guess a number between 1 to 10:")
           print("You have to guess it in 4 tries:")
           guess=input("Guess a number between 1 to 10:")
           guess=int(guess)
           tries+=1
           if guess<number:
                print("Too Low:")
           if guess>number:
                print("Too High:")
           while guess!=number and tries<4:
                     guess=input("Try Again:")
                     guess=int(guess)
                     tries+=1
                     if guess<number:
                              print("Too Low:")
                     if guess>number:
                              print("Too High:")
           if guess==number:
                     print("CONGRATULATIONS,YOU GUESSED THE CORRECT NUMBER:",number)
                     print("Number of tries:",tries)
           else:
                print("BADLUCK,YOU LOST!")
    elif option==2:
         print("Thank You for joinning us")
    else:
        print("Invalid Option:")
def play_again():
    while True:
        retry = input("Would you like to play again?(yes or no) : ")
        if retry == "yes":
            main()
        if retry == "no":
            exit()
        else:
            print("I'm sorry I could not recognize what you entered")
main()








            
