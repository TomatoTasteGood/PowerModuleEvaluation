#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_EoffRg_125C = -0.01681
p2_EoffRg_125C = 0.2399
p3_EoffRg_125C = 5.823
p4_EoffRg_125C = 283.6

p1_EoffRg_150C = -0.00475
p2_EoffRg_150C = 0.08304
p3_EoffRg_150C = 7.085
p4_EoffRg_150C = 317.1

# 2order
p1_Roff = -3.3e-5
p2_Roff = 0.0234
p3_Roff = 0.9579
# 3order
p1_Roff = -5.703e-5
p2_Roff = 0.0008139
p3_Roff = 0.01976
p4_Roff = 0.9621
#



Rgoff = 1.8
EoffRg_125C_1R2 = p1_EoffRg_125C*Rgoff*Rgoff*Rgoff+p2_EoffRg_125C*Rgoff*Rgoff+p3_EoffRg_125C*Rgoff+p4_EoffRg_125C
EoffRg_150C_1R2 = p1_EoffRg_150C*Rgoff*Rgoff*Rgoff+p2_EoffRg_150C*Rgoff*Rgoff+p3_EoffRg_150C*Rgoff+p4_EoffRg_150C


xList = [float(i/10) for i in range(10,90)]
EoffRg_125C_fit = [p1_EoffRg_125C*i*i*i+p2_EoffRg_125C*i*i+p3_EoffRg_125C*i+p4_EoffRg_125C for i in xList]
EoffRg_150C_fit = [p1_EoffRg_150C*i*i*i+p2_EoffRg_150C*i*i+p3_EoffRg_150C*i+p4_EoffRg_150C for i in xList]

EoffRg_125C_Rate = [i/EoffRg_125C_1R2 for i in EoffRg_125C_fit]
EoffRg_150C_Rate = [i/EoffRg_150C_1R2 for i in EoffRg_150C_fit]

plt.figure()
plt.subplot(2,1,1)
plt.plot(xList, EoffRg_125C_fit,"*-")
plt.plot(xList, EoffRg_150C_fit,"*-")
plt.grid()

plt.subplot(2,1,2)
plt.plot(xList, EoffRg_125C_Rate,"*-")
plt.plot(xList, EoffRg_150C_Rate,"*-")
plt.grid()
plt.show()

fileName = "Eoff_Rate_FF1000R17IE4.csv"
fileTemp = open(fileName, "w")
for i in range(len(EoffRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(",")
    fileTemp.write(str(EoffRg_125C_Rate[i]))
    fileTemp.write("\n")
fileTemp.close()


