#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_EoffRg_125C =    0.02385
p2_EoffRg_125C =    -0.1871
p3_EoffRg_125C =      55.03
p4_EoffRg_125C =      643.3 

p1_EoffRg_175C =      -0.09485  
p2_EoffRg_175C =        0.6193  
p3_EoffRg_175C =         54.38  
p4_EoffRg_175C =         744.8   

Rgoff=0.68
EoffRg_125C_R56 = p1_EoffRg_125C*Rgoff*Rgoff*Rgoff+p2_EoffRg_125C*Rgoff*Rgoff+p3_EoffRg_125C*Rgoff+p4_EoffRg_125C
EoffRg_175C_R56 = p1_EoffRg_175C*Rgoff*Rgoff*Rgoff+p2_EoffRg_175C*Rgoff*Rgoff+p3_EoffRg_175C*Rgoff+p4_EoffRg_175C

xList = [float(i/10) for i in range(5,90)]
EoffRg_125C_fit = [p1_EoffRg_125C*i*i*i+p2_EoffRg_125C*i*i+p3_EoffRg_125C*i+p4_EoffRg_125C for i in xList]
EoffRg_175C_fit = [p1_EoffRg_175C*i*i*i+p2_EoffRg_175C*i*i+p3_EoffRg_175C*i+p4_EoffRg_175C for i in xList]

EoffRg_125C_Rate=[i/EoffRg_125C_R56 for i in EoffRg_125C_fit]
EoffRg_175C_Rate=[i/EoffRg_175C_R56 for i in EoffRg_175C_fit]

fileName="Eoff_Rate_FF1800R17IP5.csv"
fileTemp=open(fileName,"w")
for i in range(len(EoffRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(',')
    fileTemp.write(str(EoffRg_125C_Rate[i]))
    fileTemp.write(',')
    fileTemp.write(str(EoffRg_175C_Rate[i]))
    fileTemp.write('\n')
fileTemp.close()



# 125C下损耗随Rg上升的更快，用125C的值来替代175C
p1_125C_Roff = 3.504e-05
p2_125C_Roff =-0.0002749
p3_125C_Roff =0.08085
p4_125C_Roff = 0.9451

p1_175C_Roff =-0.0001213
p2_175C_Roff =0.0007919
p3_175C_Roff = 0.0695
p4_175C_Roff =0.9524


rgList= [float(i/10) for i in range(5,50)]
e125c_1 = [p1_125C_Roff*i*i*i+p2_125C_Roff*i*i+p3_125C_Roff*i+p4_125C_Roff for i in rgList]
e175c_1 = [p1_175C_Roff*i*i*i+p2_175C_Roff*i*i+p3_175C_Roff*i+p4_175C_Roff for i in rgList]
plt.figure()
plt.plot(rgList,e125c_1,label="125C")
plt.plot(rgList,e175c_1,label="175C")
plt.grid()
plt.legend()
plt.show()











