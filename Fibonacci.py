import matplotlib.pyplot as plt
import numpy as np
import math 

sum = 2
number = 1000 
value_prev = 2
value_prev_prev = 1
value = 3
while(value <= 4000000) :
    value = value_prev + value_prev_prev 
    print value
    if value%2 == 0:
    	sum = sum + value 

    value_prev_prev = value_prev 
    value_prev = value 
    
print sum 


