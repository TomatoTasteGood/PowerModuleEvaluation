#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_ErecRg_125C =    -4.841
p2_ErecRg_125C =    45.04
p3_ErecRg_125C =    -165
p4_ErecRg_125C =    441.3

p1_ErecRg_175C =      -3.118   
p2_ErecRg_175C =      35.23  
p3_ErecRg_175C =       -165.9  
p4_ErecRg_175C =       561.3   

Rgrec=0.56
ErecRg_125C_R56 = p1_ErecRg_125C*Rgrec*Rgrec*Rgrec+p2_ErecRg_125C*Rgrec*Rgrec+p3_ErecRg_125C*Rgrec+p4_ErecRg_125C
ErecRg_175C_R56 = p1_ErecRg_175C*Rgrec*Rgrec*Rgrec+p2_ErecRg_175C*Rgrec*Rgrec+p3_ErecRg_175C*Rgrec+p4_ErecRg_175C

xList = [float(i/10) for i in range(5,90)]
ErecRg_125C_fit = [p1_ErecRg_125C*i*i*i+p2_ErecRg_125C*i*i+p3_ErecRg_125C*i+p4_ErecRg_125C for i in xList]
ErecRg_175C_fit = [p1_ErecRg_175C*i*i*i+p2_ErecRg_175C*i*i+p3_ErecRg_175C*i+p4_ErecRg_175C for i in xList]

ErecRg_125C_Rate=[i/ErecRg_125C_R56 for i in ErecRg_125C_fit]
ErecRg_175C_Rate=[i/ErecRg_175C_R56 for i in ErecRg_175C_fit]

fileName="Erec_Rate_FF1800R17IP5.csv"
fileTemp=open(fileName,"w")
for i in range(len(ErecRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(',')
    fileTemp.write(str(ErecRg_125C_Rate[i]))
    fileTemp.write(',')
    fileTemp.write(str(ErecRg_175C_Rate[i]))
    fileTemp.write('\n')
fileTemp.close()



# 175C下损耗随Rg上升的降低的更少，用175C的值来替代125C
p1_125C_Rrec = -0.01337
p2_125C_Rrec = 0.1244 
p3_125C_Rrec =-0.4556
p4_125C_Rrec =1.218 

p1_175C_Rrec =-0.006511
p2_175C_Rrec =0.07356 
p3_175C_Rrec =-0.3464
p4_175C_Rrec = 1.172 


rgList= [float(i/10) for i in range(5,50)]
e125c_1 = [p1_125C_Rrec*i*i*i+p2_125C_Rrec*i*i+p3_125C_Rrec*i+p4_125C_Rrec for i in rgList]
e175c_1 = [p1_175C_Rrec*i*i*i+p2_175C_Rrec*i*i+p3_175C_Rrec*i+p4_175C_Rrec for i in rgList]
plt.figure()
plt.plot(rgList,e125c_1,label="125C")
plt.plot(rgList,e175c_1,label="175C")
plt.grid()
plt.legend()
plt.show()











