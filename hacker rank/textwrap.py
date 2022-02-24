def wrap(string, max_width):
    str=' '+string+' '
    length=len(string)
    i=0
    while i in range(0,length+1):
        if i==0:
            i=i+1
        elif i==1:
            print(str[1],end='')
            i=i+1 
        elif i%(max_width)!=0 and i!=0:
            print(str[i],end='') 
            i=i+1  
        elif i%(max_width)==0:
            print(str[i],end='\n')
            i=i+1
        else:
            break
    return (' ')

wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ",4)