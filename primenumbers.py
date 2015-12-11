import matplotlib.pyplot as plt
import numpy as np
import math  

#n= input('Enter a number: ')

n= input('Enter a number: ')
factor=2
lastFactor=1
while n>1:
 if n % factor==0: 
   lastFactor=factor
   n=n/ factor
 while n %factor==0: 
   n=n / factor
 factor=factor+1
print(lastFactor)


'''
for i in range(2,number-1): 
	if number%i == 0:   
		print(i, "Factors")
		if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0  and i % 11 != 0 and i % 13 != 0 and i % 17 != 0): 
			print (i, "Prime factors greater than 17")
'''
'''
c = 0
sqrtnum = math.sqrt(number) 
mylist = []
floor = int(math.floor(sqrtnum))
for i in range(2,floor):
    if floor%i == 0:  
      print (i)  
      c = c + 1 
      if (c == 1): 
      	print (number/i)

'''
'''
size = n//2
sieve = [1]*size
limit = int(n**0.5)
for i in range(1,limit):
    if sieve[i]:
        val = 2*i+1
        tmp = ((size-1) - i)//val 
        sieve[i+val::val] = [0]*tmp
print( [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0] )
'''
'''
n= input('Enter a number: ')
factor=2
lastFactor=1
while n>1:
 if n % factor==0: 
   lastFactor=factor
   n=n/ factor
 while n %factor==0: 
   n=n / factor
 factor=factor+1
print(lastFactor)
'''
