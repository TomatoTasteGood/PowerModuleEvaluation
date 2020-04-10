#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_ErecRg_125C = -0.2167
p2_ErecRg_125C = 5.344
p3_ErecRg_125C = -45.79
p4_ErecRg_125C = 253

p1_ErecRg_150C = -0.255
p2_ErecRg_150C = 6.313
p3_ErecRg_150C = -54.31
p4_ErecRg_150C = 301.7

# 2order
p1_Ron = 0.01035
p2_Ron = -0.1555
p3_Ron = 1.154
# 3order 
p1_Ron = -0.001055
p2_Ron = 0.02602
p3_Ron = -0.223
p4_Ron = 1.232
#




Rg = 1.2
ErecRg_125C_1R2 = p1_ErecRg_125C*Rg*Rg*Rg+p2_ErecRg_125C*Rg*Rg+p3_ErecRg_125C*Rg+p4_ErecRg_125C
ErecRg_150C_1R2 = p1_ErecRg_150C*Rg*Rg*Rg+p2_ErecRg_150C*Rg*Rg+p3_ErecRg_150C*Rg+p4_ErecRg_150C


xList = [float(i/10) for i in range(10,90)]
ErecRg_125C_fit = [p1_ErecRg_125C*i*i*i+p2_ErecRg_125C*i*i+p3_ErecRg_125C*i+p4_ErecRg_125C for i in xList]
ErecRg_150C_fit = [p1_ErecRg_150C*i*i*i+p2_ErecRg_150C*i*i+p3_ErecRg_150C*i+p4_ErecRg_150C for i in xList]

ErecRg_125C_Rate = [i/ErecRg_125C_1R2 for i in ErecRg_125C_fit]
ErecRg_150C_Rate = [i/ErecRg_150C_1R2 for i in ErecRg_150C_fit]

plt.figure()
plt.subplot(2,1,1)
plt.plot(xList, ErecRg_125C_fit,"*-")
plt.plot(xList, ErecRg_150C_fit,"*-")
plt.grid()

plt.subplot(2,1,2)
plt.plot(xList, ErecRg_125C_Rate,"*-")
plt.plot(xList, ErecRg_150C_Rate,"*-")
plt.grid()
plt.show()

fileName = "Erec_Rate_FF1000R17IE4.csv"
fileTemp = open(fileName, "w")
for i in range(len(ErecRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(",")
    fileTemp.write(str(ErecRg_125C_Rate[i]))
    fileTemp.write("\n")
fileTemp.close()


