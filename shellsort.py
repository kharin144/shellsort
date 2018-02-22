#!/usr/bin/python

import sys

# iarray = [10, 5, 8, 7, 6, 9, 4, 3, 2, 1, 0, -1]

if( len(sys.argv) < 2 ):
    exit(1)

iarray = sys.argv[1:]
for i in range(len(iarray)):
    iarray[i] = int(iarray[i])

i = 0
sum = 1
steps = [1]
while sum < len(iarray):
    steps.append(pow(2, i) + 1)
    sum += pow(2, i) + 1
    i += 1

# Inverting steps
steps.reverse()

# assert steps, [5, 3, 2, 1]

# Ascending Shell sort
for i in steps:
    for j in range(len(iarray) - i):
        if iarray[j] > iarray[j + i]:
            iarray[j], iarray[j + i] = iarray[j + i], iarray[j]

print(iarray)
