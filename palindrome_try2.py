import matplotlib.pyplot as plt
import numpy as np
import math  

#To calculate the largest palindrome among all products of 3-digit numbers 
r = 1
max = 0
for f in range(1,1000,1): 
	for k in range(1,1000,1): 
		n = f * k 
		#print ( f, k , f*k)
		num = [0] * 6    #To break down the number and see if its a palindrome
		#num2 = [100000] * 100 #To hold all the palindrome values 
		i = 0  
		count = 0
		j = 0 
		while n: 
			#print(n %10) 
			num[i] = n%10 
			n /= 10 
			i = i + 1  

		if i >5: 
			for i in range(0,3):
				if num[i] == num[5-i]:  
					count = count + 1  
					#print ( f, k , f*k, count)
				if count>2: 
					print "This is a palindrome", r, "of", f, "times", k ,"which is", f*k
					r = r + 1
					if f*k > max: 
						max= f*k 
			
print "And the winner is...." 
print "........Maximum palindrome we are looking for is", max




