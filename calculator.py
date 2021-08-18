def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c

print(" ------------------------------- ")
print("| Choose Your Option :          |")
print("| Enter 1 for Addition          |")        
print("| Enter 2 for Substraction      |")
print("| Enter 3 for Muktiplication    |")
print("| Enter 4 for Division          |")
print(" ------------------------------- ")

inp = int(input("\nEnter Your Input : "))

if inp<=0 or inp>=5:
    print("Wrong Input!!!, Try Again...")
    exit()

a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if inp == 1:
    print("Result : ", add(a, b))
elif inp == 2:
    print("Result : ", sub(a, b))
elif inp == 3:
    print("Result : ", mul(a, b))
else:
    print("Result : ", div(a, b))