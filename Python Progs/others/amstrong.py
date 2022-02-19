num = int(input("Enter a number: ")) 
# num is the variable that holds the number given 
# by the user 

sum = 0  
# sum set to 0 so that we can sum the value after 
# every loop and finally check with the user given no.

temp = num  
# using a temporary variable to hold the user given no.

while temp > 0: 
   digit = temp % 10  # 153 % 10 = 3
   sum += digit ** 3  # sum = sum + digit(3)^3
   temp //= 10  # temp = temp // 10, [153 // 10 = 15]

# loop untill 153 becomes 15 becomes 1 becomes 0
# and sum = sum + 3^3 + 5^3 + 1^3
# this should make sum = 153 to be an amstrong

if num == sum: # checking if sum is 153, if yes
   print(num,"is an Armstrong number")  # yes
else:  # else
   print(num,"is not an Armstrong number")  # not