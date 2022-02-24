n=int(input())
l=[]
for i in range (1,n+1):
    l.append(i)
newl=[]
for j in l:
    newl.append(str(j))
length=len(newl)
for k in range (0,length):
    print(newl[k],sep='',end='')