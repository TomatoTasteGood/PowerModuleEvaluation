#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_EonRg_125C =       4.869
p2_EonRg_125C =         -53
p3_EonRg_125C =       543.1
p4_EonRg_125C =       315.1 

p1_EonRg_175C =   4.446      
p2_EonRg_175C =  -52.81      
p3_EonRg_175C =   594.8      
p4_EonRg_175C =   412.7       

Rgon=0.56
EonRg_125C_R56 = p1_EonRg_125C*Rgon*Rgon*Rgon+p2_EonRg_125C*Rgon*Rgon+p3_EonRg_125C*Rgon+p4_EonRg_125C
EonRg_175C_R56 = p1_EonRg_175C*Rgon*Rgon*Rgon+p2_EonRg_175C*Rgon*Rgon+p3_EonRg_175C*Rgon+p4_EonRg_175C

xList = [float(i/10) for i in range(5,90)]
EonRg_125C_fit = [p1_EonRg_125C*i*i*i+p2_EonRg_125C*i*i+p3_EonRg_125C*i+p4_EonRg_125C for i in xList]
EonRg_175C_fit = [p1_EonRg_175C*i*i*i+p2_EonRg_175C*i*i+p3_EonRg_175C*i+p4_EonRg_175C for i in xList]

EonRg_125C_Rate=[i/EonRg_125C_R56 for i in EonRg_125C_fit]
EonRg_175C_Rate=[i/EonRg_175C_R56 for i in EonRg_175C_fit]

fileName="Eon_Rate_FF1800R17IP5.csv"
fileTemp=open(fileName,"w")
for i in range(len(EonRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(',')
    fileTemp.write(str(EonRg_125C_Rate[i]))
    fileTemp.write(',')
    fileTemp.write(str(EonRg_175C_Rate[i]))
    fileTemp.write('\n')
fileTemp.close()



# 125C下损耗随Rg上升的更快，用125C的值来替代175C
p1_125C_Ron = 0.008068
p2_125C_Ron =-0.08783
p3_125C_Ron = 0.9
p4_125C_Ron = 0.5221

p1_175C_Ron =0.00609
p2_175C_Ron = -0.07234
p3_175C_Ron =0.8148
p4_175C_Ron =0.5653


rgList= [float(i/10) for i in range(5,50)]
e125c_1 = [p1_125C_Ron*i*i*i+p2_125C_Ron*i*i+p3_125C_Ron*i+p4_125C_Ron for i in rgList]
e175c_1 = [p1_175C_Ron*i*i*i+p2_175C_Ron*i*i+p3_175C_Ron*i+p4_175C_Ron for i in rgList]
plt.figure()
plt.plot(rgList,e125c_1,label="125C")
plt.plot(rgList,e175c_1,label="175C")
plt.grid()
plt.legend()
plt.show()











