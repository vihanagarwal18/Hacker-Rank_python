s = input()
length=len(s)
l=[]
for i in range (0,length):
    l.append(s[i])
j=0
while j<=length-1:
    if l[j].isalnum()==True:
        print(l[j].isalnum())
        break
    elif j==length-1:
        print('False')
    j=j+1
j=0
while j<=length-1:
    if l[j].isalpha()==True:
        print(l[j].isalpha())
        break
    elif j==length-1:
        print('False')
    j=j+1
j=0  
while j<=length-1:
    if l[j].isdigit()==True:
        print(l[j].isdigit())
        break
    elif j==length-1:
        print('False')
    j=j+1
j=0  
while j<=length-1:
    if l[j].islower()==True:
        print(l[j].islower())
        break
    elif j==length-1:
        print('False')
    j=j+1    
j=0  
while j<=length-1:
    if l[j].isupper()==True:
        print(l[j].isupper())
        break   
    elif j==length-1:
        print('False')
    j=j+1         
