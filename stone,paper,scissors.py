import random

print("Hey! Hope you enjoy this game..")
flag = True
p1 = 0
p2 = 0

while flag == True:
    options = ["stone", "paper", "scissors"]
    computer = random.choice(options)
    you = int(input("Enter '1' for 'stone', '2' for 'paper' and '3' for 'scissors': "))
    you = options[you - 1]
    print("Your choice:", you)
    print("My choice:", computer)
    if computer == you:
        print("It's a tie!")
    elif (computer == "stone" and you == "paper") or (computer == "paper" and you == "scissors") or (computer == "scissors" and you == "stone"):
        print("You got a point!")
        p1 += 1
    else:
        print("I got a point!")
        p2 += 1
    print("The points are: You:", p1, "Me:", p2)
    ask = int(input("Do you wish to continue? Enter '1' for 'yes' and '0' for 'no': "))
    if ask == 1:
        continue
    else:
        if p1 > p2:
            print("Congrats! You won..")
        elif p1 < p2:
            print("Sorry! You lost..")
        else:
            print("It's a tie!")
        print("Thankyou for playing!")
        flag = False