#!/usr/bin/python3

import sys

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

count=0
for i in x:
    if(i.isalnum()):
        count=count+1

count2=0
for i in y:
    if(i.isalnum()):
        count2=count2+1


count3=0
for i in z:
    if(i.isalnum()):
        count2=count2+1

print(count+count2+count3)