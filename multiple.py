import matplotlib.pyplot as plt
import numpy as np
import math  

#This program is to calculate smallest number that is divisible by 1 to 20
#To calculate the largest palindrome among all products of 3-digit numbers 
havntfound = 1 
numbers = 232792500 
#prime = [1,2,3,5,7,11,13,17,19]
while havntfound==1:  
	count = 0
	#for i in prime: 
	for i in range(1,21):
		if numbers%i == 0: 
			count = count + 1   
			print "number right now is", numbers, "and count is" , count, "with i is", i

	if count >= 20: 
		havntfound = 0 
		print numbers

	numbers = numbers + 1
	
