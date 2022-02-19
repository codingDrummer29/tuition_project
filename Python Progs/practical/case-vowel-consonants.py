f=open("E://text-file.txt",'r')
data=f.read()
print("My file content:\n\n", data)
vowels=0
consonants=0
upper=0
lower=0
other1=0
other2=0
for ch in data:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper += 1
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        lower += 1
    else :
        other1 += 1
    ch=str.lower(ch)
    if ch in"aeiou":
        vowels += 1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        consonants += 1
    else :
        other2 += 1		
print("\nNo of vowels :",vowels)
print("no of consonants:",consonants)
print("no of upper case letters:",upper)
print("no of lower case letters:",lower)
