def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

should_continue = True
while should_continue:
    check = input("Want to do ops Type: Yes or No    ").lower()
    if check == "yes":
        n1 = float(input("What is your first number"))
        print(" + - * /")
        ope = input("Pick a opertion:    ")
        n2 =  float(input("What is your second number"))

        print(f"The output is:     {ops[ope](n1,n2)}")
    else:
        should_continue = False
        print("Good Bye!!!!")
