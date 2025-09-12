import random

print("WELCOME TO BLACKJACK GAME !!!")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

should_continue = True

def check():
    global should_continue
    check = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if check == "y":
        should_continue = True
    else:
        print("Good Bye!!!")
        should_continue = False

def sum(li):
    add = 0
    for i in li:
        add +=i

    return add

def finalcheck(val1,val2):
    if val1 >=21 or val2 >=21:
        if val1 > val2:
            print("You Win")
        else:
            print("Computer Win")
        check()

def drawChecker(com,my):
    if com == my:
       return True
    else:
        return False

def checker():
    checkerVal = input("Type 'y' to get another card, type 'n' to pass: ")
    if checkerVal == "y":
        return True
    else:
        return False
    
def computerSumCheckFor21():
    global computersHand
    global computersum
    if computersum < 17:
        computersHand +=random.choices(cards,k=1)
        computersum = sum(computersHand)
        if computersum >= 21:
            finalcheck(computersum,mysum)
        else:
            computerSumCheckFor21()

def firstGo():
    global computersum
    global mysum
    global computersHand
    global myHand
    computersHand = random.choices(cards,k=2)
    myHand = random.choices(cards,k=2)
    computersum = sum(computersHand)
    mysum = sum(myHand)
    """Ace condition """
    if 11 in cards and (mysum > 21 or computersum >21):
      computersHand.remove(11)
      computersHand.append(1)
      myHand.remove(11)
      myHand.append(1)
      computersum = sum(computersHand)
      mysum = sum(myHand)
         
    ch = print(f"Computer card:  {random.choice(computersHand)}")
    cs = print(f"Computer complete Hand:  {computersHand}")
    print(f"Your cards:  {myHand}")
    print(f"Current Score :  {mysum}")
    print(f"Computer Score :  {computersum}")


while should_continue:
    firstGo()
    if drawChecker(computersum,mysum) == True:
            print("Draw")
            check()
            firstGo()
    
    if mysum == 21:
                print("You Won")
                check()
    elif computersum == 21:
                print("Computer Won")
                check()

    if computersum > 21:
        print("Computer Lost")
    elif mysum > 21:
        print("You Lose")
    else:
        if checker():
            computersHand +=random.choices(cards,k=1)
            myHand +=random.choices(cards,k=1)
            print(f"Computer Hand: {computersHand}")
            print(f"My Hand: {myHand}")
            cs2 = sum(computersHand)
            mys = sum(myHand)
            print(f"Computer Sum: {cs2}")
            print(f"My Sum: {mys}")
            if drawChecker(cs2,mys) == True:
                print("Draw")
                check()
            else:
                finalcheck(mys,cs2)
        else:
            computerSumCheckFor21()
        