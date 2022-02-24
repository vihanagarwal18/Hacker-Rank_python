str=input()
l=str.split()
newl=[]
for i in l:
    newl.append(int(i))
n=newl[0]
m=newl[1]
pattern=".|."
hash="-"
k=int(m-3)
s=6
f=n-2
for i in range(1,n+1):
    if i<=((n-1)/2):
        print(hash*(int(k/2)),pattern*(2*i-1),hash*int((k/2)),sep='')
    elif i==(n+1)/2:
        print(hash*(int((m-7)/2)),"WELCOME",hash*(int((m-7)/2)),sep='')
    else:
        print(hash*int(s/2),pattern*(int(f)),hash*int(s/2),sep='')
        s=s+6
        f=f-2
    k=k-6
    
