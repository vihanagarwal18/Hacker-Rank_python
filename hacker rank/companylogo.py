import math
import os
import random
import re
import sys

s = input()
all_freq={}
for i in s:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
#all_freq=sorted(all_freq.items(), key=lambda x: x[1], reverse=True)
all_freq=sorted(all_freq.items(), key=lambda item: (-item[1], item[0]))

dict1=dict(all_freq)

dict_items=dict1.items()
first_3=dict(list(dict_items)[:3])
v1=list(first_3.values())
v2=list(first_3.keys())
for i in range(0,3):
    print(v2[i]," ", v1[i],sep='')