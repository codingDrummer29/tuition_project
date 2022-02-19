def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x
   i = 1
   while(i <= smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i
       i+=1
   return hcf  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))
