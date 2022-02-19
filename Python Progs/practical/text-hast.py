f=open("E://text-file.txt",'r')
item=[]
for i in f:
    words=i.split()
    for j in words:
	    item.append(j)

print("#".join(item))
