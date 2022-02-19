#define all vowels in a list
vowels = ['a', 'e', 'i', 'o', 'u']
special_char = ['!', ':', '-', ')']

#input a string and transform it to lower case
str = input("Enter a string: ").lower()

#define counter variable for both vowels and consonants
v_ctr = 0
c_ctr = 0
space_ctr = 0
special_char_ctr = 0

#iterate through the characters of the input string 
for x in str:
    #if character is in the vowel list,
    #update the vowel counter otherwise update consonant counter
    if x in vowels:
        v_ctr += 1 # v_ctr = v_ctr + 1
    elif x == " " :
        space_ctr += 1
    elif x in special_char :
        special_char_ctr += 1
    else:
        c_ctr += 1

#output the values of the counters
print("Vowels: ", v_ctr)
print("Consonants: ", c_ctr)
print("No. OF Spaces: ", space_ctr)
print("No of Special chars: ", special_char_ctr)
