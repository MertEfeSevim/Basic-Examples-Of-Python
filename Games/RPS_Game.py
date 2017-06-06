import random

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        player = int(input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: "))
        try:
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Enter 1,2,3 not anything else")

def result(player,computer):
    print("You choose ", intToStr(player))
    print("Computer threw ", intToStr(computer))

    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if (player - computer == -2 or player - computer == 1 ):
            print("You win")
            player_score += 1
        elif(player - computer == 2 or player - computer == -1 ):
            print("Computer wins")
            computer_score += 1

def play_again():
    answer = input("Would you like to play again ? y/n" )
    if answer in ("y","Y","yes","Yes","YES"):
        return answer
    else:
        print("Thanks for playing, see you next time")

def scores():
    global  player_score, computer_score
    print("HIGH SCORES")
    print("Player : ",player_score)
    print("Computer : ",computer_score)

def intToStr(a):
    if(a == 1):
        return "rock"
    elif(a == 2):
        return "paper"
    else:
        return "scissors"

if __name__ == '__main__':
    print("Let's Start...")
    while game():
        pass
    scores()