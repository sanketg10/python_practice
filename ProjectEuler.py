import matplotlib.pyplot as plt
import numpy as np
import math 

sum = 0 
number = 1000
for i in range(1,number):  
  if (i%3)==0 or (i%5) == 0:
   sum = sum + i 

print sum
