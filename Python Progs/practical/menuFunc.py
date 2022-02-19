def isSpecial(num):
    x = num
    add = 0
    mul = 1
    while x > 0:
        rem = x % 10
        add += rem
        mul *= rem
        x //= 10
    if num == add + mul :
        return True
    else :
        return False
    
def isAmstrong(num):
    x = num
    add = 0
    while x > 0:
       rem = x % 10
       add += rem ** 3
       x //= 10
    if num == add:
       return True
    else:
       return False
    
def isPrime(num):
    x = num
    if x > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    
def isAutomorphic(num):
    x = num  
    square = num*num      
    while num > 0 :   
        if((num % 10) != (square % 10)):  
            return False                        
        num=num//10                        
        square=square//10
    return True

number = int(input("Enter a integer number: "))

print("\nChoose a option from below to check if ", number, "  is:")
choice = int(input("1. Special Number\n2. Amstrong Number\n3. Prime Number\n4. Automorphic Number\n"))
print("\n")

if choice == 1:
    res = isSpecial(number)
    if res:
        print("Given number ", number, " is a Special Number")
    else :
        print("Given number ", number, " is not a Special Number")
elif choice == 2:
    res = isAmstrong(number)
    if res:
        print("Given number ", number, " is an Amstrong Number")
    else :
        print("Given number ", number, " is not an Amstrong Number")
elif choice == 3:
    res = isPrime(number)
    if res:
        print("Given number ", number, " is a Prime Number")
    else :
         print("Given number ", number, " is not a Prime Number")
elif choice == 4:
    res = isAutomorphic(number)
    if res:
        print("Given number ", number, " is an Automorphic Number")
    else:
        print("Given number ", number, " is not an Automorphic Number")
else : 
        print("Given number ", number, " is an ordinary number")
