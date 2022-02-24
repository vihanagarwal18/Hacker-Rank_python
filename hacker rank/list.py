list=[]
n=int(input())
for i in range (0,n):
    str=input()
    if str[0]=='i':
        l=str.split()
        newl=[l[0],int(l[1]),int(l[2])]
        list.insert(newl[1],newl[2])
    elif str=='print':
        print(list)
    elif str[2]=='m':
        l=str.split()
        newl=[l[0],int(l[1])]
        list.remove(newl[1])
    elif str[0]=='a':
        l=str.split()
        newl=[l[0],int(l[1])]
        list.append(newl[1]) 
    elif str=="sort":
        list.sort()          
    elif str=="pop":
        length=len(list)
        list.pop(length-1)
    elif str=="reverse":
        list.reverse()  