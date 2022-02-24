def reverse_digits(n):
    new_digit = 0
    while(n > 0):
        a = n % 10
        new_digit = new_digit * 10 + a
        n = n // 10
    return new_digit

length=int(input())
list = list(map(int, input().split()))
reversed_list=[]
if all(element>=0 for element in list):
    for g in list:
        t=reverse_digits(g)
        reversed_list.append(t)
    lengths=len(reversed_list)
    for h in range(0,lengths):
        if reversed_list[h]==list[h]:
            print('True')
            length=length-1
            break
    if length==lengths:
        print('False')
else:
    print('False')
        
