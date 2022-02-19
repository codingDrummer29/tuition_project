def left(str):
    str2 = str
    for i in range (0, len(str)-1):
        if(str[0] == " "):
            str2[i].replace(' ', '')
    
    return str2

def right(str):
    str2 = str
    for i in range (0, len(str)-1):
        if(str[len(str) - 1] == " "):
            str2[len(str) - 1].replace(' ', '')
    
    return str2

def both(str):
    str2 = str
    for i in range (0, len(str)-1):
        if(str[0] == " "):
            str2[i].replace(' ', '')
        elif(str[len(str) - 1] == " "):
            str2[len(str) - 1].replace(' ', '')
    
    return str2

def_str = " Computer Science Class XII "

# error op
print("Default string: #", def_str, '#')
print("Left side extra space removed: \n#", left(def_str), '#')
print("Right side extra space removed: \n#", right(def_str), '#')
print("Both side extra space removed: \n#", both(def_str), '#')
        
