def count_substring(string, sub_string):
    count=0
    length=len(string)
    l=len(sub_string)
    for i in range (0,length):
        if sub_string in string[i:i+l]:
            count=count+1
    return  count