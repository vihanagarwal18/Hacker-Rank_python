n=int(input())
str=input() 
l=str.split()
newl=[]
for i in l:
    newl.append(int(i))  
    t=tuple(newl)
print(hash(t))