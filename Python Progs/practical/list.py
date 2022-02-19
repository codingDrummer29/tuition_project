def add(x):
    ele = int(input("Enter no. to add: "))
    x.append(ele)
    print("Your updated list\n", x)
    
def show(x):
    print("Printing your list:\n", x)

def delStart(x):
    ele = x.pop(0)
    print("1st element was: ", ele)
    print("Updated list:\n", x)

def delEnd(x):
    ele = x.pop(-1)
    print("Last element was: ", ele)
    print("Updated list:\n", x)

def delAt(x):
    print("This is your list:\n", x)
    pos = int(input("\nEnter the position of the element you want to delete: "))
    ele = x.pop(pos - 1)
    print("The element was: ", ele)
    print("Updated list:\n", x)

def delVal(x):
    print("This is your list:\n", x)
    val = int(input("\nEnter the element you want to delete: "))
    ele = x.remove(val)
    print("The value was: ", ele)
    print("Updated list:\n", x)

list = [1,2,3,4,5]
print("Your list: ", list)
print("\n\nChoose an option from below:\n1.Add/append element into list\n2.Delete elements from list\n3.Show all elements in the list\n4.Quit\n")
choice1 = int(input())
if choice1 == 1 :
    add(list)
elif choice1 == 3 :
    show(list)
elif choice1 == 4 :
    print("Quiting program")
    exit
elif choice1 == 2 :
    print("Choose an option from below:\nA-Delete at beginning\nB – Delete at end\nC – Delete at position\nD – Delete my value\nE – Exit\n")
    choice2 = input()
    if choice2 == 'A' :
        delStart(list)
    elif choice2 == 'B' :
        delEnd(list)
    elif choice2 == 'C' :
        delAt(list)
    elif choice2 == 'D' :
        delVal(list)
    else :
        print("Exiting program")
        exit
    
    
