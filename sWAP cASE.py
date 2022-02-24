def swap_case(s):
    output=''
    length=len(s)
    for i in range (0,length):
        if s[i].isupper()==True:
            output=output+ (s[i].lower())
        elif s[i].islower()==True:
            output=output+(s[i].upper())
        else:
            output=output+s[i]
    return output