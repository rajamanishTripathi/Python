import random

print("WELCOME TO BLACKJACK GAME !!!")

cards = [11,2,3,4,5,6,7,8,9,10,10,10]

should_continue = True

def check():
    check = print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if check == "y":
        should_continue = True
    else:
        should_continue = False

def sum(list):
    add = 0
    for i in list:
        add +=i

    return add

# print(f"Hello {sum(cards)}")

while should_continue:
    computersHand = random.choices(cards,k=2)
    myHand = random.choices(cards,k=2)
    computersum = sum(computersHand)
    mysum = sum(myHand)    
    ch = print(f"Computer card:  {random.choice(computersHand)}")
    cs = print(f"Computer complete Hand:  {computersHand}")
    print(f"Your cards:  {myHand}")
    print(f"Current Score :  {mysum}")
    print(f"Computer Score :  {computersum}")

    checker = input("Type 'y' to get another card, type 'n' to pass: ")

    if checker == "y":
        if computersum == mysum:
            ch
            cs
            print("Draw")
            check()
        else:
            should_continue = True
    else:
        should_continue = False
        