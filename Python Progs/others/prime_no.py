def prime(num):
    if num>1:
        s=int(num/2)
        print("s: ", s)
        for i in range(2,s+1):
            if num%i==0:
                return("not prime")
                break
        return("prime")
print(prime(240)) 
