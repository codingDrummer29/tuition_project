def add (n1, n2):
    return n1 + n2

def sub (n1, n2):
    return n1 - n2

def mul (n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

print("This is a simple calculator. Your choices are:\n+ => Addition\n- => Subtraction\n* => Multiplication\n/ => Division\n\n")
choice = input("Enter your choice:")

print("Enter two numbers for A+B or A-B or A*B or A/B:")
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if choice == '+' :
    res = add(a, b)
elif choice == '-' :
    res = sub(a ,b)
elif choice == '*' :
    res = mul(a ,b)
elif choice == '/' :
    res = div(a ,b)
else: print("Wrong Choice")

print("Your desired result for choice ", choice, " is: ", res)
    
