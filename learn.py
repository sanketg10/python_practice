import matplotlib.pyplot as plt
import numpy as np
import math
tox=9.6*10**-7
u=232
Esat=4*10**4
Vt=1 
W= 10*10**-4 
L=0.6*10**-4
Vds=np.arange(0,5.1,0.1)
Vgs=np.arange(5,0.5,-0.5)
#Vgs=4
Vdsat=np.arange(5,-1,-1)

eox=3.9*8.85*10**-14
Cox=eox/tox

for j in range(len(Vgs)): 
 Vdsat=2*(Vgs[j]-Vt)/(np.sqrt(1+2*(Vgs[j]-Vt)/(Esat*L))+1) 
 print Vdsat
 
#Vdsat=2*(Vgs-Vt)/(np.sqrt(1+2*(Vgs-Vt)/(Esat*L))+1) 
#print Vdsat 
#for i in range(len(Vds)):
   #Ids=(W/L)*u*Cox*((Vgs-Vt)*Vds[i]-Vds[i]**2/2)/(1+Vds[i]/(Esat*L)) 
 
 Ids=(W/L)*u*Cox*((Vgs[j]-Vt)*Vds-Vds**2/2)/(1+Vds/(Esat*L)) 
 print Ids
    
 Idsat=(W/L)*u*Cox*((Vgs[j]-Vt)*Vdsat-Vdsat**2/2)/(1+Vdsat/(Esat*L))
 print Idsat

 for i in range(len(Vds)): 
    #print Vds[i] 
    if Vds[i]>=Vdsat:
       Ids[i]=Idsat 
    if Ids[i]<0: 
       Ids[i]=0
 print Ids 

 plt.plot(Vds,Ids)

plt.show() 
