f=open("E://text-file.txt",'r')
data=f.read()
print("My file content before change:\n\n", data)

f=open("E://text-file.txt",'r')
f2=open("E:/new-text-file.txt",'w')
l=f.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        f2.write(i)
f2.close()

f2=open("E:/new-text-file.txt",'r')
data=f2.read()
print("\n\nNew generated file content after change:\n\n", data)

f.close()
f2.close()
