file=open("database.txt",'r')
data=file.readlines()
each_lines=[]
for i in data:
    i=i.removesuffix('\n').split(',')
    print(i)
    break
