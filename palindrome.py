import matplotlib.pyplot as plt
import numpy as np
import math  

#n= input('Enter a number: ')
#n_str = str(n)
#print (n_str[1]) 
print("This is to test the largest 6 digit palindrome which can be represented as a product of ") 
array = []
for f in range(500,1000,1): 
	for k in range(545,1000,1):  
		print("Yes, the number is a palindrome")
        array.append(f*k)
        length = len(array)
        print length

for t in range(1, length): 
	n = array[t]
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
        for i in range(0,3):
            if num[i] == num[5-i]: 
  	            count = count + 1  
  	              #print ( f, k , f*k, count)
      
  	    if count>2: 
  	    	print (array[t])
	        #print("Yes, the number is a palindrome") 
            #num2[j] = n
            

            #print("Nope, it is not a palindrome") 
       


'''
for m in range(1,5): 
	for k in range(1,5): 
		print(m,k,m *k)
'''

'''
n = numone * numtwo 
print(n)
num = [0] * 6
i = 0  
count = 0
while n: 
    print(n %10) 
    num[i] = n%10 
    n /= 10 
    i = i + 1 

print("0th digit", num[0])
print("6th digit", num[5])

for i in range(0,5):
  if num[i] == num[5-i]: 
  	count = count + 1  

if count==5: 
	print("Yes, the number is a palindrome")
else:
    print("Nope, it is not a palindrome") 
    '''
