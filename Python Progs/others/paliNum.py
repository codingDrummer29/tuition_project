n = int(input("Enter number:")) # holds user input 121

temp = n # holds user's input temporarrily

rev = 0 # processed value as rev of user-given one

while(n > 0) : # 121 is greater than 0
    dig  = n % 10 # new var dig = 121 % 10 = 1
    rev = rev * 10 + dig # rev = (0 * 10) + 1
    n = n // 10 # n = 121 // 10 = 12
# loops untill n = 121 becomes 12 becomes 1 becomes 0
# rev should become 121 at the end 

if(temp == rev) : # checks if 121 = rev
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")