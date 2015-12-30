import matplotlib.pyplot as plt
import numpy as np
import math  

#This program is to calculate the difference of sum of squares and square of sums 

def sumofsquares(x): 
	sum = 0  
	sumsquares = 0
	for i in range(1,11): 
		sum = sum + i  
		sumsquares = sumsquares + i*i  
		print i

	print "sum of squares is", sumsquares
	print "square of all sum is", sum* sum 
	print "difference is", sum*sum - sumsquares

sumofsquares(1000)





