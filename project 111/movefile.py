import os

from_dir= 'C:/Users/Saumya Narsang/Documents'
listoffiles= os.listdir(from_dir)
print(listoffiles)
for i in listoffiles:
    name,ext=os.path.splitext(i)
    print(name)
