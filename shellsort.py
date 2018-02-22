#!/bin/python3

iarray = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

steps = [5, 3, 2, 1]

for i in steps:
	for j in (range(len(iarray) - i) ):
		if iarray[j]>iarray[j+i]:
			iarray[j], iarray[j+i] = iarray[j+i], iarray[j]

print(iarray)
