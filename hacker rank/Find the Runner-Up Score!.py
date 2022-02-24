n=int(input(""))
str=input()
l=[]
l=str.split()
ilist=[]
for i in l:
    ilist.append(int(i))

s=set(ilist)
newl=list(s)
newl.sort()
len=len(newl)
if len>=2:
    print(newl[len-2])
else:
    print(newl[1])
