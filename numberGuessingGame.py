import random

def game():

    guessTime = 0

    number = random.randint(1,40)

    while(True):

        guess = int(input("Enter a guess : "))

        if guess < number:
            print("Your guess is smaller than number, Try one more...")
            guessTime+=1

        elif guess > number:
            print("Your guess is bigger than number, Try one more...")
            guessTime+=1

        else:
            guessTime+=1

            print("Correct guess. You have tried",guessTime,"times")

            again = input("Do you wanna play again :")

            if again == "yes" :
                game()
            else :
                print("Thank you for playing.")
                break



if __name__ == '__main__':
    game()





