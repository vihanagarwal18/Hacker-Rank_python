n_and_m= list(map(int, input().split()))
array = list(map(int, input().split()))
aa= set(map(int, input().split()))
bb = set(map(int, input().split()))
happiness=0
for h in array:
    if h in aa:
        happiness=happiness+1
    elif h in bb:
        happiness=happiness-1
print(happiness)