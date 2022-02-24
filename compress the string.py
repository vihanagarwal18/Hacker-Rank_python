str=input()
l=list(str)
length=len(l)
orderpair={}
count=1
for i in range(0,length):
    if i==length-1:
        print("(",count,", ",l[i],")",sep='',end=' ')
        break
    elif l[i]==l[i+1] and i!=length-1:
        count=count+1
    elif i!=length-1:
        print("(",count,", ",l[i],")",sep='',end=' ')
        count=1