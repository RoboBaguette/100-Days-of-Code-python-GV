from replit import clear
import art


# Functions for all the operation of the calculator
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


cal = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
ans = ""
# calculator loop
while ans != "n":
    print(art.logo + "\n")
    num_1 = float(input("What's the first number?: "))
    for sym in cal:
        print(sym)
    oper = input("Pick an operation: ")
    num_2 = float(input("What's the second number?: "))
    ans_p = cal[oper](num_1, num_2)
    print(f"{num_1} {oper} {num_2} = {ans_p} ")
    ans = input("type 'y' to continue calculating or type 'n' to end the progaram ")
    clear()
print("The calculator program has ended.")
