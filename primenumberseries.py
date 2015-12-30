import matplotlib.pyplot as plt
import numpy as np
import math  

#This program is to calculate the difference of sum of squares and square of sums 
arr = [0] * 20000 
def lastFactorfunction(num,initial,firstfactor):  

	for i in range(2,num+1): 
		if num%i == 0: 
			firstfactor = firstfactor + 1 	
			print firstfactor 
			if i == num and firstfactor == 1:  
				arr[initial]=i   
				initial = initial + 1
	return arr

def primeNumber(numseries,count): 
		lastFactor = lastFactorfunction(numseries,0,0) 
		print lastFactor[1]

primeNumber(12,0)




'''
	while num>1: 
		if num % factor==0: 
			lastFactor=factor 
			num=num/factor 
		while num%factor==0:
			num=num/factor
		factor=factor+1
	return lastFactor 
'''


