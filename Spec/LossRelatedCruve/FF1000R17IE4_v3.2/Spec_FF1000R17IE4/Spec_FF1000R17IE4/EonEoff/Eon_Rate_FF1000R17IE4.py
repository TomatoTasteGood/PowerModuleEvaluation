#
#
#
import numpy as np
import matplotlib.pyplot as plt
#
p1_EonRg_125C = 0.004317
p2_EonRg_125C = -5.081
p3_EonRg_125C = 154.5
p4_EonRg_125C = 212.2

p1_EonRg_150C = 0.01297
p2_EonRg_150C = -5.496
p3_EonRg_150C = 164.7
p4_EonRg_150C = 225.6

# 2order
p1_Ron = -0.01285
p2_Ron = 0.3952
p3_Ron = 0.5445
# 3order
p1_Ron = 1.106e-5
p2_Ron = -0.01302
p3_Ron = 0.3959
p4_Ron = 0.5437
#




Rgon = 1.2
EonRg_125C_1R2 = p1_EonRg_125C*Rgon*Rgon*Rgon+p2_EonRg_125C*Rgon*Rgon+p3_EonRg_125C*Rgon+p4_EonRg_125C
EonRg_150C_1R2 = p1_EonRg_150C*Rgon*Rgon*Rgon+p2_EonRg_150C*Rgon*Rgon+p3_EonRg_150C*Rgon+p4_EonRg_150C


xList = [float(i/10) for i in range(10,90)]
EonRg_125C_fit = [p1_EonRg_125C*i*i*i+p2_EonRg_125C*i*i+p3_EonRg_125C*i+p4_EonRg_125C for i in xList]
EonRg_150C_fit = [p1_EonRg_150C*i*i*i+p2_EonRg_150C*i*i+p3_EonRg_150C*i+p4_EonRg_150C for i in xList]

EonRg_125C_Rate = [i/EonRg_125C_1R2 for i in EonRg_125C_fit]
EonRg_150C_Rate = [i/EonRg_150C_1R2 for i in EonRg_150C_fit]

plt.figure()
plt.subplot(2,1,1)
plt.plot(xList, EonRg_125C_fit,"*-")
plt.plot(xList, EonRg_150C_fit,"*-")
plt.grid()

plt.subplot(2,1,2)
plt.plot(xList, EonRg_125C_Rate,"*-")
plt.plot(xList, EonRg_150C_Rate,"*-")
plt.grid()
plt.show()

fileName = "Eon_Rate_FF1000R17IE4.csv"
fileTemp = open(fileName, "w")
for i in range(len(EonRg_125C_Rate)):
    fileTemp.write(str(xList[i]))
    fileTemp.write(",")
    fileTemp.write(str(EonRg_125C_Rate[i]))
    fileTemp.write("\n")
fileTemp.close()


