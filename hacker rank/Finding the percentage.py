n=int(input())
d={}

for i in range(0,n):
    l=[]
    str=input()
    l=str.split()
    d[l[0]]=[l[1],l[2],l[3]]  
name=input()
marks=d[name]
new_marks=[]
for j in marks:
    new_marks.append(float(j))
sum=0
length=(len(new_marks))
for k in new_marks:
    sum=sum+k   
avg=sum/length
print("{:.2f}".format(avg))